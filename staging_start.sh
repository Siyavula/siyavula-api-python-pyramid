#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
blue=`tput setaf 4`
reset=`tput sgr0`

# Add environment variables
source my.env

source routes.sh

venv/bin/pserve siyavula_api_python_pyramid/staging.ini
