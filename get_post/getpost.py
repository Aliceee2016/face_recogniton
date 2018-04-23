import requests
import json

def get(url):
	req = requests.get(url);
	print("status: " + str(req.status_code))
	print(json.loads(req.text)['id'])
	return json.loads(req.text)
	

def post(url, postData = None):	
	req = requests.post(url, data = postData)
	print("status: " + str(req.status_code))
	return json.loads(req.text)

# get("http://zflxsr.cn:8086/worker/findOne?id=2")
# post("http://zflxsr.cn:8086/attendance/sign", {"workId": "2", "state":"2"})