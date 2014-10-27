Vagrant
=======
Lisa Hagemann
@lhagemann

Check out her github repos

You can automate tests into the configuration automation

Great way to learn DB admin

Vagrant Share and Vagrant Cloud - hashicorp has some hosted options, http sharing - share what you're working on with your team. They can ssh into your box on your local machine.***

adding boxes vagrant box add <name><url>
vagrant box list

Vagrant Cloud - vetted by hashicorp
vagrantbox.es - know who you're downloading from
You can make your own Vagrant box - you can use Chef to provision your Vagrant Box (you need Chef on your client.)
Don't put the Vagrant Box in your project repository, though - they're waaaay too big for that.

vagrant box add <user>/<box>
such as vagrant box add chef/debian-7.4

or do vagrant box add <title><url>

vagrant init ubuntu/trusty64
This will create your vagrantfile, populated with the filename information you feed it.

READ the Vagrantfile
====================
It has tons of helpful information in the comments sections


config.vm.synced_folder "../data", "/vagrant_data" /* give it a relative path to the file on the guest and to the host --- look this up, yo missed someting"

Provisioning
============
* shell
* Chef
* Puppet
* ??
* Vagrant is a great way to learn provisioning automation

You can practice, get comfy, Vagrant is easy, Chef is hard, but you can play around, test it. You just change the line in the Vagrant file keep all of your provisioning files.

config.vm.provision :shell, :path => "bootstrap.sh"
tell vagrant you're using a sheel script and give it a path to the script

or use chef
config.vm.provision "chef_solo" do |chef|
  chef.add_recipe "demo::packages"
  chef.add_recipe "demo::webserver"
  chef.add_recipe "demo::db"
  chef.json = {
    :demo => {
...
You can add any configuration changes and editing that you need here so that you don't need to go in and do odd things.

VirtualBox will tell you all running Vagrant boxes
==================================================
VirtualBox isn't just there to be pretty. Look into it from time to time

learnchef.opscode.com
http://misheska.com/blog/2013/06/16/getting-started-with-chef-cookbooks-the-berkshelfway-org

Ask about that presentation thing


