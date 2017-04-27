import sys
import os

from comtypes import client

f = os.path.abspath(sys.argv[1])
if not os.path.exists(f):
    print "No such file!"
    sys.exit(-1)

powerpoint = client.CreateObject('Powerpoint.Application')
powerpoint.Presentations.Open(f)
powerpoint.ActivePresentation.Export(f, 'PNG')
powerpoint.ActivePresentation.Close()
powerpoint.Quit()
