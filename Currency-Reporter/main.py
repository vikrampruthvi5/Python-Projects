#!/usr/bin/env python3

import pv_foriegn_price as pv
import os

x= pv.get_EUR()
#print(x)

os.system('curl -X POST -H \'Content-type: application/json\' --data \'{"text":"'+x+'"}\' https://hooks.slack.com/services/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')
