#!/bin/bash
clear
echo ""
  _   _ _   _____ ____   ___  _   _ 
 | | | | | |_   _|  _ \ / _ \| \ | |
 | | | | |   | | | |_) | | | |  \| |
 | |_| | |___| | |  _ <| |_| | |\  |
  \___/|_____|_| |_| \_\\___/|_| \_|
                                    
""
# Termux session string generator for TeleBot
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/xditya/TeleBot/master/resources/telebot-setup.py
pip install telethon
python telebot-setup.py