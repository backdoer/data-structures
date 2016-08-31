# Assignment: Choose a Language

Choose an appropriate language to use in this class.  Along with others who choose your language, contribute the following to the course wiki:

* A description and background of your language.  How did it start?  What is it primarily used for?  How popular is it?  What are its strengths and weaknesses?
* An explanation (with examples) of how your programming language manages memory, the call/frame stack, bytecode instructions, etc.  Include information about the stack, heap, pointers and/or references, and garbage collection.

While others in the class will also contribute to your wiki page, you need to author at least one coding example linked to the language page.  Ensure the example is clear and concise, but ensure it is complex enough to illustrate something about the inner workings of your language.  Walk the reader through the development of your program, and show output data.

## Getting Started

The following steps will help you get started:

1. Go to [http://www.bitbucket.com/](BitBucket) and create an account.
1. Ensure `git` works in your terminal (console/command prompt/shell/powershell).  If not, you need to [https://www.atlassian.com/git/tutorials/install-git](install git).  There are graphical front ends, but I highly recommend you learn the terminal commands this semester.
1. Create a directory where you'll keep the files for this course.  We'll call it `byu537`.
1. In terminal, change to the `byu537` directory. Clone the class git repository: `git clone git@bitbucket.org:jdt1204/byu_data_structures.git`.  You should now have a new directory called `byu_data_structures`.  This is where assignments will be posted and where our wiki source is kept.

Next, learn how to write markdown by going [https://confluence.atlassian.com/bitbucketserver/markdown-syntax-guide-776639995.html](a documentation page).  It's pretty easy to pick up. 

## Your Work Session

The following steps are a guide to your work session.  Repeat these steps each time you work on the assignment.

1. In terminal, Change to the `byu537/wiki` directory.
1. Pull all new changes: `git pull`.  There probably won't be any since you just cloned the repository, but it's good practice.
1. Create a branch to work in: `git checkout -b cyl_your_name`.  The `-b` is only required the first time you checkout the branch (it creates the branch).  
     * This branch name is extremely important: the `cyl` is the code for this assignment (I made it up).  Your name is, well, your name.  By using this format, we'll be able to track your branches for assignments and give you credit for your work.
1. Merge any changes in master into your branch: `git merge master`.
     * In the near future, I'll start requiring you to `rebase` your branch on master.  This is a little more complex, so we'll stick with merging for now.
1. Open the files in your favorite editor.  It seems like [https://atom.io/](Atom) is the favorite among most right now.
     * Edit the files.  Everything starts with `README.md`.  Look at the code in the current README.md to see how files can be linked.
     * When you create a directory or file, be sure to add it: `git add --all`.
     * As you work, commit regularly: `git commit -am 'a nice description of my changes'`.
1. When you are finished, push your changes back to the repository: `git push origin cyl_your_name`.  BitBucket should respond nicely when it works.

## Submitting the Assignment

When you are finished with your assignment, follow these steps:

1. Ensure that all your files are committed and pushed to the server.
1. Ensure that you have pulled the most recent changes from the server and you have merged the most recent master into your code.
1. Push with `git push origin cyl_your_name`.

When it is successfully pushed, BitBucket should give you a nice URL that looks something like this:

```
remote: 
remote: Create pull request for choose_a_language:
remote:   https://bitbucket.org/jdt1204/byu_data_structures/pull-requests/new?source=cyl_your_name
remote: 
```

Copy that link into your browser and submit a **Pull Request** for your branch to merge into `master`.  We will look at the contributions and code in your request, give a grade, and merge your content into the master branch.  You'll now see your changes on the site!


## Requirements for this Assignment

There are two parts to this assignment:

1. Contribute to the main language page on our wiki.  The list at the top of this page details examples of what you can contribute.  Others will contribute to this page with you.
1. Create a **new page** that is linked from your main language page.  You will be the sole author of this page.  Write a program in your language that shows off some capability of your language.  Your program should be 50-100 lines long (that's a rough guide).  On your page, walk the reader through the development of your program.  Explain the concepts  and algorithms your program uses.  Show input and output data.

