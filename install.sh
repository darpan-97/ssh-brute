#!/bin/bash
pip3 install pwntools
curl "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/top-20-common-SSH-passwords.txt" -o passwords.txt
echo -ne "\nCreated a wordlist file passwords.txt\nUSAGE :\n python3 ssh-brute.py [username] [IP address] [port] passwords.txt\n"

