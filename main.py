import falcon
import db

class ThingsResource(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        db.cursor.execute('select name from author')
        resp.body = ('''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
   <title>Layout-Blog X</title>
   <link rel="stylesheet" href="/furtive">
 </head>
  <body>
    <h1>Title</h1>
    <h2>Sub Title</h2>
    <p>{}</p>
    <script src="js/scripts.js"></script>
  </body>
</html>
''').format(db.cursor.fetchone()[0])


class CSSResource(object):
    def __init__(self, csspath):
        with open(csspath, 'r') as cssfile:
            self.csscontent = cssfile.read()

    def on_get(self, req, resp):
        """returns css file for /css url"""
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/css'
        resp.body = self.csscontent

# falcon.API instances are callable WSGI apps
application = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()
furtive = CSSResource('/home/Fidtz/layout-blog/furtive/css/furtive.css')

# things will handle all requests to the '/things' URL path
application.add_route('/furtive', furtive)
application.add_route('/things', things)

#db.close()

import subprocess  # for pythonanywhere
subprocess.run(["/home/Fidtz/layout-blog/reload"])  # for pythonanywhere


