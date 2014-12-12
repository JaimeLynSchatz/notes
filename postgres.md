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
