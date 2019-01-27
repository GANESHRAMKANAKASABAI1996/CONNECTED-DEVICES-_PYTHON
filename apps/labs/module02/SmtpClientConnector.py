'''
Created on Jan 24, 2019

@author: GANESHRAM KANAKASABAI
'''
from labs.common import ConfigUtil
from labs.common import ConfigConst
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
'''
creating a class smtpClientConnector
'''
class SmtpClientConnector(object):
    '''
    constructor of smtpClientConnector
    '''
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props');
        print('Configuration data...\n' + str(self.config));
        self.config.loadConfig();
    '''
    PublicMessage function is used to build and construct message and is sent as a notification.
    @param topic: Subject to Email
    @param data : Sensor notification
    '''  
    def publishMessage(self, topic, data):
        host = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.HOST_KEY);
        port = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.PORT_KEY);
        fromAddr = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.FROM_ADDRESS_KEY);
        toAddr = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.TO_ADDRESS_KEY);
        authToken = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.USER_AUTH_TOKEN_KEY);
        msg = MIMEMultipart();
        msg['From'] = fromAddr;
        msg['To'] = toAddr;
        msg['Subject'] = topic;
        msgBody = str(data);
        msg.attach(MIMEText(msgBody));
        msgText = msg.as_string();# Here the email notification is sent .
    
        try:  
            smtpServer = smtplib.SMTP_SSL(host, port);#Connecting SMTP server at given port number.
            smtpServer.ehlo();#method calling SMTP extended hello
            smtpServer.login(fromAddr, authToken);
            smtpServer.sendmail(fromAddr, toAddr, msgText);
            smtpServer.close();
        except:
            print("Error in Sending Mail");