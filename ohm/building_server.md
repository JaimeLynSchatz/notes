Building the Test Server
========================
Don't read the comments, but always read the error messages!

See the Twitter " 'C' language does not exist" error
The postgis sql file has the 'C' error. Can't use ''s, has to be C without quotes because the language is really lowercase c, not C. The processor won't convert to lowercare if it's a string.

Used find and replace in Vim to replace all 500+ occurances.
  :%s/foo/bar/q
  Will replace all occurances of foo with bar, throughout the entire document

Next error was the Permission error. The pgsql user isn't a superuser, so it can't run C scripts.
Log into psql (NOT FROM BASH)
  sudo -u SUPERUSER_USERNAME psql
  
  Then the prompt changes to postgres=#, so you know you're not in ~~Kansas~~ Bash anymore
  type:  create role dba with superuser noinherit;
         grant dba to USERNAME;
  Another clue that you need to be in the psql is the semicolons after the commands!
  
  \q to get out of there, then log back in as the newly pumped up USERNAME
        -u USERNAME psql (??? not ssure here - haven't gotten this far)
        set role dba
        ---- do what you need to do here ----
        reset role
        \q (??? not sure again.)
        
And this is where I left off when I had to stop.
  
  
