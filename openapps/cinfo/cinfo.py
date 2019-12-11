import os
import sys
here = sys.path[0]
print here
sys.path.insert(0,os.path.join(here,'..','..','..','coap'))

from coap import coap
import signal

MOTE_IP = 'bbbb::1415:92cc:0:4'
UDPPORT = 61618 # can't be the port used in OV

c = coap.coap(udpPort=UDPPORT)

# read the information about the board status

txt='coap://[{0}]/w'.format(MOTE_IP)
print txt
p = c.GET(txt)
print ''.join([chr(b) for b in p])


while True:
        input = raw_input("Done. Press q to close. ")
        if input=='q':
            print 'bye bye.'
            #c.close()
            os.kill(os.getpid(), signal.SIGTERM)
