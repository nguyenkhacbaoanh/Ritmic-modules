#!/bin/bash

sudo cp ritmic.service /lib/systemd/system/ritmic.service
sudo systemctl daemon-reload
sudo systemctl enable ritmic.service
sudo systemctl restart ritmic.service