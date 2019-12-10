# Test case for LSL incoming triggers

Steps to run the script:

1. If you have python not installed, install it (version 3.7): 

https://www.python.org/downloads/

2. Install pylsl with the following command in the CMD:

```py -m pip install pylsl```

3 Using the CMD prompt, go to the script folder path (using ```cd```). For example:

```cd C:\Users\neuro\Desktop\pytest```

4. To execute the script use the following command specifying the number of triggers and its interval time between them (in secs). 

If you want to send infinite triggers use -1 and finalize the script using ```Ctrl + C```

```py incoming_trigger_test.pz <numberoftriggers> <intervalseconds>```
