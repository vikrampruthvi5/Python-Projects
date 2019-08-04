#!/usr/bin/env python3

class pv_time():
	
	def get_ist(self):
		import pytz
		from datetime import datetime
		utc = pytz.utc
		pst = pytz.timezone('America/Los_Angeles')
		ist = pytz.timezone('Asia/Calcutta')
	
		#print('Current Date Time in UTC =', datetime.now(tz=utc))
		#print('Current Date Time in PST =', datetime.now(pst))
		#print('Current Date Time in IST =', datetime.now(ist))

		return str(datetime.now(ist))

if __name__ == "__main__":
	x = pv_time()
	ist_time = x.get_ist()
	print(ist_time)
