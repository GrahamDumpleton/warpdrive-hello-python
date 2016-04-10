from __future__ import print_function

import os
import sys

from wsgiref.simple_server import make_server
from wsgi import application

port = int(os.environ.get('WARPDRIVE_HTTP_PORT', '8080'))

httpd = make_server('', port, application)

print('Serving on port %d ...' % port, file=sys.stderr)

httpd.serve_forever()
