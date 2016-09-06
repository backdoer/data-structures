# Calling the OpenWeatherMap API with Swift via AlamoFire

AlamoFire makes networking with Swift easy. To demonstrate just *how* easy, here's a small little tutorial on how to call the OpenWeatherMap API from Swift using AlamoFire.

## Side-note on OpenWeatherMap API

The OpenWeatherMap API documentation can be found at [openweathermap.org/api](). It's a free, simple API for getting weather data. All you need is an API key, which you can obtain on their site. Head on over to get one, then come on back to get started!

## Our Setup

To make this code example as simple as possible, I wanted to call this API from an Xcode Playground, rather than creating a full-fledged app. The goal of this tutorial is to show how simple AlamoFire makes networking, therefore a UI isn't going to help get that point across. Also, running our example in a Playground will allow us to see instantaneous feedback, rather than having to run the simulator over and over to get it right.

Unfortunately, getting a CocoaPod inside of an Xcode playground isn't the most straightforward, easy thing to do (check out this [SO article](http://stackoverflow.com/questions/33367609/how-to-use-cocoapods-with-playground)). I spent a couple of hours wrestling with getting AlamoFire into a playground, only to find that the when I had it there, the response data wasn't accessible because the people behind AlamoFire removed Playground functionality in their most recent release. So, we will be creating a new single page app and testing the code inside an app.

**Note**: This tutorial assumes that you have some Xcode experience, including creating Outlets and Actions, and editing settings for UI elements.

PS. My macOS version for this tutorial is 10.11.6. My Xcode version is 7.3.1.

So, let's start by installing AlamoFire.

## Installing AlamoFire

