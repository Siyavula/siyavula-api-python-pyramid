#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
blue=`tput setaf 4`
reset=`tput sgr0`

# Add environment variables
source my.env

echo "${yellow}Starting siyavula_api_python_pyramid${reset}"
echo "${green}Routes:${reset}"
echo -e "${green}\tStandalone Activity: ${reset}${blue}http://localhost:6543/standalone${reset}"
echo -e "${green}\tAssignment Activity: ${reset}${blue}http://localhost:6543/assignment${reset}"
echo -e "${green}\tPractice Activity: ${reset}${blue}http://localhost:6543/practice${reset}"
echo -e "${green}\tPractice Activity Table of Contents: ${reset}${blue}http://localhost:6543/practice-toc${reset}"
echo -e "${green}\tPractice Activity Table of Contents (Mastery Applied): ${reset}${blue}http://localhost:6543/practice-toc-mastery${reset}"
venv/bin/pserve siyavula_api_python_pyramid/production.ini
