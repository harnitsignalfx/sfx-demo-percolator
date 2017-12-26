import os
import sys
import random
import time
import socket
import signalfx

if 'SF_TOKEN' in os.environ:
    print os.environ['SF_TOKEN']
else:
    print 'SF_TOKEN env variable not found'
    sys.exit(0)

sfx = signalfx.SignalFx().ingest(os.environ['SF_TOKEN'])

try:
    while True:
        sfx.send(counters=[
          {'metric': 'http.requests.received',
          'value': random.randint(900,1100),
          'timestamp':int(round(time.time()*1000)),
          'dimensions': {'containerId': socket.gethostname()}
          }
        ])
        print 'sending..'
        time.sleep(1)
except:
    sfx.stop()
finally:
    sfx.stop()
