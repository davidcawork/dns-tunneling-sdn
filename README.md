# dns-tunneling-sdn
DNS Tunneling in Software Defined Networking (PoC)

![seCampeona](https://pbs.twimg.com/media/FT9dD-YWAAASIbw?format=jpg&name=large)


## Requisitos

Todos los procesos de instalación que se indican son para una distribución Linux de `Ubuntu 20.04 (x86_64)`

*   Vagrant (`Vagrant 2.2.19`)

```bash
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install vagrant
```

## Metodo de instalación 

Bla bla bla 

```bash
git clone https://github.com/davidcawork/dns-tunneling-sdn
cd dns-tunneling-sdn
```

```bash
vagrant up
```

```bash
vagrant ssh vagrant ssh scenarioDNS-Tunneling
```



#### Troubleshooting problems regarding SSH
If you have problems connecting via SSH to the machine, check that the keys in the path `.vagrant/machines/scenarioDNS-Tunneling/virtualbox/` are owned by the user, and have read-only permissions for the owner of the key. 

``` bash
cd .vagrant/machines/scenarioDNS-Tunneling/virtualbox/
chmod 400 private_key

# We could also use this instead of "chmod 400" (u,g,o -> user, group, others)
# chmod u=r,go= private_key
```
Instead of using vagrant's manager to make the SSH connection, we can opt for manually doing it ourselves by passing the path to the private key to SSH. For example:

```bash
ssh -i .vagrant/machines/scenarioDNS-Tunneling/virtualbox/private_key vagrant@192.168.56.2
```

---