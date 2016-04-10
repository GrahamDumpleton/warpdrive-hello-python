import os

from wsgiref.simple_server import make_server
from wsgi import application

port = int(os.environ.get('WARPDRIVE_HTTP_PORT', '8080'))

httpd = make_server('', port, application)
print 'Serving on port %d ...' % port
httpd.serve_forever()
