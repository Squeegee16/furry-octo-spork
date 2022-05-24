#! /usr/bin/env python3

# service has not been enabled untill ready for deployment
# use sudo systemctl start webtem.service
# once reat use sudo systemctl enable webtem.service

from website import temp

app = temp()#ref from init.py

if __name__ == '__main__':# run this file directly
    try:
        app.run(debug = True, host = "192.168.0.156", port = 5500) # auto rerun of webapp when changes occur

    except KeyboardInterrupt:
        print('User Stop')
