from bs4 import BeautifulSoup

class lector:
	def __init__(self, html=None):
		self.html=html
	def obtenertag(self, tag=None):
		if self.html:
			doc=self.html
			soup=BeautifulSoup(markup=doc, features="html.parser")  
			return soup.find_all(tag)
  
