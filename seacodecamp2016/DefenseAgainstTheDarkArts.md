#Defense Against the Dark Arts - Metrics!

##Productivity
- before asking how do we measure it, ask WHAT DO YOU MEAN BY IT?

##Quality
- is it all just absolute bug counts?

What's the story behind a metric? *How* are the metrics being presented.

###More bugs doesn't mean less quality. More bugs mean somebody LOOKED.

W. Edwards Deming - look him up, quality assurance

How do you cope with the metrics you can see vs. the metrics you can't see and would make big changes if you could

True Mtric vs. Proxy Metric
True - what you *should measure*, "Delivering Software that is Valuable"
or could be you don't have the data *yet* but will have it afer some time

Proxy - what you *can* measure, could be estimated time vs. actual time per feature

You need a reason to believe that the proxy is actually correlated to the true mteric

What about when you actually don't know what your true metrics are - you need to identify what a deisreable outcome even is.

Patrick Linsioni (five disfunctions of a team or "The Advantage") -- get it and READ IT

Question: what is my contribution to that organiational goal?

Cost - Benefit analysis -- measuring cost is easy and that tends to be where we focus
Focus on the BENEFIT you're delivering

don't just tell the half of the story that makes them look bad
Tell the story that shows the value you deliver, the benefit side of the cost-benefit analysis

The expected ROI that the business folks used to justify the project needs to be shared with the developers.
Not just "how long it's going to ttake and how much is it going to cost."
How much is too much, how much is it worth to you? 
What's the MVP? - danger ... they want it, they want it all

HIPPO - Highest Paid Person's Opinion
What's in your backlog that's only there because someone important wants it


## Effective Metrics
* Comparable
* Honest
* Actionable
* Simple

Measure it because you can think of a way for it to be useful, not just because you can.

###Comparable
Story points across teams are NOT comparable. Encourage different teams to use different measuring systems.
If they're all numbers, the temptation to compare them will be great.

Comparable across time, across geographies, that can be good and helpful.

###Actionable
You're contructing an hypothesis - your metrics are checking to see if your hypothesis is correct
You're creating metrics to drive behavior
Based on the measures that you get back, you can make a decision to keep doing something, stop doing something or try something else

Is the team shared right - do they need more resources? If they get more resources, will they deliver more.

###Simple
If they're super complicated, you won't know what actions you took that influenced the metric
If there are too many imputs, you can't isolate the effect of your decision

###Honest
If you're lying to yourselves, you're not getting anywhere

##Who's Your Audience?
Internal
- Simple
- Actionable
- Honest -- don't beat eachother up, but be honest about where you are right now
Did the things you do make enough of a difference?
No --- then do something different!

External
- Simple
- Comparable
- Honest (?)

A team retrospective is different from a Retrospective that's really a report up to management.

Choose metrics that tell a good story about your team.
You may be judged on a metric that you don't do well on -- report that, that's fine. But include the 17 other metrics that look great for you.

If you don't want to be compared with other teams, find a way to compare yourself to your self
- Growth and trends -- trendlines are good
- Ratios and proportions
      Absolute bug counts, story sizes - not comparable
      % of bugs discovered in production vs. pre-production (pushing that metric shows the value of QA)

Be aware how folks feel when you're measuing them.
If they don't trust you, they will game the metrics.

Turnaround time on bugs is a nice metric if you're interested in bugs

##Essential Metrics
###Metrics aren't free
- time to collect
- time to tabulate
- time to pretty up
- tools
- morale
Be sure the benefit justifies the cost!

##Magic Charm for Metrics
- Time to Feedback
Getting the feedback, instant feedback and take action

###True Metrics
Mean time to stakeholder feedback - big picture
Lead time - medium picture -- can include time wasted in bottlenecks
Cycle time - small picture -- from when *you* started it to when *you* finished it (not when it sat waiting for approval or deployment or whatever)

###Proxy Metrics
Wait time -- as a piece of work travels through your organization, where does it go and how long does it wait (kanban boards can help you here)
Touch time
Work In Progress: Little's Law
Queue Length
MTTR - Realize, Recover, Repair, Remediate
Code coverage - teeny, tiny feedback loops

##Self-Organize
Make sure your team can generatetheir own metrics
As you're talking to your boxx and your grand boss, you can show your metrics
You're communicating up

The priority is SO majorly important.
If we all agree the top item in the backlog 
Excaped bug rate