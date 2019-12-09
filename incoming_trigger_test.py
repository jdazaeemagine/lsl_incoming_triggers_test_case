"""@author: jdaza"""

import pylsl as lsl
import datetime
import time
import random
import sys 


if __name__ == "__main__":
    
	if(len(sys.argv)<3):
		print("ERROR: Incorrect use of the script")
		print("Use: python incoming_trigger_test.py <numberoftriggers> <interval in seconds>")
		sys.exit()
	
	print("LSL INCOMING TRIGGERS TEST\n")
	
	name = "stream_trigger"

	si = lsl.StreamInfo(name=name, type='Markers', source_id='testing_dep', channel_format=lsl.cf_string)
	so = lsl.stream_outlet(si)
	
	print("It will take 5 seconds to start sending triggers...")
	time.sleep(5) # Make sure that eego got the news of the new stram and subcribes to it. Not needed from the python side
    
    
	triggers = int(sys.argv[1]) #number of triggers
	sleeping_time = int(sys.argv[2]) #time in seconds

	cont = 1

	while(cont<=triggers or triggers is -1):
	
		string = "%i -> %s"%(cont, datetime.datetime.now().time())
    
		print(string)
    
		time.sleep(sleeping_time)
		
		so.push_sample([string], lsl.local_clock())
		cont+=1