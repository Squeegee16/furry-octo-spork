#! /bin/bash
#echo sudo systemctl show -p ActiveState --value web_thermometer.service
#echo sudo systemctl show -p ActiveState --value temp_logger.service
# check if in active then restart 
#--quiet was removed
systemctl is-active temp_logger.service || sudo service temp_logger restart
sleep 15
systemctl is-active web_thermometer.service || sudo service web_thermometer restart