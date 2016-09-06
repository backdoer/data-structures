```
//this is a swift code example showing how closures work in swift, example of using a weak reference, the guard statement, for loops

//ASSUMPTIONS: there is a userAPI class that has a getUser function.  This function makes a network call, and returns the user information encoded as JSON.  This code uses a cocoa pod called magical record to work with core data (a database on the physical device running the app)

//here is an example of a closure in swift.  This closure is labeled as a parameter called "completionBlock"  an explict reference to "self" is made in brackets, then the variables the getUser returns are named as "userJSON" and "errorCode".  The logic of the closure is defined after the "in" statement.
userApi.getUser(id, completionBlock: { [weak self](userJSON, errorCode) in //make the reference to self explicitly weak
				guard let strongSelf = self else { return } //guard statement = create strong, immutable instace of self called "strongSelf" if self is not nil, if it's not then return or break out of the closure.
                //guard let statement is a simple way to do error handling in swift
				// error
				if (errorCode != nil || userJSON == nil) {
                    completionBlock(nil, K.Local.UnknownErrorOccurred) //return an error if there's an errorCode
                } else {

                    User.MR_truncateAll() //delete any user object previously stored
                    let apiUser = User.MR_importFromObject(userJSON!)
                    apiUser.lastUpdated = NSDate()

                    // if let statement.  if the cast of "apiUser.favorites" as a set of favorites succeedes, then an immutable variable "favorites" is created and the code inside the curly brackets is executed.  If not the code is skipped and the variable is not created.
                    if let favorites = apiUser.favorites as? Set<Favorite> {

                        var duplicateFavorites = [Favorite]()

                       //example of a swift for in statement.  This works on enumberable data structures such as arrays and dictionaries
                        for favorite in favorites {

                            //short hand syntax for a closure.  "$0" represents a single favorite from the favorites set as the name is not important.
                            let favArray = favorites.filter { $0.id == favorite.id }

                            if (favArray.count > 1) {
                                //C style for loops are deprecated in swift.  Instead, the syntax below should be used.  "..." includes the maximum limit while "..<" does not.
                                for i in 1..<favArray.count { // loop through all except the last item in the array
                                    let tempFavorite = favArray[i]
                                    if (!duplicateFavorites.contains(tempFavorite)) {
                                        duplicateFavorites.append(tempFavorite)
                                    }
                                }
                                strongSelf.defaults.setBool(true, forKey: K.Dev.updateUserKey) // flag the user to be updated
                                strongSelf.defaults.synchronize()
                            }

                        }

                        // loop and delete duplicate favorites
                        for favorite in duplicateFavorites {
                            favorite.MR_deleteEntity()
                        }
                    }

                    //save to core data
                    NSManagedObjectContext.MR_defaultContext().MR_saveToPersistentStoreAndWait()

                    //return the user object
                    completionBlock(apiUser, nil)
				}
    })
	```
