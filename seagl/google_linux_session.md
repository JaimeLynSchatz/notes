Session 1: Google Powered by Linux and Linux Powered by Google
==============================================================
How does Google use linux, etc (see avoe)

Ok, Google Powered by Linux, got it.

How can we do some cool stuff with Linux via Google?

**The Google Compute Engine**
Big Query - aggregates logs from other systems
There's a lot on this in the GitHub data vis challenge

*It's a sales pitch. I'm a sucker.*

from libcloud.compute.types import Provider
from libcloud.poumpute.providers import get_driver

connection - get_driver(Provider.GCE) (EMAIL, KEY, project=PROJECT_ID)

There's also Ruby fog, and jclouds for Java

Combining VMs with Puppet, Chef, Saltstack, etc.

**Beyond Virtual Machines**
On to Docker and Friends
Kubernetes - new project by Google
OS container cluster manager

Kubernetes
==========
There are sample apps in the package - go get them and check them out.


g.co/cloudstarterpack
promo code erjohnso for a $500 cloud platform credit
https://www.gcp-live.com/
http://bit.ly/use-gce
kubernetes.io/
