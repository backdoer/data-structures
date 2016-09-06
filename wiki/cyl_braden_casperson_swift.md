# Swift Camera-Use Example

```//
//  Created by Braden Casperson on 9/5/16.
//  Copyright © 2016 Braden Casperson. All rights reserved.
//

import UIKit
import Photos

class RecentActivityViewController : UITableViewController, UIImagePickerControllerDelegate {

    // MARK: - Properties

    //The userDefaults allow defaults to be saved to a user device, an iPhone or iPad...or iPod.
    private let userDefaults = NSUserDefaults.standardUserDefaults()

    //pickedImage is optional since it will be null initially, until they've taken a picture.
    var pickedImage: UIImage?

    //this grabs an id that had previously been saved in the userDefaults
    let userId = String(NSUserDefaults.standardUserDefaults().stringForKey("token"))

    //this is a timer that can be set.
    var postTimer = NSTimer()
    var userTimer = NSTimer()

    //This is how you can determine the location of a user.
    var locManager = CLLocationManager()

    //This is interesting. Swift uses segues to move between view controllers in the storyboard.
    //Sometimes you want to go to a new storyboard view and do something and once that is completed,
    //you may want to go back to previous viewController storyboard. You do this with an unwind.
    @IBAction func unwindToMenu(segue: UIStoryboardSegue) {}

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    //an IBAction is something that when interacted with, causes something to happen, usually a button.
    @IBAction func takePicture(sender: AnyObject) {
        //this creates an imagePicker object which can access a devices camera.
        let imagePicker = UIImagePickerController()
        imagePicker.delegate = self

        //Here we check if the device even does have a camera and if it is available.
        //If it does, then we proceed to set up the object's availabletypes and opens the camera.
        if UIImagePickerController.isSourceTypeAvailable(.Camera) {
            imagePicker.sourceType = UIImagePickerControllerSourceType.Camera
            if let availableTypes = UIImagePickerController.availableMediaTypesForSourceType(.Camera) {
                if (availableTypes as NSArray).containsObject(kUTTypeMovie) {
                    imagePicker.mediaTypes = [kUTTypeMovie as String]
                    imagePicker.mediaTypes = [kUTTypeImage as String]
                    imagePicker.allowsEditing = false
                    self.presentViewController(imagePicker, animated: true, completion: nil)
                    // proceed to present the picker
                }
            }
        }
    }

    //this is the function for the imagePicker once you have taken the picture.
    //It will save the image to a variable, and then perform segue.
    func imagePickerController(picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject]) {

        if let image: UIImage = info["UIImagePickerControllerOriginalImage"] as? UIImage {
            pickedImage = image
            self.dismissViewControllerAnimated(true, completion: nil)
            self.performSegueWithIdentifier("Show New Post", sender: self)
        }
    }

    //in the case that the user exits the camera before taking a picture.
    func imagePickerControllerDidCancel(picker: UIImagePickerController) {
        self.dismissViewControllerAnimated(true, completion: nil)
    }

    //this function happens when a segue is called. The pickedImage that was taken
    //with the camera is then passed on to the next view and used however it is needed.
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "Show New Post" {
            if let destVC = segue.destinationViewController as? NewPostViewController {
                destVC.uploadImage = self.pickedImage
            }
        }
    }
}```
