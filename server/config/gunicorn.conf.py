import os

# basic
bind = '0.0.0.0:80'
proc_name = 'hakumai-server'
workers = 2
max_requests = 1000
max_requests_jitter = 100

# log
accesslog = './log/access.log'
errorlog = './log/error.log'