# coding: UTF-8
import requests
import time
from sae.storage import Bucket


TOKEN_PAIR = ('09T037P4KDARV7SK', '21Z7W9V2SPFK17MD')



def checktest(tt):
   def gpng(txt):
    url = 'https://api.handwriting.io/render/png'
    params = {
      'handwriting_id': '2D5S18M00002',
      'handwriting_size': 'auto',
      'width': '500px',
      'height': '320px',
      'line_spacing': '1.5',
      'line_spacing_variance': 0.1,
      'text': 'Though bladed corn be lodged and trees blown down'
    }

    params['text']=txt
    r = requests.get(url, auth=TOKEN_PAIR, params=params)
    return r 

   correct_time = time.strftime('%m_%d_%H_%M_%S',time.localtime(time.time()))
   bucket = Bucket('tempic') #修改成你自己的storage名
   bucket.put()
   bucket.post(acl='.r:*', metadata={'expires': '1d'})
   f = gpng(tt)
   data = f.content
   bucket.put_object(correct_time+".png", data)
   file_url = bucket.generate_url(correct_time+".png")
   return file_url
     