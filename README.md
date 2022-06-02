# dns-tunneling-sdn
DNS Tunneling in Software Defined Networking (PoC)

![seCampeona](https://pbs.twimg.com/media/FT9dD-YWAAASIbw?format=jpg&name=large)


## Requisitos

Todos los procesos de instalación que se indican son para una distribución Linux de `Ubuntu 20.04 (x86_64)`

*   Vagrant (`Vagrant 2.2.19`)

```
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install vagrant
```