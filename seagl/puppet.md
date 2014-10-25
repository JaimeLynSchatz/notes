Puppet Session
==============
gh@learnpuppet.com
learnpuppet.com
@learnpuppet

fpm - f-ing package manager for dealing with tarballs

If you're not automating, it's going to get messy.

The commit should say WHY you did something, not that you did something
=======================================================================

When you have a problem, donuts work to get folks talking

Disaster Recovery
=================
If you're using Puppet, you can automate some of this.

Look up Kickstart - it keeps being brought up in these talks

Pets vs. Cattle
You're invested in your pets. You feed them, love them, take care of them
Your systems could be your pets.

Cattle have numbers. You can scale them out. If they're sick , you put them down and just get some more.

If your system is easy to rebuild, you will just rebuild when there's a problem.


Pull-based system (not a pushed based system)
The nodes wake up, ask the puppetmaster "What should I look like?", puppetmaster sends it out, node asks "do I look like that" and they go on.

The facts are key-value pairs, maybe structures. You can access them in the code, use templates.
Now the puppetmaster can use the facts sent by the node to make conditional requirements of 

Catalog - the requirements

Reporting - every change, many choices for reporting systems

WHAT not HOW
===========

package { 'ntp': ensure => installed,
}

Imperative, not directive. What, not how.

ls puppet/lib/puppet/provider/package
huge list of goodies

What is zfs? Cron? smf??
There are lots of defined types in Puppet.

class motd {
  file { 'etc/motd' }

serve it up here
Puppet uses erb as a templating engine

github.com/ghoneycutt/puppet-modules

***Look into Puppet meetups***
They meet once a month.

Puppet module cve?? Security, checks for vulnerability for cve's
Factor - what is that?? Check out ghoneycutt's github repo on it

