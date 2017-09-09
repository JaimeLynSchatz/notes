#Ui Test Automation
_@slobo80_
[https://devatheart.com](Blog at devatheart.com)
Check this out -- the code has comments and tips and ideas.

_look up Codestock_

First Monday of the Month - .NET Dev Associattion

November 6th: Removing Chaos and Noise from the Dev Stack 
[http://dotnetda.org](.NET Developers Association)

UI Tests
Integration Tests
Unit Tests

Server side tests tend to be more predictable

SPAs are much trickier

_You can write thetests to pass, doesn't mean it's the right way to write the test_

Selenium -- USE IT

##Fragile
##Hard to Maintain
##Slow to Execute

###Test - Driver - Browser
*IEDriverServer.exe
*SafariDriver
*Firefox has built-in driver
*Chrome Webdriver

Chrome tests can be run HEADLESS after *version* 59.

*If you terminate or cancel the test before it automates, the driver will continue running in the task manager. Pay attention to your task manager so you don't leave the drivers running.*

Create new test project in Visual Studio
Nuget pagackes: selenium webdriver, selenium subbort, selenium chrom ewebdriver

Run with options.AddArgument("--headless")

###Important to clean up
TestCleanup()
driver.Quit()
driver.Dispose()

Don't be afraid to read the Selenium source code - you can see what the test is really looking for. You can pull in the pageSource of the page through the tests, all kinds of things.

*Take screenshots on failing tests so you can see what Selenium saw.*

_BrowserStack -- set up the test matrix for your testing_
*You can set up different viewports to test different views
*Different browsers, different versions, etc

_or_ you can do that kind of testing manually

Problems:
*Strongly tied to the html of the page
*If items are loaded differently (spa) the tests will fail

###Fix # 1
Repair the tight coupling - break the dependency
The html does not belong in th test

**PageObject Pattern**
IWebElement serarches by the kind of element (query type, css ,etc)

**ID is the preferrable way to look at an element**
_avoid css classnames!_

public By BySearchBox => By.Name("q");

###Fix # 2
_Stay higher level and more abstracted so that Selenium updates their heuristics and you won't have to._
If you want to ge that close to the metal, go work on the Selenium project! :D

Use 
var wait = new WebDriverWait(driver, Timespan.FromSeconds(20));   ---> defining the timeout condition
wait.Until(ExpectedConditions.ElementIsVisbile(page.BySearchBox));  ----> _the test will fail if the item isn't available after 20 seconds_
ElementExists
ElementIsVisible --> Selenium has a heuristic for this that they update as browsers evolve
ElementIsClickable --> this is a nice one

###Fix # X
A better way to go is the user Actions
_be sure to wrap the Action is Waits_

var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(20));

new Actions(driver
	.MOveToElement(page.SearchBox)
	.SendKeys("Seattle Code Camp")
	.SendKeys(Keys.Enter)
	.Perform();   ---> make sure you actually perform the test!!

_Need a wait here_
wait.Until(ExpectedConditions.ElementIsVisible(page.ByFristSearchResult));

__NEVER CATCH OR EXPECT AN EXCEPTION YOU ARE NOT THROWING__
The test will pass, but it clearly didn't work as expected

var manyElements = driver.FindElements(By.Id("missingElementId"));
Assert.AreEqual(0, manyElements.Count);
_this will work, __however__ it will be very, very slow because it has to traverse the entire DOM_
Try to find another way to search for missing elements, though

###One More Thing
_WARNING:_ wait.Until(p=>ExpectedConditions.ElementIsVisisble(page.ByFirstSearchResult));
this delegate will never be executed.
We're passing a delegate as a delegate -- it will never be executed.

