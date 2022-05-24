#! /usr/bin/env python3
import sys, re
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError, OperationalError
from datetime import datetime
from rssi_db import main

import datetime, time

from os import path

def log():
    while True:
        device_file = '/sys/bus/w1/devices/10-000802354c82/w1_slave' 

        Base = declarative_base()
        db_path = path.join(path.dirname(__file__), 'website/'+'temprature.db')
        db_uri = 'sqlite:///{}'.format(db_path)
        engine = create_engine(db_uri, echo=False)
        
        class Temprature(Base):
            __tablename__ = 'Temprature'
            eid = Column(Integer, primary_key=True,nullable = True)
            date_stamp = Column(String(27),unique = False,nullable = True)
            year = Column(String(4),unique = False,nullable = True)
            mon = Column(String(2),unique = False,nullable = True)
            day = Column(String(2),unique = False,nullable = True)
            tod = Column(String(8),unique = False,nullable = True)
            hour = Column(String(2),unique = False,nullable = True)
            minute = Column(String(2),unique = False,nullable = True)
            temp = Column(Float,unique = False, nullable = True, default = 0.0)

            def __repr__(self):
                return f"Temprature('{self.eid}','{self.date_stamp}','{self.temp}')"

        if not path.exists('temprature.db'):
            Base.metadata.create_all(engine)
            # print('New Database Created!')
        else:
            1# print('Using existinig Database')

        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        x2 = datetime.datetime.now()

        try:
            f=open(device_file,'r')#read file
            lines = f.readlines()
            f.close()
            # 22 00 4b 46 ff ff 09 10 c0 : crc=c0 YES
            # 22 00 4b 46 ff ff 09 10 c0 t=17187
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
            t = Temprature(date_stamp = x2,year = x2.strftime("%Y"),mon = x2.strftime("%m"), day = x2.strftime("%d"), tod = x2.strftime("%T"), hour =x2.strftime("%H"), minute = x2.strftime("%M"),temp = temp_c)
            session.add(t)
            session.commit()

        except IndexError:
            print('index Error')

        except ValueError:
            print('Value Error')

        except FileNotFoundError:
            print('File error')
            t = Temprature(date_stamp = '0000-00-00 00:00:00.000000',year = '0000',mon = '00', day = '00', tod = '00:00:00', hour = '00', minute = '00',temp = 0)
            print('logged temp')
            session.add(t)
            session.commit()         

        except IntegrityError:
            session.rollback()
            print('Database entry error')

        except OperationalError:
            print(x2,"OperationalError: can't connect, exiting")
            sys.exit()
            break

        except KeyboardInterrupt:
            print('User Stop')
            session.commit() 
            session.close()
            break
            
        time.sleep(300)
        rssi_db.main()
        

####################################################
if __name__ == '__main__':# run this file directly
    log()
# service --status-all
# systemctl --type=service
# ss -ltup
