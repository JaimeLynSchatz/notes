Postgres Password Madness
=========================

Find the pg_hba.conf file somewhere in here:
/etc/postgresql/8.4/main/pg_hba.conf
/etc/postgresql/9.1/main/pg_hba.conf

How to change “postgres” user’s password (Postgresql 9.3) on Ubuntu 14.04
Posted on June 17, 2014 by Naved
1. In pg_hba.conf, insert or change the below line.
from :

local all postgres

to

local all postgres trust

2. Restart PostgreSQL services in order for Step 1 changes to take effect :

/etc/init.d/postgresql restart

3. Login to PostgreSQL on the local machine with the user name "postgres" to change the password :

psql -U postgres

4. At the "postgres=#" prompt, change the user name "postgres" password :

ALTER USER postgres with password ‘new-password';

5. Quit PostgreSQL interactive session by executing "\q", to exit

6. Alter the configuration (what we did in Step 1) to disable password-less login from local machine to PostgreSQL by changing the word "trust" to "md5" in pg_hba.conf.
from:

local all postgres trust

to:

local all postgres md5

7. Restart PostgreSQL to make Step 6 changes take effect by repeating Step 2.

8. Update .pgpass with your new password if you are using one

/home/&lt;user&gt;/.pgpass

9. Re-login to PostgreSQL using the new password by :

psql -U postgres

Dropping Databases
==================

You can run the dropdb command from the command line.

dropdb 'database name'
Note that you have to be a superuser or the database owner to be able to drop it.

You can also check the pg_stat_activity view to see what type of activity is currently taking place against your database, including all idle processes.

SELECT * FROM pg_stat_activity WHERE datname='database name';
edited Aug 16 '11 at 5:16 | answered Aug 16 '11 at 5:11
I'm using dropuser command to remove also the user. –  pl1nk Sep 5 '12 at 15:26 

This will restart postgres and disconnect everyone: sudo service postgresql restart Then do a: dropdb -h localhost -p 5432 -U "youruser" "testdb" Notice the "" to make sure special characters go in without a hitch. –  unmircea Jun 26 at 6:10 

Making Postgres Find C
======================
You are probably running into this change in PostgreSQL 9.2 (quoting the release notes here):

No longer forcibly lowercase procedural language names in CREATE FUNCTION (Robert Haas)

While unquoted language identifiers are still lowercased, strings and quoted identifiers are no longer forcibly down-cased. Thus for example CREATE FUNCTION ... LANGUAGE 'C' will no longer work; it must be spelled 'c', or better omit the quotes.

It's also reflected in the manual for CREATE FUNCTION

lang_name

The name of the language that the function is implemented in. Can be SQL, C, internal, or the name of a user-defined procedural language. For backward compatibility, the name can be enclosed by single quotes.

Quoting the language name has been discouraged since at least version 7.3 (maybe longer), but old habbits die hard, obviously.

You would need to remove the quotes around C arriving at: LANGUAGE c.

Seems like Joe Conway didn't get the message and PL/R (therefore) isn't ready for PostgreSQL 9.2, judging from the project page.

Feedback from Joe Conway

Joe Conway left an answer that got deleted because it should be a comment. I paste it here for the general public who can't see deleted answers:

I got the message, just haven't had the time to do a new PL/R release. Look for it by December, but in the meantime the manual workaround noted above is pretty simple.
