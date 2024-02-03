import time
import argparse

seconds=60

if(__name__):

    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds",required=False)
    args = parser.parse_args()
    if(args.seconds):
        seconds = args.seconds
        print("The paramenter --seconds was set to {0}".format(seconds))
    else:
        print("--seconds parameter has been not set, using default - {0}".format(seconds))
        
    print("exiting in {0}s...".format(seconds))
    try:
       if not type(int(seconds)) is int:
           raise Exception("Only integers are allowed")
       else:
           for x in range(int(seconds)):
            print("waiting for {0}".format(x))   
            time.sleep(1)
    except Exception as err:
        print("An exception occured - {0}".format(err))


