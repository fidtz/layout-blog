import falcon

class ThingsResource(object):
  def on_get(self, req, resp):
    """Handles GET requests"""
    resp.status = falcon.HTTP_200  # This is the default status
    resp.content_type = 'text/html'
    resp.body = ('''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
   <title>The HTML5 Herald</title>
   <link rel="stylesheet" href="/css">
 </head>
  <body>
    <h1>Title</h1>
    <h2>Sub Title</h2>
    <p>content</p>
    <script src="js/scripts.js"></script>
  </body>
</html>
''')

class CSSResource(object):
    def __init__(self, csspath):
        with open(csspath,'r') as cssfile:
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
css = CSSResource('/home/Fidtz/layout-blog/furtive/css/furtive.css')

# things will handle all requests to the '/things' URL path
application.add_route('/css',css)
application.add_route('/things', things)

