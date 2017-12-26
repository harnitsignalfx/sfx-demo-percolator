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

userDim = 'Default'

if 'USER_DIM' in os.environ:
    userDim = os.environ['USER_DIM']

sfx = signalfx.SignalFx().ingest(os.environ['SF_TOKEN'])

try:
    while True:
        sfx.send(counters=[
          {'metric': 'documents.processed',
          'value': random.randint(700,1200),
          'timestamp':int(round(time.time()*1000)),
          'dimensions': {'containerId': socket.gethostname(),'user': userDim}
          }
        ])
        print 'sending..'
        time.sleep(1)
except:
    sfx.stop()
finally:
    sfx.stop()
