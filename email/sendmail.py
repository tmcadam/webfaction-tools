import smtplib, time, sys, os, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email.encoders import encode_base64
from types import SimpleNamespace
import json

class Email:
    msg = MIMEMultipart
    config = SimpleNamespace

    def __init__(self, _config_file, _files=[]):
        self.config = self.load_config(_config_file)
        self.configure_msg()
        self.load_files(_files)

    def load_config(self, _config_file):
        with open(_config_file) as json_data:
            config = SimpleNamespace(**json.load(json_data))
            config.smtp_server = SimpleNamespace(**config.smtp_server)
            return config

    def configure_msg(self):
        self.msg = MIMEMultipart()
        self.msg['From'] = self.config.from_addr
        self.msg['To'] = ', '.join(self.config.to_addrs)
        self.msg['Date'] = formatdate(localtime=True)
        self.msg['Subject'] = self.config.subject
        self.msg.attach( MIMEText(self.config.body) )

    def load_files(self, _files):
        for file in _files:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload( open(file,'rb').read() )
            encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"'
                            % os.path.basename(file))
            self.msg.attach(part)

    def send(self):
        smtp = smtplib.SMTP(    self.config.smtp_server.name,
                                self.config.smtp_server.port )

        smtp.login( os.environ[ self.config.smtp_user_var ],
                    os.environ[ self.config.smtp_pass_var ])

        smtp.sendmail(  self.config.from_addr,
                        self.config.to_addrs,
                        self.msg.as_string() )
        smtp.close()

Email( sys.argv[1], sys.argv[2:] ).send()
