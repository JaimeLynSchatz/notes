<br />[Thursday, July 24, 2014] <br />[04:03:00 AM] <jlschatz> .
<br />[Thursday, July 24, 2014] <br />[06:30:13 AM] <muninn-project> Morning
<br />[Thursday, July 24, 2014] <br />[06:30:43 AM] <jlschatz> Good morning
<br />[Thursday, July 24, 2014] <br />[06:42:00 AM]  * jlschatz getting sidetracked thinking about what it would take to build an irc bot that responded to "Good morning" with Gandalf's reply to Bilbo at same. Time for more coffee.
<br />[Thursday, July 24, 2014] <br />[06:51:26 AM] <muninn-project> ahaha
<br />[Thursday, July 24, 2014] <br />[06:51:44 AM] <muninn-project> jlschatz: eggdrop works ok and will do that out of the box.
<br />[Friday, July 25, 2014] <br />[12:16:19 AM] <jlschatz> in positive news, I learned about console.dir (as opposed to console.log) for examining objects in javascript. In less contructive news, I'm in the weeds (again). I will hit it again tomorrow am and will holler if I'm still stuck after more hacking.

<br />[17:03] * jlschatz ashamed, realizing that Jaime doesn't have the right Nick's code (a different contributor named Nick) That explains a lot.
<br />[17:03] <jlschatz> If anyone has a chance, can you pass on a link sometime? I'm on and off tonight, more solidly on tomorrow (except for my commute to a coworking spot.)
<br />[17:06] <muninn-project> ?
<br />[17:07] <muninn-project> jlschatz: You mean the code to the rendered?
<br />[17:07] <jlschatz> Yes.
<br />[17:07] <muninn-project> Roger.
<br />[17:07] <jlschatz> I thought I had it, but I don't.
<br />[17:08] <jlschatz> :/ (Got to learn about what some other Nick did, though, before I discovered my mistake :) )
<br />[17:10] <muninn-project> jlschatz: About to shutdown for the night here.
<br />[17:10] <muninn-project> jlschatz: I can't find a link in my email, but at worst, I'll login to the machine and pull whatever is in production
<br />[17:11] <jlschatz> Do you know his username? I can search that way :)
<br />[17:11] <jlschatz> (and if it's actually just "Nick" i'll go climb in a hole.)

<br />[05:57] <muninn-project> chippy: Was is mikel that hacked together the 2009 layer on ohm?
<br />[06:04] <chippy> originally yeah
<br />[06:04] <chippy> i remade it
<br />[06:07] <chippy> it might not be kept updated like the main one though
<br />[06:35] <muninn-project> chippy: It's just a minute update no?
<br />[06:35] <chippy> the main one is 5 mins
<br />[06:35] <chippy> or 10 or something
<br />[06:35] <muninn-project> Roge.r
<br />[06:36] <muninn-project> Did you do the selection for 2008 at import time or render time?
<br />[06:52] <chippy> render
<br />[06:52] <chippy> code and maybe documentation is online :)
<br />[06:52] <muninn-project> in your github?
<br />[06:52] <chippy> wiki I think.
<br />[06:53] <chippy> ohm github has code which does both the import / conversion into postgis and then the selection when making the maps
<br />[06:55] <chippy> http://wiki.openstreetmap.org/wiki/OHM/Dev 
<br />[07:18] <muninn-project> Roger
<br />[07:29] <muninn-project> jlschatz: Did you catch the above with chippy?
<br />[07:30] <jlschatz> yes, Im bouncing between irc tabs - there's also a opw intern meeting going on in #opw
<br />[07:30] <muninn-project> roger
<br />[07:31] <jlschatz> muninn-project: it looks like it's wrapping up soon. I've got the link to the wiki, did i miss another link (and soooo glad I don't need to get the python renderer working - majob head bashing last night on that)
<br />[07:31] <muninn-project> No python no.
<br />[07:32] <jlschatz> I like python but some of the libraries R requires do not like my computer
<br />[07:33] <muninn-project> I feel the pain, through you can expet some with the renderd setup, 
<br />[07:33] <muninn-project> we will over come.
<br />[07:39] <muninn-project> (dramatic music)
<br />[07:40] <jlschatz> i can deal with some :) (I managed to install Pythong, Ruby, Rails. etc on a windows machine before. I can deal with square pegs and round holes :D)
<br />[07:41] <jlschatz> oh! and I may have just discovered what one of my issues was with the r-alphahull package last night. I'll put it on the queue. (
<br />[07:42] <chippy> jlschatz, are you coming to wikimania btw?
<br />[07:43] <jlschatz> chippy: no, I can't make it across the pond, as it were. :)
<br />[07:44] <jlschatz> I am going to a 10th Year Anniversary meetup for OSM. Organized by Clifford Snow
<br />[07:44] <chippy> okay :)
<br />[07:44] <chippy> ooh, enjoy! I hope to go to the one in London
<br />[07:44] <chippy> I went to the 2nd
<br />[07:46] <jlschatz> chippy: It sounds so awesome. I'll make it out there eventually :D. I'm also potentially going to FOSS4G. (Trying to get all my ducks in order)
<br />[08:18] * muninn-project is trying to justify a 3rd transatalntic trip this fall and cursing himself.

