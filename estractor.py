import requests

class estractor:
	def __init__(self, URL=None):
		self.URL=URL
		
	def obtenerhtml(self):
        	if self.URL:
            		r=requests.get(self.URL)
            		return r.text
        	else:
            		print ("vacio")
            		return None
