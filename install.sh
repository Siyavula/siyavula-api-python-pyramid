#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`

# Create the virtual environment
if [ -d "venv" ]; then
    echo "${green}Virtual environment exists${reset}"
else
    echo "${yellow}Creating Virtual environment${reset}"
    virtualenv --python=python3.8 venv
    echo "${green}Virtual environment created${reset}"
fi

# Upgrade packaging tools
echo "${yellow}Upgrade packaging tools${reset}"
venv/bin/pip install --upgrade pip setuptools

# Install app
echo "${yellow}Installing siyavula_api_python_pyramid${reset}"
cd siyavula_api_python_pyramid
../venv/bin/pip install -e ".[testing]"
echo "${green}Completed installing siyavula_api_python_pyramid successfully${reset}"

# Install requirements
echo "${yellow}Installing requirements${reset}"
cd ../
venv/bin/pip install -r requirements.txt

echo "  ${green}Installation completed successfully${reset}"
