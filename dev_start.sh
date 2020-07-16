#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`

# Add environment variables
source my.env

echo "${yellow}Starting siyavula_api_python_pyramid${reset}"
echo "${yellow}Go to http://localhost:6543/standalone or http://localhost:6543/assignment${reset}"
venv/bin/pserve siyavula_api_python_pyramid/development.ini --reload