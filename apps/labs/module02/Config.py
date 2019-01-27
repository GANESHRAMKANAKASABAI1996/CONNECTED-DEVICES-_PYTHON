'''
Created on Jan 25, 2019

@author: ganes
'''
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# 
# host           = 'smtp.gmail.com'
# port           = 465
# fromAddr       = 'venkat.devicerpi@gmail.com'
# toAddr         = 'venkat.devicerpi@gmail.com'
# authToken      = 'otkimkujeomzbjgh'
# data = "Hello World";
# msg = MIMEMultipart();
# msg['From'] = fromAddr
# msg['To'] = toAddr
# msg['Subject'] = "Intro"
# msgBody = str(data)
# msg.attach(MIMEText(msgBody))
# msgText = msg.as_string()
# # send e-mail notification
# smtpServer = smtplib.SMTP_SSL(host, port)
# smtpServer.ehlo()
# smtpServer.login(fromAddr, authToken)
# smtpServer.sendmail(fromAddr, toAddr, msgText)
# smtpServer.close()

from labs.common import ConfigUtil
from labs.common import ConfigConst
import configparser

config = ConfigUtil.ConfigUtil();
DEFAULT_CONFIG_FILE = "../data/ConnectedDevicesConfig.props"
data = configparser.RawConfigParser();

data.read(DEFAULT_CONFIG_FILE);
print(data.get('smtp.cloud','host' ))

#print(config.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.POLL_CYCLES_KEY))