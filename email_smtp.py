# -*- coding: utf-8 -*-

import smtplib
import mimetypes
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'test'
to_addr = from_addr
password = 'test'
smtp_server = 'mail.customs.gov.cn'

msg = MIMEMultipart()
msg['From'] = _format_addr('自定义发送方…… <%s>' % from_addr)
msg['To'] = _format_addr('自定义接收方…… <%s>' % to_addr)
msg['Subject'] = Header('测试……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('测试带附件……', 'plain', 'utf-8'))

attach_file = '新建 Microsoft Excel 工作表.xlsx'
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(attach_file, 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    contype, encoding = mimetypes.guess_type(attach_file)
    if contype is None or encoding is not None:
        contype = 'application/octet-stream'  # default MIME type
    maintype, subtype = contype.split('/')
    att = MIMEBase(maintype,subtype)
    mime = MIMEBase(contype, 'xlsx', filename=attach_file)
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=attach_file)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()




