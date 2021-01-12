# -*- coding: utf-8 -*-

import smtplib
#smtpObj = smtplib.SMTP('mail.customs.gov.cn', 25)
smtpObj.starttls()
smtpObj = smtplib.SMTP_SSL('mail.customs.gov.cn', 465)
smtpObj.ehlo()
smtpObj.login('test@customs.gov.cn', 'testdd')

smtpObj.sendmail('bjhg_cx1@customs.gov.cn','bjhg_cx1@customs.gov.cn',
                 'Subject: test\ntest ssl.')


smtpObj.quit()



