import falcon
import db

class HtmlResource(object):

    def __init__(self, htmlrequired):
        db.cursor.execute("select content from text_resources where resourcename = '{}'".format(htmlrequired))
        self.htmlcontent = db.cursor.fetchone()[0]

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        resp.body = self.htmlcontent

class CSSResource(object):
    def __init__(self, cssrequired):
        db.cursor.execute("select content from text_resources where resourcename = '{}'".format(cssrequired))
        self.csscontent = db.cursor.fetchone()[0]

    def on_get(self, req, resp):
        """returns css file for /css url"""
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/css'
        resp.body = self.csscontent

# falcon.API instances are callable WSGI apps
application = falcon.API()

# Resources are represented by long-lived class instances
home = HtmlResource('initalhome')
furtive = CSSResource('furtive')

# things will handle all requests to the '/things' URL path
application.add_route('/furtive', furtive)
application.add_route('/', home)

import subprocess  # for pythonanywhere
subprocess.run(["/home/Fidtz/layout-blog/reload"])  # for pythonanywhere


