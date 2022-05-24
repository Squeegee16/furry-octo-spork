#! /bin/bash
#echo sudo systemctl show -p ActiveState --value web_thermometer.service
#echo sudo systemctl show -p ActiveState --value temp_logger.service
# check if in active then restart 
#--quiet was removed
systemctl is-active temp_logger.service || temp_logger.service restart
sleep 30
systemctl is-active web_thermometer.service || web_thermometer.service restart

