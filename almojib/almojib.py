from .utils import headers
from .utils import api
from .utils import get
from .utils import post
from .objects import search
class Almojib:
	def __init__(self):
		self.api = api
		self.headers = headers
	def search(self,text:str,page:str="1"):
		self.text = text
		self.page = page
		response = get(f"/v1.1/faq/search?page={self.page}&search={self.text}")
		return search(response.json())
	def get_home_questions(self,start:str="1",end:str="10"):
		self.start = start
		self.end = end
		response = get(f"/faq/question/recommended?page={self.start}&per_page={self.end}")
		return search(response.json())