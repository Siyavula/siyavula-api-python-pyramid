#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`

# Update requirements
echo "${yellow}Updating requirements${reset}"
venv/bin/pip install -r requirements.txt

echo "${green}Update completed successfully${reset}"