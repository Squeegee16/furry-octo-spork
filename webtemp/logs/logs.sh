#! /bin/bash

sudo cat /var/log/messages >> /home/markone/logs/msgs
sudo cat /var/log/syslog >> /home/markone/logs/sys_log
sudo cat /var/log/auth.log >> /home/markone/logs/auth_logs
sudo cat /var/log/bootstrap.log >> /home/markone/logs/boot_logs
sudo cat /var/log/dmesg >> /home/markone/logs/dmesg_logs
sudo cat /var/log/kern.log >> /home/markone/logs/kern_logs
sudo cat /var/log/faillog >> /home/markone/logs/fail_logs
sudo cat /var/log/cron >> /home/markone/logs/cron_logs
sudo cat /var/log/btmp >> /home/markone/logs/btmp_logs
sudo cat /var/log/daemon.log >> /home/markone/logs/daemon_logs
sudo cat /var/log/wtmp >> /home/markone/logs/wtmp_logs
sudo cat /var/log/vsftpd.log >> /home/markone/logs/vsftpd_logs
sudo cat /var/log/user.log >> /home/markone/logs/user_logs
sudo cat /var/log/debug >> /home/markone/logs/debug_logs
sudo cat /var/log/dpkg.log >> /home/markone/logs/dpkg_logs