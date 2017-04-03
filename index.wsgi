# coding: UTF-8
import os
import sys
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'kennethreitz-requests-296928f')) 
import sae
import web
  
from weixinInterface import WeixinInterface
  
urls = (
'/weixin','WeixinInterface'
)
  
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)
  
app = web.application(urls, globals()).wsgifunc()  
application = sae.create_wsgi_app(app)
