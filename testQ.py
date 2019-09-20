import os
import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import sys
from sys import argv
from IPython.display import HTML

import qpython
from qpython import qconnection
print('qPython %s Cython extensions enabled: %s' % (qpython.__version__, qpython.__is_cython_enabled__))


print('xxxx argv: {}'.format(argv))

sector = argv[1]


rdb = qconnection.QConnection(host='localhost', port=9009, pandas=True)
rdb.open()
print('connected to Kdb service: ')
print(rdb)
query = 'tables[]'
df2 = rdb.sendSync(query)
#rdb.close()
print('...kdb data: ')

fn = '/home/ubuntu/git/code/opt_signal.q'
with open(fn) as f:
    sql = f.read()
print('xxx sql: ',sql)

df = rdb.sendSync(sql)
#print(df.head().to_html())


# python email

fromaddr = "gfeng22@gmail.com"
toaddr = "gfeng22@yahoo.com"
#toaddr = "gfeng22@outlook.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Options put/call dollar ratio - {}".format(sector)

#body = "Please see attached - ".format(sector)
style = '<style>.right_aligned_df td { text-align: right; }</style>'
#HTML(style + df.to_html(formatters=frmt, classes='right_aligned_df'))
int_frmt = lambda x: '{:,}'.format(x)
float_frmt = lambda x: '{:,.0f}'.format(x) if x > 1e3 else '{:,.2f}'.format(x)
frmt_map = {np.dtype('int64'):int_frmt, np.dtype('float64'):float_frmt}
frmt = {col:frmt_map[df.dtypes[col]] for col in df.columns if df.dtypes[col] in frmt_map.keys()}

body = "Please see attached - {}".format(style + df.to_html(formatters=frmt, classes='right_aligned_df'))
msg.attach(MIMEText(body, 'html'))

"""
filename = "{}_put_call_ratio{}.csv".format(sector, (datetime.today() - timedelta(days = 1)).strftime('%Y%m%d'))
attachment = open("/tmp/{}".format(filename), "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
"""


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
with open('/home/ubuntu/.goog/pass.txt') as f:
    secret = f.read()
server.login(fromaddr, secret)

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.sendmail(fromaddr, "gfeng22@outlook.com", text)
server.quit()

print('email has been sent to {}'.format(toaddr))