<br />[13:09] <jlschatz> Hi all :). I've been fumbling around with the commands on http://wiki.openstreetmap.org/wiki/OHM/Dev and (finally) got node working properly (had to change the registry to .eu, the CDN at .org is apparently down) I'm poking around in the code of https://github.com/OpenHistoricalMap/ohm_mod_tile/, but I don't *really* know what I'm looking for. I can feel the new synapses forming but I don't know if I'm going down a productive path.
<br />[13:14] <jlschatz> Funny aside: I was searching for carto references in the ohm repo and found lots of SPANISH! (map === *carto*graphia)
<br />[13:21] *** The channel topic is "OpenHistoricalMap - http://OpenHistoricalMap.org mapping the history of the world! ".
<br />[13:21] *** The topic was set by ChanServ!services@services.oftc.net on 06/18/14 04:25 PM.
<br />[13:21] *** Channel modes: no messages from outside, topic protection
<br />[13:21] *** This channel was created on 04/25/14 07:05 AM.
<br />[13:23] <muninn-project> jlschatz_wikimedia_intern: Ok. You're searching for the bit of code that gets the data from the database before rending.
<br />[13:24] <jlschatz_wikimedia_intern> Am I looking in the right place: ohm_mod_tile? Trying to follow along with the info on the wiki but not sure if I'm going down a rabbit hole
<br />[16:24] <muninn-project> jlschatz_wikimedia_intern: documentation fro renderd sucjs
<br />[16:24] <jlschatz_wikimedia_intern> muninn-project: yes, yes it does :)
<br />[16:26] <jlschatz_wikimedia_intern> I'm tracing my way through ohm_mod_tile - I found the bash (?) script that builds up the url (the renderer uses a different url with "combinations" of the x and y coordinates) and so it has to go back and forth between the two formats.
<br />[16:27] <jlschatz_wikimedia_intern> I'm tracing through daemon.c which seems to be running most of the show, but, again, still tracing through.
<br />[16:28] <muninn-project> jlschatz_wikimedia_intern: trying to track down the db connection.
<br />[16:28] <muninn-project> jlschatz_wikimedia_intern: shitth documenttion
<br />[16:29] <jlschatz_wikimedia_intern> If the Sorcerer's book was easy to understand, Mickey wouldn't have gotten into so much trouble with those brooms. Docs sometimes seem to be intentionally cryptic :D.
<br />[16:33] <muninn-project> humm
<br />[16:35] <jlschatz_wikimedia_intern> There's a function in there called send_response that sends an object called item (which I think is the map requested with x and y coordinates) along with a render_time limit
<br />[16:39] <muninn-project>  urses
<br />[16:41] <jlschatz_wikimedia_intern> send_response uses send(), which (don't know if it's the same one) is defined in renderd.py (the comments in that file say it's a port of the renderd.c, but the c version isn't in this repo)
<br />[16:42] <muninn-project> damm them where is code ;)
<br />[16:43] <jlschatz_wikimedia_intern> ???
<br />[16:45] <muninn-project> Damm
<br />[16:45] <muninn-project> I'm cursing how the code is written,
<br />[16:46] <jlschatz_wikimedia_intern> So I take it that this is not a model of well-structured code?
<br />[16:47] <jlschatz_wikimedia_intern> It's like a map written in another language that you can only read by moonlight every 12 years.
<br />[16:47] <muninn-project> jlschatz_wikimedia_intern: You're trying to cheer me up, aren't you?
<br />[16:48] <jlschatz_wikimedia_intern> muninn-project: random SF references are good for everyone! :D
<br />[16:48] <muninn-project> !
<br />[16:49] <muninn-project> jlschatz_wikimedia_intern: http://wiki.openstreetmap.org/wiki/OHM/Dev
<br />[16:50] <muninn-project> jlschatz_wikimedia_intern: mapnik_2009.xml is what need. Of course my ohm password is on the office machine
<br />[16:51] <jlschatz_wikimedia_intern> this is that page that I was trying to follow along with until I got to the point when it asked if I wanted to override the db.
<br />[16:52] <jlschatz_wikimedia_intern> I remember doing some of this (?? I think) many many moons ago (wow, like in the spring) when first setting up. I don't this I did all of this, though.
<br />[16:52] <jlschatz_wikimedia_intern> where do you even enter a password? When setting up the db users?
<br />[16:55] <muninn-project> that is in the 
<br />[16:55] <muninn-project> just a secon
<br />[16:56] <muninn-project> https://github.com/mapnik/mapnik/wiki/PostGIS
<br />[16:57] <muninn-project> https://github.com/mapnik/mapnik/blob/master/plugins/input/postgis/postgis_datasource.cpp#L48
<br />[16:58] <muninn-project> jlschatz_wikimedia_intern:  this going to require a little bit of hacking.
<br />[16:58] <jlschatz_wikimedia_intern> muninn-project: It certainly looks like it
<br />[16:59] <muninn-project> Take a look at line 223?
<br />[16:59] <jlschatz_wikimedia_intern> the bit that talks about changing the extent parameters for custom projections answers a question I had.
<br />[16:59] <jlschatz_wikimedia_intern> looking...
<br />[17:00] <muninn-project> We need to get the url parameters in there 
<br />[17:01] <jlschatz_wikimedia_intern> << "SELECT ST_SRID(\"" << geometryColumn_ << "\") AS srid FROM "
<br />[17:01] <jlschatz_wikimedia_intern>                       << populate_tokens(table_) << " WHERE \"" << geometryColumn_ << "\" IS NOT NULL LIMIT 1;"
<br />[17:01] <jlschatz_wikimedia_intern> I don't know if I'm looking in the right spot?
<br />[17:02] <jlschatz_wikimedia_intern> is our url the geometry_field?
<br />[17:07] <jlschatz_wikimedia_intern> is srid_ the rendered tiles? Trying to follow along here.
<br />[17:08] <jlschatz_wikimedia_intern> oh, it's map jargon. Reading up.
<br />[17:10] <muninn-project> humm
<br />[17:10] <muninn-project> srid is the projection type
<br />[17:12] <jlschatz_wikimedia_intern> https://en.wikipedia.org/wiki/SRID ?
<br />[17:12] <jlschatz_wikimedia_intern> should I get this out of my head?
<br />[17:13] <muninn-project> its set for us so we dont have to worry about it
<br />[17:13] <jlschatz_wikimedia_intern> Ok.
<br />[17:24] <muninn-project> This code is pretty hard core
<br />[17:26] <jlschatz_wikimedia_intern> I'm having trouble telling what language it is - it looks like a mashup of C++ and SQL? (I know not strictly a programming language, but...)
<br />[17:26] <muninn-project> jlschatz_wikimedia_intern: Need to get that config file from the ohm box.
<br />[17:26] <muninn-project> jlschatz_wikimedia_intern: It's C++ with a SQL inline
<br />[17:27] <jlschatz_wikimedia_intern> ok, so I can tell what language it is :) (tiny win)
<br />[17:27] <jlschatz_wikimedia_intern> ? the config file from *which* ohm box? (there are so many repos called ohm_something)
<br />[17:28] <muninn-project> http://wiki.openstreetmap.org/wiki/OHM/Dev
<br />[17:28] <muninn-project> mapnik_2008.xml on the ohm
<br />[17:28] <muninn-project> I suspect there's a config parameters to lock in the year config.
<br />[17:29] <muninn-project> If we can get that it will be a hint of where in the code to find the magic to add to the query.
<br />[17:30] <muninn-project> eseentialy, we need to make the year = xxx in the WHERE clause, but I'd rather re-use as much of the code as possible.
<br />[17:30] <muninn-project> Do you mind if we shut it down for tonight and I'll login to the machine tomorrow first thing?
<br />[17:31] <jlschatz_wikimedia_intern> No problem. :/ Sorry to keep you up with this. 
<br />[17:31] <muninn-project> It's my job. ;)
<br />[17:31] <jlschatz_wikimedia_intern> :D  Well, thank you.