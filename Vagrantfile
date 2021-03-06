# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  #  The machines will be running Ubuntu 20.04 Focal Fossa
  config.vm.box = "ubuntu/focal64"
  
  # These settings enable X11 forwarding so that native
  # Linux users can just run a graphic application
  # on the VMs and have that displayed by their local
  # X11 server. This concerns the `xterm` command on
  # mininet, for instance.
  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true

  # We'll allocate 1 GiB of memory to each VM.
  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", 1024]
  end

  # Let's configure the machine running MiniNet machine.
  config.vm.define "scenarioDNS-Tunneling" do |scenarioDNSTunneling|

    scenarioDNSTunneling.vm.hostname = 'scenarioDNSTunneling'

    # It'll be assiged IPv4 address 192.168.56.2 on VirtualBox's NATted network.
    scenarioDNSTunneling.vm.network :private_network,ip:"192.168.56.2"

    # Lets copy the xauthority file
    scenarioDNSTunneling.vm.provision "file", source: "./src/config/Xauthority", destination: "/home/vagrant/.Xauthority"

    # Copy the scenario
    scenarioDNSTunneling.vm.provision "file", source: "./src/scenario.py", destination: "/home/vagrant/scenario.py"
    scenarioDNSTunneling.vm.provision "file", source: "./src/scenario_fulltunneling.py", destination: "/home/vagrant/scenario_fulltunneling.py.py"


    # Copy the run_x11 utility
    scenarioDNSTunneling.vm.provision "file", source: "./src/util/run_x11.sh", destination: "/home/vagrant/run_x11.sh"

    # We'll run the following script to install  mininet, iodine, wireshark
    scenarioDNSTunneling.vm.provision "shell", :path => "./src/util/install_mininet.sh"
    scenarioDNSTunneling.vm.provision "shell", :path => "./src/util/install_wireshark.sh"
    scenarioDNSTunneling.vm.provision "shell", :path => "./src/util/install_iodine.sh"
    scenarioDNSTunneling.vm.provision "shell", :path => "./src/util/install_x11_utils.sh"
    
    
  end
end