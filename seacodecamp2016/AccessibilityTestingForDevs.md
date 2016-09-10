#Accessibility Testing for Developers

http://www.slideshare.net/gerardkcohen/accessibility-testing-tools-for-developers-gerard-k-cohen-csun-2016
Check out his PluralSight course

gerardkcohen@gmail.com
@gerardkcohen

##Test Early, Test Often

FE devs as the last hope to ensure work and products are inclusive to everybody

Ted Brake (Drake - accessibility control test)

## Basic Test # 1
This is the bare minimum
###https://validator.w3.org/nu

Browsers had to be built to be forgiving to keep the internet working - readers, not so much
Assitistive technology needs the proper sturcture and no broken tags, etc.

###http://chrispederick.com/work/web-developer/
Web Developer Tools
Toolbar plugin

###Local Validator https://github.com/validator/validator - when youc an't send code behind  a firewall

## Basic Test # 2
Use the tab key to tab through your site. What happens?
- focus needs to be visible
- focus needs to be in a natural order -- matching the visual order, logical order of the page
- no keyboard traps
- no focus on hidden elements
- then try shit tab from the bottom up

If focus is lost, try :focus { border: 1px solid red; } when testing -- you can always see where focus is

Check the DOM order first - floating can mess with the visual vs. DOM order
Check for abs position or off-canvas
CSS animations to animate heights - the item is still there, even though it's not visible
tab index values - specifies the tab order

never have a tabindex greater than 0 -- it's either -1 or 0
Controls are natrually focusable
tabindex 0 will make another kind of widget tabbable in the natural order
a tabindex of -1 will drop it out until you use a script to make it tababble

Greater than 0 will do strange things with the browser

###CSS Bookmarklets
http://imbrianj.github.io/debugCSS

http://www.karlgroves.com/2013/09/07/diagnostic-css-super-quick-web-accessibility-testing/

https://github.com/Heydon/REVENGE.CSS

###Writing Custom Rules in Your CSS
the test for aria labels in CSS

###JS Bookmarklets
http://khan.github.io/tota11ly

Links that say "read more" or "click here" are useless -- the link text needs to include what you're linking to (not URL, but something like "link to work item ##X details" or something similar)

Chris Matthews - vxl something that made words better (homonyms are tricky, so are things like dashes and subtraction symbols)

All caps are read letter by letter

http://squizlabs.github.io/HTML_CodeSniffer

If you disable CSS styling and the page still makes sense, then you're looking pretty good on logical flow

Presentational images without any meaning can have an empty alt attribute (like a lovely graphic that's just there for looks)

###Accessiblity Developer Tools in Chrome Plugin

###Color Contrast
You want to meet a ratio of 4.5:1

###Advanced Testing - Automating These Tools
NightWatch
- a front end for Selenium
Tool is tricky - it's got poor documentation, but it's an experiment
NightWatch is tough to use, but supports many browsers

