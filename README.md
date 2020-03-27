# Ritmic modules

This is the ritmic module main repository. 
It contain the endpoint an instruction to start automatically a ritmic module into a rapsberry.

## Requirements
- Python 3
- Systemctl
-

## Get started
Create a `ritmic` user on your machine , log in it, and clone this repository on your device on the `/home/ritmic/` folder.

Set the config file `config.json` with custom values if needed. 

run `sudo sh install.sh` to install and run the ritmic.service.

## More commands

Start service
`sudo systemctl start ritmic.service`

Restart service
`sudo systemctl restart ritmic.service`

Stop service
`sudo systemctl stop ritmic.service`