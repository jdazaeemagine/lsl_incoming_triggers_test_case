"""@author: jdaza"""

import pylsl as lsl
import datetime
import time
import random
import sys 

if __name__ == "__main__":
    
 
    name = f"Testing_lsl_stream"

    si = lsl.StreamInfo(name=name, type='Markers', source_id='testing_dep', channel_format=lsl.cf_string)
    so = lsl.stream_outlet(si)

    time.sleep(5) # Make sure that eego got the news of the new stram and subcribes to it. Not needed from the python side
    
    
    triggers = sys.argv[1] #number of triggers
    sleeping_time = sys.argv[2] #time in seconds

    cont = 0

    while(cont<triggers or triggers is -1):
    
        string = "%i -> %s"%(cont, datetime.datetime.now().time())
    
        print(string)
    
        time.sleep(sleeping_time)
        so.push_sample([string], lsl.local_clock)
        cont+=1