The creators of AlamoFire make it simple to install and use; the easiest method to do so is via [CocoaPods](https://cocoapods.org/), the package-manager for iOS / macOS projects. *Think `pip` for Swift / Objective-C.*

**Note**: The rest of this tutorial assumes that you have (or will install) CocoaPods 1.0.0 or higher!

Start by installing CocoaPods, if you haven't already, by running this in your terminal:

```bash
sudo gem install cocoapods
```

If you run into an error that says that you need to update Ruby in order to download CocoaPods, follow these steps:

```bash
# Update Homebrew (if installed, if not, skip this)
brew update
# Download RVM
curl -sSL https://get.rvm.io | bash -s stable --ruby
# If not using bash, make sure rvm command is available
source /Users/USERNAME/.rvm/scripts/rvm
# If newer version of ruby was downloaded while downloading RVM, make it default
rvm use 2.3.0 --default
# Else, download newer version of Ruby and make it default
rvm install 2.3.0
rvm use 2.3.0 --default
```

Next, we'll need to create an Xcode project. Create the project (easiest to use the Single-View Application template), name it whatever you'd like, and save it in the directory that you'd like to have your Playground eventually reside in.

Now in your terminal, navigate to the new project's directory and then run `pod install` to generate your `podfile` (the file in which you declare your CocoaPods dependencies). Then, edit your `podfile` so that it looks something like this:

```ruby
# Uncomment this line to define a global platform for your project
platform :ios, '9.0'

target 'AlamoFireTest' do
  # Comment this line if you're not using Swift and don't want to use dynamic frameworks
  use_frameworks!

  # Pods for AlamoFireTest
  pod 'Alamofire'

  target 'AlamoFireTestTests' do
    inherit! :search_paths
    # Pods for testing
  end

  target 'AlamoFireTestUITests' do
    inherit! :search_paths
    # Pods for testing
  end

end
```

Once done editing it, save it and return to your terminal. Run `pod install` to generate your Workspace file (the file that you would use to work on your full app project instead of the one that Xcode generated for you).

At this point, you might hit an error that looks something like this:

```
[!] Unable to add a source with url `https://github.com/CocoaPods/Specs.git` named `master`.
You can try adding it manually in `~/.cocoapods/repos` or via `pod repo add`.
```

To fix this, run the following in your terminal:

```bash
cd ~/.cocoapods/repos
git clone https://github.com/CocoaPods/Specs.git master
cd ~/Path/to/your/podfile/
pod install
```

Once that finishes, open the newly-generated Workspace file, and follow these steps:

- Allow insecure (HTTP) network calls (only needed because the OpenWeatherMap API is over HTTP, not HTTPS)
    - See [http://stackoverflow.com/questions/31254725/transport-security-has-blocked-a-cleartext-http]() on how to accomplish this.
- Open the storyboard file, and select the "iPhone 5.5-inch" size from the Simulated Metrics screen in the right-hand navigation bar
- Toss in several labels and a button for the information
- Open the `ViewController.swift` file in the parallel mode and create an outlet for the Label that you created, as well as an action for the button that you created

## Write the Code

Now that the hardest part is out of the way, it's time to write the code that will connect to the OpenWeatherMap API!

You'll need your API key from OpenWeatherMap here, so make sure you went out and got one!

Here's the code that you'll use to connect to the API. Write this in the newly-created action tied to the run button:

```swift
// OpenWeatherMap API Key
        let apiKey = "INSERT YOUR API KEY HERE!"

        // City for Weather Data
        let city = "Provo"

        // Units (F)
        let units = "imperial"

        // Make the GET call for current Weather Data
        Alamofire.request(.GET, "http://api.openweathermap.org/data/2.5/weather", parameters: ["q": city, "APPID": apiKey, "units": units])
            .validate()
            .responseJSON { response in
                switch response.result {

                // Successful Validation
                case .Success(let data):

                    let JSON    = data as! NSDictionary
                    let weather = JSON.objectForKey("weather") as! NSMutableArray
                    let others  = JSON.objectForKey("main") as! NSDictionary

                    let weatherDict = weather[0] as! NSDictionary

                    let main = weatherDict.objectForKey("main") as! String
                    let desc = weatherDict.objectForKey("description") as! String
                    let temp = others.objectForKey("temp") as! Int

                    self.mainLabel.text = main
                    self.descLabel.text = desc
                    self.tempLabel.text = "\(temp) degrees F"

                // Failed Validation
                case .Failure(let error):
                    print("Request failed with error: \(error)")
                }
        }
```

You'll notice that the most convoluted portion of the code is the actual parsing of the JSON. There is another CocoaPod that is very common to use alongside AlamoFire called `SwiftyJSON`, which is used the conversion of a JSON response to an easy-to-traverse object in Swift. You can read more about SwiftyJSON in the further readings.

## Wrapping Up

And that's it! In total, the controller file looks something like this:

```swift
//
//  ViewController.swift
//  AlamoFireTest
//
//  Created by John Turner on 9/5/16.
//  Copyright © 2016 John Turner. All rights reserved.
//

import UIKit
import Alamofire

class ViewController: UIViewController {

    // Outlet
    @IBOutlet weak var mainLabel: UILabel!
    @IBOutlet weak var descLabel: UILabel!
    @IBOutlet weak var tempLabel: UILabel!


    /*
     Connect to OpenWeatherMap API and return information
     */
    @IBAction func connectOpenWeatherMap(sender: AnyObject) {
        // OpenWeatherMap API Key
        let apiKey = "INSERT YOUR API KEY HERE!"

        // City for Weather Data
        let city = "Provo"

        // Units (F)
        let units = "imperial"

        // Make the GET call for current Weather Data
        Alamofire.request(.GET, "http://api.openweathermap.org/data/2.5/weather", parameters: ["q": city, "APPID": apiKey, "units": units])
            .validate()
            .responseJSON { response in
                switch response.result {

                // Successful Validation
                case .Success(let data):

                    let JSON    = data as! NSDictionary
                    let weather = JSON.objectForKey("weather") as! NSMutableArray
                    let others  = JSON.objectForKey("main") as! NSDictionary

                    let weatherDict = weather[0] as! NSDictionary

                    let main = weatherDict.objectForKey("main") as! String
                    let desc = weatherDict.objectForKey("description") as! String
                    let temp = others.objectForKey("temp") as! Int

                    self.mainLabel.text = main
                    self.descLabel.text = desc
                    self.tempLabel.text = "\(temp) degrees F"

                // Failed Validation
                case .Failure(let error):
                    print("Request failed with error: \(error)")
                }
        }
    }
}
```

If you plug that in and run it, you'll have a simple UI that updates given the weather data freely available from OpenWeatherMap.org. Feel free to look more at the docs to see how AlamoFire handles authentication, POST requests, and a whole slew of other features!

## Further Readings

- [Great Tutorial by Ray Wenderlich](https://www.raywenderlich.com/121540/alamofire-tutorial-getting-started)
- [SwiftJSON Main Page](https://github.com/SwiftyJSON/SwiftyJSON)
