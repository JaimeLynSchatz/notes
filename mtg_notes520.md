###ETC Office Hours Meeting on Wikimedia

[09:12] --> You have joined the channel #wikimedia-office (~jlschatz@184.11.141.106).
[09:12] *** The channel topic is "Engineering Community team IRC meeting. : #wikimedia-office Channel is logged and publicly posted (DO NOT REMOVE THIS NOTE) | https://meta.wikimedia.org/wiki/IRC_office_hours".
[09:12] *** The topic was set by qgil!~qgil@192.195.83.38 on 05/20/14 09:00 AM.
[09:12] *** Channel modes: no colors allowed, no messages from outside
[09:12] *** This channel was created on 09/04/09 11:22 AM.
[09:12] *** Channel URL: http://meta.wikimedia.org/wiki/IRC_office_hours
[09:12] <tonythomas> rillke: specially if you are in India - mosh is great !
[09:12] <fhocutt> I'm glad to have 2 people assisting mentors so we can cover more languages (esp ones I'm not familiar with yet)
[09:12] <kondi> Spent most of the time documenting the requirements and reading. Apart from daily chats, I had a meeting with my mentor. afk.
[09:12] <mutante> no wonder, since toolserver hardware is in Amsterdam
[09:12] <Raylton> qgil, i know ^^
[09:12] <discoveranjali> I am in good pace with my work since the start of May ..... planned to few outreach ideas along with my mentor and shall soon be finalizing and publishing them !
[09:12] <Raylton> qgil, thanks
[09:12] <-- bawolff has left this server (Ping timeout: 255 seconds).
[09:13] *** You are now known as jlschatz.
[09:13] <rohit-dua> qgil, reports should be submitted weekly or monthly?
[09:13] <tonythomas> mutante:  It used to be almost 1 sec delay between keystrokes :\
[09:13] --> ElenaDanielle has joined this channel (~ElenaDani@192.195.83.38).
[09:13] <qgil> rohit-dua, we will talk about reports as soon as we are done with the community bonding discussion
[09:13] <-- jlschatz_intern has left this server (Quit: Bye).
[09:13] <ali_king_intern> currently preparing a presentation for SMWCon on Thursday - also a great opportunity to talk to useful people
[09:14] <qgil> fyi, Micru is referring to this reply, which is relevant to GSoC/OPW: http://lists.wikimedia.org/pipermail/wikimedia-l/2014-May/071856.html
[09:14] --> tgr has joined this channel (~gtisza@wikipedia/tgr).
[09:14] <aaron_xiao> pretty good for the bonding time. we discuss in mailing list wikizh-l, not only the mentor, but also other guys
[09:15] <Micru> qgil, do you think it is convenient for all GsoC projects to use Phabricator?
[09:15] <qgil> Micru, letś talk about this after the reports.  :)
[09:15] <qgil> The first report is about the community bonding period.
[09:15] <Micru> ok, ok, qgil :)
[09:15] <qgil> You have all learned something, you have made first decisions as a team, you have found some expected and unexpected obstacles...
[09:16] <qgil> Please reflect the most important aspects in a short report. This will give you some practice reportin.  :)
[09:16] <qgil> Any questions about this first report?
[09:16] <sandaru_> what would be the approximate word count of this?
[09:16] <qgil> Copying from https://www.mediawiki.org/wiki/Google_Summer_of_Code_2014#Status :
[09:16] <qgil> community bonding report including links to
[09:16] <qgil> minimum viable product and goals
[09:16] <qgil> communication plan
[09:16] <qgil> lessons learned since 21 April
[09:17] <fhocutt> where should we post them?
[09:17] <qgil> sandaru_, reports are as short as possible, providing important details and links
[09:17] <discoveranjali> Any preferred format to be followed for the report ?
[09:17] --> cndiv has joined this channel (~cndiv@wikimedia/cdeubner).
[09:17] --> mindspillage has joined this channel (~kat@wikimedia/KatWalsh/x-0001).
[09:17] <qgil> Every time you write your report you have to think hat there are 22 more interns doing the same, and this is only two programs among the many we have around
[09:18] <muninn-project> roger
[09:18] <qgil> Also in the wiki we are identifying good practices (well, just one so far, but mentors and other vets are welcome to add more examples)
[09:18] <qgil> The example provided: https://www.mediawiki.org/wiki/User:Mariapacana/OPW_Progress_Report
[09:18] <sandaru_> Thanks qgil
[09:18] <mvolz> Ok so FOSS OPW interns should follow the same format as GSoc i.e. weekly reports?
[09:18] <qgil> Create a subpage under your project wiki page and start reporting there, creating new sections for new reports
[09:19] --> Joel___ has joined this channel (c0c547bd@gateway/web/freenode/ip.192.197.71.189).
[09:19] <tonythomas> qgil: ok
[09:19] <-- HaithamS has left this server (Remote host closed the connection).
[09:19] <qgil> We have seen all kinds of frequency used, from monthly to daily. It is a good idea to default to weekly reports.
[09:19] <-- Raylton has left this server (Ping timeout: 255 seconds).
[09:19] --> matanya2 has joined this channel (~yaaic@37.26.147.246).
[09:19] <qgil> mvolz, https://www.mediawiki.org/wiki/FOSS_Outreach_Program_for_Women/Round_8#Status contains exactly the same text, transcluded
[09:20] <qgil> We want to align GSoC and OPW processes and standards as much as possible
[09:20] --> Raylton has joined this channel (~Raylton@wikibooks/Raylton-P-Sousa).
[09:20] --> terrrydactyl has joined this channel (~terrrydac@c-50-150-83-44.hsd1.ca.comcast.net).
[09:20] --> jmehta has joined this channel (~chatzilla@182.68.193.45).
[09:20] <qgil> Why weekly? Because you can miss one week and itś not a big problem, but if you miss a second report it has been "only "14 days missing.
[09:21] <qgil> Previously we were defaulting to monthly reports, but then we found about serious problems really late (for a project that is supposed to last about 3 months only)
[09:21] <qgil> More questions about reporting? More opinions from mentors, ECT colleagues...?
[09:21] <ali_king_intern> how should this relate to the (minimum) fortnightly blog posts, if at all?
[09:21] <guillom> I think twice a month is a good rhythm, more is welcome
[09:21] <matanya2> e.g watch list grouping project
[09:22] <Raylton> qgil. I think wikimedia should require reports "every few days"
[09:22] <-- cndiv has left this server (Ping timeout: 240 seconds).
[09:22] <jlschatz> matanya2: what's a watch list grouping project?
[09:22] <Raylton> i do that with deepali and molly... good results
[09:23] <matanya2> previous gsoc project that died
[09:23] <qgil> ali_king_intern, OPW have this requirement for fortnightly blog posts. At least from the Wikimedia point of view, you could paste your two weekly reports preceded by an intro, and be good.
[09:23] <jlschatz> matanya2: thanks
[09:23] <sumanah> Raylton: can you point to a sample report? am I right in inferring that each one was maybe a paragraph long?
[09:23] <qgil> guillom, Raylton "Wikimedia" is suggesting weekly, but every team can decide the way of woerking that fits best for them.
[09:24] <guillom> sounds good to me :)
[09:24] --> HaithamS has joined this channel (~HaithamS@199-117-24-190.dia.static.qwest.net).
[09:24] <qgil> We only want a simple communication plan agreed with the mentors, no sttress, and no ugly surprises.  :)
[09:24] <Raylton> sumanah, https://meta.wikimedia.org/wiki/Book_management_2013/Progress#Weekly_reports
[09:24] --> apsdehal has joined this channel (uid26473@gateway/web/irccloud.com/x-qcrxaylhplvakfwx).
[09:25] <qgil> Raylton, sumanah, other,  you are encouraged to link to more god examples of reports next to the example of Maria Pacana at the GSoC page.
[09:25] <qgil> Anything else about reporting? Have I missed any questions?
[09:25] <jlschatz> qgil: I have an OT Q re: ugly surprises, will there be time later?
[09:26] <matanya2> gnome gsoc reports are good
[09:26] --> Jurgen has joined this channel (~chatzilla@wikimedia/JurgenNL).
[09:26] --> jdlrobson has joined this channel (~jdlrobson@5ec2c39c.skybroadband.com).
[09:26] <Raylton> qgil, yes... I have problems with google-melange
[09:26] <apsdehal> Hi everyone, where can we host our server side scripts, wikimedia labs?
[09:26] <qgil> jlschatz, the ugliest surprise (imho) is when everybody thinks that an intern is doing ok, just having some temporary difficulties, until you realize that the project has been stalled and about to fail
[09:27] <qgil> all because having too much patience with silence, or with misc arguments avoiding some core problem
[09:27] <Raylton> qgil, I sent an email to you but got no answer
[09:27] <rillke> apsdehal, gerrit or github ?
[09:27] <qgil> Regular reporting is not the solution for this problem, but at least helps detecting the symptoms earlier and better.
[09:27] <rillke> (gerrit-wm)
[09:27] <apsdehal> No I want to run, actually I have to create an api for wikimedia login
[09:27] <jlschatz> qgil: yes, that would be bad :). Very frequent reporting sounds really helpful for that. My Q was about the "if funding comes in" portion of our OPW contracts.
[09:28] <qgil> Raylton, the one about you not being officially a mentor? In my ToDo list, no worries.
[09:28] <matanya2> apsdehal: yes
[09:28] <apsdehal> To which I can redirect my client side app towards that api for login
[09:28] <rohit-dua> what about phabricator. shall it be used for all projects?
[09:29] <qgil> jlschatz, I'm not sure I understand the link between ugly surprises and funding. Can you explain, please?
[09:29] <mvolz> jlschatz:
[09:29] <mvolz> whoops.
[09:29] --> TBloemink has joined this channel (~TB@wikimedia/tbloemink).
[09:29] <apsdehal> Actually software I am building upon already has openid login
[09:29] <-- Joel___ has left this server (Quit: Page closed).
[09:29] <apsdehal> But wikimedia doesn't supports it
[09:29] <qgil> apsdehal, can you leave discussions about your project for later, please?
[09:29] <mvolz> jlschatz: are you referring to gnomes issues with cash flow problems for the last round?
[09:29] <jlschatz> qgil: the contract says that if funding falls through, interns won't receive payments even if they're successful in their projects
[09:30] <apsdehal> qgil: Yes, sorry for that
[09:30] <andre__> apsdehal: spontaneously I'd say: Wikimedia Labs.
[09:30] <Raylton> qgil, thanks. please answer  before the midterm.
[09:30] <jlschatz> mvolz: i think the change in the contract language was a result of their cash flow issue (i read about it online, didn't hear from Gnome specifically on it)
[09:30] <qgil> jlschatz, Wikimedia pays its bills as much as Google.  :)  You shouldn't worry about funding.
[09:30] <jlschatz> qgil: :) thanks
[09:31] <-- csteipp has left this server (Quit: Ex-Chat).
[09:31] <qgil> Ok, anything else about reporting before moving to the question about Phabricator?
[09:31] <thepwnco> yes - when should community reports be submitted? My guess is as soon as possible...
[09:32] <rillke> a deadline is always welcome
[09:32] --> apexkid1 has joined this channel (~adi@14.139.236.210).
[09:33] <tonythomas> rillke: you just need to update it as soon as you complete a milestone right ? why deadlines ?
[09:33] *** kaity|away is now known as kaity.
[09:33] <-- matanya2 has left this server (Ping timeout: 276 seconds).
[09:33] <qgil> thepwnco, the community bonding report can be submitted... soon.  Let's say this week, since  you are required to submit your first actual report about the project by 30 May.
[09:33] --> DarTar has joined this channel (~DarTar@wikimedia/DarTar).
[09:33] <fhocutt> tonythomas, deadlines help some of us focus
[09:33] --> subbu has joined this channel (~subbu@75-168-184-186.mpls.qwest.net).
[09:34] <Raylton> qgil, a blog post is ok for that?
[09:34] <qgil> We have just a few dates defined during the program, some of them set by the program organizers aka Google & GNOME. They are useful as sync points.
[09:34] <tonythomas> qgil:  submitting == updating your report wiki page right ?
[09:34] <qgil> Raylton, for what?
[09:35] <qgil> tonythomas, yes.
[09:35] <tonythomas> qgil: cool then
[09:35] <Raylton> qgil,  community bonding report
[09:35] <qgil> We recommend you to submit brief reports in a wiki subpage (see the example above). If you want to write blog post, send updates to mailing lists, etc, you can also do it.
[09:35] <rillke> should we touch https://www.mediawiki.org/wiki/Google_Summer_of_Code_2014 again or leave it as it is ?
[09:36] <rillke> - for listing reports etc.
[09:36] --> PPena has joined this channel (~PPena@216.38.130.164).
[09:36] <qgil> rillke, it is useful to keep your row in that table up to date. It gives a good view of the status of the whole program.
[09:36] <qgil> rillke, no need to list every weekly report, but main milestones.
[09:36] <qgil> e.g. mid-term evaluations
[09:37] <qgil> Reporting ok?  :)
[09:37] <rohit-dua> :)
[09:38] <qgil> (I will try to capture the usual questions and document the answers in the GSoC / OPW wiki pages.
[09:38] <qgil> The question about Phabricator
[09:38] <qgil> The bottom line here is that you need to define the way you want to work.
[09:39] <qgil> The wiki project page is a must, it needs to be updated reflecting always the current plan + the subpage with reporting.
[09:39] <-- HaithamS has left this server (Remote host closed the connection).
[09:39] --> JoelS has joined this channel (c0c547bd@gateway/web/freenode/ip.192.197.71.189).
[09:39] <qgil> Then, about the tasks, we have been using Bugzilla as a way to define tasks, blockers, etc, for coding projects.
[09:40] <-- aaron_xiao has left this server (Quit: 暂离).
[09:40] <andre__> Is it broadly known here what "Phabricator" is, when it comes to our infrastructure? (I wonder if I missed an email I'm not aware of)
[09:40] <andre__> (In short: It will replace Bugzilla at some point.)
[09:40] <qgil> Most of your projects have a central report in Bugzilla, so it is easy to create blockers for specific tasks, bugs, etc.
[09:40] --> HaithamS has joined this channel (~HaithamS@199-117-24-190.dia.static.qwest.net).
[09:40] <qgil> andre__, I'm getting there.  :)
[09:41] <qgil> And then most of your projects also have a related code repository, by default in Gerrit.
[09:41] <qgil> We are just in the middle of a transition to go from these various tools to Phabricator (keeping MediaWiki for documentation)
[09:41] <qgil> https://www.mediawiki.org/wiki/Phabricator
[09:42] <-- HaithamS has left this server (Remote host closed the connection).
[09:42] <qgil> In this context, you may want to consider the possibility of using/testing Phabricator for your project.
[09:42] --> HaithamS has joined this channel (~HaithamS@199-117-24-190.dia.static.qwest.net).
[09:42] <qgil> ... which is the advice I gave to Micru earlier today at http://lists.wikimedia.org/pipermail/wikimedia-l/2014-May/071856.html
[09:43] <qgil> Phabricator is useful to organize tasks, and you could use our instance at http://fab.wmflabs.org/ already now
[09:43] *** kaity is now known as kaity|away.
[09:43] <muninn-project> ok
[09:43] <rillke> And it reliably works :)
[09:43] <qgil> For instance, this is what rillke is doing at http://fab.wmflabs.org/project/view/26/
[09:44] <qgil> For code review... it might be premature, although it depends on how brave and how much are you willing to be an alphatester.
[09:44] <qgil> So you don't have to use Phabricator, and the default keeps being Bugzilla, but if you want to try and help testing/learning about this tool, you are welcome.
[09:44] <-- HaithamS has left this server (Remote host closed the connection).
[09:45] <qgil> Is it clear?
[09:45] --> HaithamS has joined this channel (~HaithamS@199-117-24-190.dia.static.qwest.net).
[09:45] <Raylton> qgil i need to leave. i'll see the logs and ask some question by email. ok?
[09:45] <qgil> ok Raylton
[09:45] <Raylton> thanks
[09:46] *** Raylton is now known as Raylton_away.
[09:46] <rohit-dua> qgil, where should i host server side scripts(like python-bot scripts)?
[09:46] *** InezK is now known as InezK_away.
[09:46] --> matanya2 has joined this channel (~yaaic@5.28.148.173).
[09:46] <qgil> rohit-dua, your mentors should know, but I guess the answer is Wikimedia Labs
[09:46] <-- HaithamS has left this server (Remote host closed the connection).
[09:46] <andre__> rohit-dua: would Wikimedia Labs work for this?
[09:47] <qgil> https://www.mediawiki.org/wiki/Wikimedia_Labs
[09:47] <rohit-dua> sndre__, yes. i meant where should i publish the code for the bot for review process
[09:48] <matanya2> gerrit
[09:48] <qgil> rohit-dua, please agree this with your mentors
[09:48] <rohit-dua> qgil, ok :)
[09:48] <qgil> Gerrit is the default option, yes.
[09:48] <sumanah> qgil: let me make sure: https://www.mediawiki.org/wiki/Google_Summer_of_Code_2014#Status "community bonding report including links to: * minimum viable product and goals * communication plan * lessons learned since 21 April" -- can you please explain what you mean by "minimum viable product"? Because I think you are saying "DESCRIPTION of what the mentee WILL achieve, at minimum, within the next 3 months"
[09:48] <qgil> More questions?
[09:49] <qgil> About minimum viable product
[09:49] <jlschatz> +1 for sumanah's Q
[09:49] <qgil> 1 min... searching
[09:49] <-- AnnaKoval has left this server (Ping timeout: 252 seconds).
[09:49] <sumanah> honestly I think we should either remove that jargon entirely and leave "goal" (which everyone understands) or explain better.
[09:50] <qgil> See https://www.mediawiki.org/wiki/Mentorship_programs/Selection_process
[09:50] <fhocutt> also for sumanah's question, if that's for the entire project is there not a section for "things achieved since 21 April"?
[09:50] <mvolz> I find the MVP concept very useful although it's true that everyone might not understand it.
[09:50] <fhocutt> or is that just "lessons learned"?
[09:50] <qgil> "A good team must work on a good plan. A good plan is expected to define a minimum viable product (the content of your first testable release) and build the rest of features on top of it."
[09:50] <sumanah> in most cases, the goals/mvp description that would belong that initial "community bonding report" is what the mentee wrote up in their Deliverables section of their initial proposal, I think
[09:51] <sumanah> qgil: that's still unclear and confusing, because that sentence you just quoted conflates the planning and the building.
[09:51] <wctaiwan> ^ that's what I thought as well. I'd pretty much just be saying "see [[section]] in proposal"
[09:51] <fhocutt> mvolz: it's also less relevant to projects like mine that focus on standards and documentation
[09:51] <qgil> sumanah, yes yes, letś clarify. Still searching references.http://en.wikipedia.org/wiki/Minimum_viable_product
[09:51] --> HaithamS has joined this channel (~HaithamS@199-117-24-190.dia.static.qwest.net).
[09:51] <mvolz> That's true; although my project has changed pretty substantially since then.
[09:51] <mvolz> fhocutt: good point
[09:51] <qgil> The problem we want to solve is:
[09:51] <qgil> projects that at the end of the program cannot deliver a single thing
[09:52] <fhocutt> I understand the terminology, I'm just not going to have a testable release
[09:52] <qgil> because they aimed to do everything but finished nothing
[09:52] <sumanah> Right
[09:52] <qgil> this is why already during the selection process we have encouraged students and mentors to define a minimum viable product, a first minimal release to build upon
[09:52] <sumanah> again, qgil, when you say "to build upon" it
[09:53] <sumanah> it gets confusing
[09:53] <mvolz> is there a sample community bonding report?
[09:53] <mvolz> this is new to this round, correct?
[09:53] <qgil> Even in the case of documentation you may want to define a focus in one areas as opposed to try to push all "chapters"at once
[09:53] <sumanah> yes
[09:53] <-- HaithamS has left this server (Remote host closed the connection).
[09:53] <sumanah> which my mentee has already done, as she worked out the list of deliverables she would be delivering
[09:53] <qgil> sumanah, "release soon, release often"
[09:54] <sumanah> qgil: yes. I am objecting to your wording as confusing.
[09:54] <qgil> get something out that someone else can look at (a minimum viable product, a prototype...) and then continue improving it
[09:54] <fhocutt> this makes sense as a concept but I still don't know what I'm supposed to put in the report.
[09:55] <sumanah> fhocutt: My advice: just copy your list of deliverables (a.k.a. goals) that you aim to achieve by the end of the summer.
[09:55] <wctaiwan> do we need to repeat what our minimum viable product is if we've already defined it in our proposal?
[09:55] <qgil> please propose a better wording
[09:55] <-- Niharika has left this server (Ping timeout: 265 seconds).
[09:55] <qgil> sumanah, I still think it is useful to define your first "publication", that should come before the mid-term evaluation
[09:55] <sumanah> fhocutt: If we find that you have time and ability, then you'll be able to do more stuff beyond that -- file more bugs, polish more documents, and so on.
[09:55] <qgil> your initial focus
[09:56] <-- jmehta has left this server (Ping timeout: 276 seconds).
[09:56] <-- DarTar has left this server (Quit: DarTar).
[09:56] <sumanah> ok, then, fhocutt, copy the list of the things you'll be achieving in the first 6 weeks. you have your deliverables set up by week already so that should be fairly straightforward
[09:56] --> Niharika has joined this channel (~Happiness@122.161.148.245).
[09:56] <qgil> Looking at previosu projects, those that didn't have anything to show before the mid-term struggled during the second half.
[09:56] <fhocutt> thanks, sumanah, will do
[09:56] <sumanah> cool
[09:56] <siebrand> Have to go. Thanks for this meeting, qgil. Very useful IMO.
[09:57] <-- atgomez has left this server (Ping timeout: 252 seconds).
[09:57] <qgil> wctaiwan, you don't need to details you plans in the community bonding report, just link to the relevant places.
[09:57] <wctaiwan> okay, thanks.
[09:57] <qgil> siebrand, thanks!
[09:57] <thepwnco> also have to run. Thanks for this. Happy interning all!
[09:57] --> HaithamS has joined this channel (~HaithamS@199-117-24-190.dia.static.qwest.net).
[09:58] <qgil> sumanah, I will try to clarify the wording. Nobody had complained until now.  :)
[09:58] <qgil> 2 minutes
[09:58] <sumanah> I changed https://www.mediawiki.org/wiki/Google_Summer_of_Code_2014#Status to ask for "goals for the first half of the internship"
[09:58] <-- thepwnco has left this channel.
[09:58] <qgil> sumanah, good.
[09:59] --> DarTar has joined this channel (~DarTar@wikimedia/DarTar).
[09:59] *** roblaAWAY is now known as robla.
[09:59] <-- ali_king_intern has left this server (Ping timeout: 240 seconds).
[09:59] <qgil> Ok, it looks that this is it. Thank you everybody!
[09:59] <qgil> If you have more questions, you can find us at wikitech-l and the usual places.
[09:59] <andrewbogott> thanks qgil
[10:00] <rohit-dua> thank you qgil
[10:00] <fhocutt> thanks qgil, sumanah
[10:00] *** robla is now known as roblaAWAY.
[10:00] <-- Yaron has left this channel.
[10:00] <arrbee> Nice meeting qgil . Thanks :)
[10:00] <discoveranjali> Thank you for this informative discussion qgil ! :)
[10:00] <sandaru_> thanks qgil
[10:00] <-- andrewbogott has left this channel.
[10:00] <rillke> thanks everyone
[10:00] <jlschatz> Thanks, qgil!
[10:00] <-- rillke has left this server (Quit: "Bye").
[10:01] <-- sandaru_ has left this server (Quit: Page closed).
[10:01] <jlschatz> ^^ and everyone! sumanah, too - you read my mind!
[10:01] <sumanah> :)
[10:01] <mvolz> bye!
[10:01] <-- fhocutt has left this channel ("Leaving").
[10:01] <-- kunalg has left this channel ("http://quassel-irc.org - Chat comfortably. Anywhere.").
[10:01] --> kunalg has joined this channel (~quassel@103.247.99.203).
[10:01] * tonythomas waves bye-bye
[10:01] *** TBloemink is now known as TB|Auto.
[10:02] <-- sumanah has left this channel ("Leaving").
[10:02] <-- rohit-dua has left this server (Quit: Leaving).
[10:02] *** awjr_away is now known as awjr.
[10:02] <-- wctaiwan has left this channel ("Leaving").
[10:02] <apsdehal> Thanks qgil
[10:02] --> rohit-dua has joined this channel (~8ohit.dua@122.161.184.67).
[10:03] <-- rohit-dua has left this channel.
[10:03] *** roblaAWAY is now known as robla.
[10:03] *** robla is now known as roblaAWAY.
[10:03] *** roblaAWAY is now known as robla.
[10:03] <-- DarTar has left this server (Client Quit).
[10:03] *** qgil sets the channel topic to "Channel is logged and publicly posted (DO NOT REMOVE THIS NOTE) | https://meta.wikimedia.org/wiki/IRC_office_hours".
[10:04] *** qgil sets the channel topic to "Channel is logged and publicly posted (DO NOT REMOVE THIS NOTE) | https://meta.wikimedia.org/wiki/IRC_office_hours".
[10:04] <qgil> Hm.
[10:04] *** robla is now known as roblaAWAY.
[10:05] *** roblaAWAY is now known as robla.
[10:05] --> DarTar has joined this channel (~DarTar@wikimedia/DarTar).
[10:07] <-- siebrand has left this channel.
[10:07] *** bd808 is now known as bd808|AWAY.
[10:07] <-- Keegan has left this server (Ping timeout: 264 seconds).
[10:07] *** InezK_away is now known as InezK.
[10:08] --> atgomez has joined this channel (~textual@c-71-202-86-99.hsd1.ca.comcast.net).
[10:09] <guillom> qgil: andre__: BTW, our current and past projects are now listed automatically in our navigation template (courtesy of a few improvements to my Lua module): https://www.mediawiki.org/wiki/Template:Engineering_Community_Team

