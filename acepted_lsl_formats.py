# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:43:17 2020

@author: jdaza
"""

import time
import pylsl as lsl
import threading

name_format = {
            "cf_float32": lsl.cf_float32,
            "cf_double64": lsl.cf_double64,
            "cf_string": lsl.cf_string,
            "cf_int32": lsl.cf_int32, 
            "cf_int16": lsl.cf_int16, 
            "cf_int8": lsl.cf_int8}    

name_samples = {
            "cf_float32": 0.05,
            "cf_double64": 0.05,
            "cf_string": "test",
            "cf_int32": 55, 
            "cf_int16": 55, 
            "cf_int8": 55}

def push(key): 
        
    si = lsl.StreamInfo(name=key, type='Markers', source_id='testing_dep', channel_format=name_format[key])
    so= lsl.stream_outlet(si)
        
    time.sleep(5)
    print(key)
    
    for i in range(60):
        so.push_sample([name_samples[key]], lsl.local_clock())
        time.sleep(1)
        

if __name__ == "__main__":

    for key in name_format:
        
        time.sleep(5)
        threading.Thread(target=push,args=(key,)).start()