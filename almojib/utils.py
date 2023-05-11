import requests
headers = {
  "User-Agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
  "accept":"application/json, text/plain, */*"
}
api = "https://api.almojib.com/ar/api/v1.1{}".format
def get(cc:str):
	return requests.get(api(cc),headers=headers)	
def post(cc:str,data=None):
	if data == None:
		return requests.post(api(cc),headers=headers)
	else:
		return requests.post(api(cc),headers=headers,data=data)