###Back channel chat with muninn
[09:14] <jlschatz> had another client open. (eyeroll, smh, all that) swapped :)
[09:14] <muninn-project> roger.
[09:15] <muninn-project> will get your access to the machine today.
[09:15] <muninn-project> let's talk after this meeting.
[09:15] <jlschatz> You got it!
[09:15] <muninn-project> Are you squred wrt payment from the foundation?
[09:15] <muninn-project> now is the time to ask
[09:15] <jlschatz> The contract says it will come in about a month and a half if the funding goes through. 
[09:16] <jlschatz> That *if* has me nervous. It's a new contract this round.
[09:16] <muninn-project> Ask in the channel.
[09:28] <muninn-project> He mis-understood you, better ask again.
[09:28] <muninn-project> :)
[09:45] <muninn-project> Mind if we keep using buzilla.
[09:45] <muninn-project> It works,
[09:45] <muninn-project> we allredy have a lot on our minds.
[09:45] <jlschatz> I agree completely :)
[09:45] <muninn-project> ok
[10:02] <jlschatz> My first Q on the report was where to post it - I've got my project proposal page on mediawiki now - should it be on meta.mediawiki, though?
[10:03] <jlschatz> My bigger question was, though, how the project will play out: I was very vague in my proposal because the whole project is so very big. https://www.mediawiki.org/w/index.php?title=Historical_OpenStreetMap
[10:03] <jlschatz> Should my initial mvp be a slider? Or do we need to decide this after the OHM Hangout on Thursday?
[10:19] <jlschatz> afk momentarily
[10:27] <jlschatz> back
[10:30] <muninn-project> Morning
[10:32] <jlschatz> Can you see all my copious notes above?
[10:32] <muninn-project> project report should be on https://www.mediawiki.org/wiki/FOSS_Outreach_Program_for_Women/Round_8#Status
[10:32] <muninn-project> yes.
[10:33] <jlschatz> I see the last column now. Window shrunk for the IRC chat.
[10:33] <muninn-project> ConorMc on #ohm has been working on the slider also
[10:33] <muninn-project> I would like you to take charge of addding the slider into the rails port.
[10:34] <muninn-project> Doesn't need to actually influence the renderer for now
[10:34] <muninn-project> but just work.
[10:34] <jlschatz> You got it. :)
[10:34] <muninn-project> Steal and borrow from ConorMc's too if needed
[10:34] <muninn-project> ofcus on getting it in there.
[10:34] <muninn-project> Chippy on #OHM has access to the machine.
[10:35] <muninn-project> Then the secodn part will attack the renderer.
[10:35] <muninn-project> I don't think that will be that hard.
[10:35] <muninn-project> we just need to agree on how to do it.
[10:35] <jlschatz> Ok. That sounds like a great plan.
[10:35] <muninn-project> Roger .
[10:35] <jlschatz> Yes. Agreement can be hard to come by :).
[10:35] <muninn-project> NowI have to run. 
[10:35] <jlschatz> Ok. Thank you!!
[10:36] <muninn-project> We can also run by fiat. Chippy, me and Susannas are 90% of the governmance for ohm
[10:36] <muninn-project> jeff also.
[10:36] <jlschatz> Cool. :)
[10:36] <muninn-project> are you satisfied eere: finance?
[10:36] <muninn-project> are you full time on this npw?
[10:37] <jlschatz> I think so. I need to stay on at my current place to cover for my boss's upcoming vacation and then I can jump ship.
[10:37] <muninn-project> ok. What are the dates?
[10:38] <jlschatz> She's back on the 2nd of June. I plan to start working on this immediately, though.
[10:39] <muninn-project> Ok. I would like us to talk further on thursday and can you idle in the #OHM irc channel from now on?
[10:40] <jlschatz> Yes.
[10:40] <muninn-project> Awesome.
[10:40] <muninn-project> Ok,  have to run keep in touch.
[10:40] <jlschatz> Ok. Will do.
