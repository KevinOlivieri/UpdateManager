#!/bin/sh

#Colors
ORANGE='\033[0;33m' #Orange
CYAN='\33[0;36m' #Cyan
NC='\033[0m' #NoColor
#StartScript
echo "${ORANGE}Starting update utility..."
echo "\n${CYAN}Updating distributions (1/5)"
echo "${NC}"
sudo apt-get update
echo "\n${CYAN}Upgrading software (2/5)"
echo "${NC}"
sudo apt-get upgrade
echo "\n${CYAN}Upgrading distro (3/5)"
echo "${NC}"
sudo apt-get dist-upgrade
echo "\n${CYAN}Autoremoving software (4/5)"
echo "${NC}"
sudo apt-get autoremove
echo "\n${ORANGE}Updating system complete (5/5)"
exit