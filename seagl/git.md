***Look up Gitolite***
You can create your own 

sudo su -git
mkdir ~/bin
git clone git://github.com/sitaramc/gitolite
gitolite/install -ln ~/bin
gitolite setup -pk me.pub  /* USERNAME this is where you use your ssh key */

use ssh-keygen if you don't already have it

RTFM! for above

Git Hooks
=========
apply on server or in your .git/hooks directory
lots of things you can program to it to do
automating things on commit and on push

gitolite is written in perl

-e and -u at the top of your bash files is helpful so you'll die and exit if you've got an error in your bash file.
***LOOK THESE UP***

unset GIT_DIR   ---- it's not set up to play nicely when you're going git stuff when using hooks (but not actually in a hook.) ***Look this up, too***

Look up the sample hooks in git/contrib

Look up sudo NOPASSWD - can be specific commands that you allow without a password

http://www.ifokr.org/bri/presentations/lfnw-2014-ssh/ for more samples and information

Questions from group
====================

use vrefs for code review??
 
