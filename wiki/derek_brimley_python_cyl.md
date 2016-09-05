OK, so I got the framework for this code from a tutorial, [found here](http://blog.mollywhite.net/twitter-bots-pt2/). But most of the code is my own. 

I was interested in learning how to make a Twitter bot, and figured this would be a good opportunity. I decided to make a bot that would tweet random 
verses of the Book of Mormon. Later, I decided to combine 3 random verses together, and see what came up. I have a database of all the LDS scriptures,
that you can [download here](http://scriptures.nephi.org/). So that's where I got them from.

Let's go through the code! First things first:

```python
import os
import tweepy
from secrets import *
from time import gmtime, strftime
import MySQLdb
import random
```

Tweepy is the library that makes it easy to tweet programmatically. Secrets is another python file with the keys and passwords for the bot account. MySQLdb lets me connect to my local MySQL database. And you know what the random library is for.

Moving on.


```python
#CONNECT TO THE DATABASE, GRAB THE BOOK IDS FROM BOOK OF MORMON
db = MySQLdb.connect(host="localhost",user="root",passwd="",db="scriptures")
cur = db.cursor()
books_result = cur.execute(
	"SELECT id FROM books WHERE volume_id = 3"
)

books = cur.fetchall()

```

This code is used to connect to my database. You create a db connection, and then a cursor, which is used to run queries. Weirdly, the query returns a count of the results, so you need to run fetchall() to get the actual results. 

```python

#CREATE SCRIPTURE OBJECT
scripture_options = {}

for book in books:
	#LEVEL 1
	scripture_options[book[0]] = {}

	sql_string = "SELECT id FROM chapters WHERE book_id = " + str(book[0])
	chapters_result = cur.execute(
		sql_string
	)
	chapters = cur.fetchall()
	for chapter in chapters:
		#LEVEL 2
		scripture_options[book[0]][chapter[0]] = []
		
		sql_verse_string = "SELECT id FROM verses WHERE chapter_id = " + str(chapter[0])
		
		verses_result = cur.execute(
			sql_verse_string
		)
		verses = cur.fetchall()
		verses_list = []
		for verse in verses:
			#LEVEL 3!
			verses_list.extend(verse)
		scripture_options[book[0]][chapter[0]] = verses_list
```

I wanted to build the structure of the Book of Mormon into a dictionary, so that I would have the database IDs that I would need to choose at random. Later, I realized that I could just figure out the range of verse IDs that correspond to the Book of Mormon. But I kept this dictionary, because it took me forever to figure it out, and I'm proud of it. The dictionary will is structured like this:

*Book 1
    *Chapter 1
	    *Verse 1
		*Verse 2
		*Verse 3
		*Verse 4
		*Verse 5
		*Verse 6
	*Chapter 2
	*Chapter 3
*Book 2
*Book 3

Data structures FTW!

```python
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)
```

Tweepy stuff.


```python
# ====== Individual bot configuration ==========================
bot_username = 'RobotOfMormon'
logfile_name = bot_username + ".log"

# ==============================================================
```
Setting the Twitter username...

Here comes the good stuff:

```python
def get_random_verse():
	db = MySQLdb.connect(host="localhost",user="root",passwd="",db="scriptures")
	cur = db.cursor()
	
	#GET RANDOM BOOK ID
	books = []
	for book_option in scripture_options:
#		print(book_option)
		books.append(book_option)
	book_choice = random.choice(books)
#	cur.execute(
#		"SELECT book_title FROM books where id = " + str(book_choice)
#	)
#	book_title = cur.fetchall()
	
	#GET RANDOM CHAPTER ID
	chapters = []
	for chapter_option in scripture_options[book_choice]:
#		print(chapter_option)
		chapters.append(chapter_option)
		
	chapter_choice = random.choice(chapters)
#	cur.execute(
#		"SELECT chapter_number FROM chapters where id = " + str(chapter_choice)
#	)
#	chapter_number = cur.fetchall()
	
	#GET RANDOM VERSE ID
	verses = []
	for verse_option in scripture_options[book_choice][chapter_choice]:
		verses.append(verse_option)
		
	verse_choice = random.choice(verses)

	#GET THE VERSE TEXT AND NUMBER
	cur.execute(
		"SELECT verse_number, scripture_text FROM verses where id = " + str(verse_choice)
	)
	random_verse = cur.fetchall()
	random_verse_text = random_verse[0][1]
	db.close()
	
#	print(str(book_title[0][0]) + ' ' + str(chapter_number[0][0]) + ', verse ' + str(random_verse_number) + ' - "' + str(random_verse_text) + '"')
	
	return random_verse_text
```

Pretty simple. This uses the dictionary built above to get a random book, chapter, and verse from the book of mormon, and return the text of the verse. I was going to include the verse number/chapter/book in the Tweet, but then I realized that 140 characters isn't enough room for a lot of verses. And then I decided that I wanted to mash up several verses anyways. Which brings us to...

```python
def create_tweet():
	
	#GET THREE RANDOM VERSES
	verse_1 = get_random_verse()
	verse_2 = get_random_verse()
	verse_3 = get_random_verse()

	#GET FIRST 10 WORDS OF VERSE 1
#	print(verse_1,verse_2,verse_3)
	verse_1_words = verse_1.split()
	verse_1_words = verse_1_words[:10]
	verse_1_substr = " ".join(verse_1_words)
#	print(verse_1_substr)
	
	#GET WORDS 6 THROUGH 10 OF VERSE 2
	verse_2_words = verse_2.split()
	verse_2_words = verse_2_words[5:10]
	verse_2_substr = " ".join(verse_2_words)
#	print(verse_2_substr)
	
	#GET LAST 5 WORDS OF VERSE 3
	verse_3_words = verse_3.split()
	verse_3_words = verse_3_words[5:]
	verse_3_substr = " ".join(verse_3_words)
#	print(verse_3_substr)
	
	#PUT 'EM ALL TOGETHER
	combined_text = verse_1_substr + ' ' + verse_2_substr + ' ' + verse_3_substr
	print(combined_text)
	return combined_text
```

Got it? So this grabs three random verses, takes a few words from each, mashes them together, and returns the combined string. There's probably a more elegant way to do this, but it's too late now.

```python
def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
        print("success!")
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)
```

These two functions, or 'defs', were given to me by the tutorial. They do all the Tweepy stuff of authenticating, connecting to the Twitter API, and tweeting the tweet. And logging that it occurred.

And lastly...

```python
if __name__ == "__main__":
	#INFINITE LOOP
	while True:
		tweet_text = create_tweet()
		if len(tweet_text) <= 140:
			tweet(tweet_text)
			break
```

This is the code that runs it. I put it all in an infinite loop so that it would keep running until it built a tweet that was 140 characters or less, and then break out. You can see some of the results by following @RobotOfMormon on Twitter. Thank you.