import requests
import json

url = "http://localhost:8000/Student/"

def postdata():
	data = {
		'name' : 'anil',
		'roll' : 5,
		'city' : 'delhi' 
		}

	json_data = json.dumps(data)

	r = requests.post(url=url,data =json_data)
	print(r.json())

postdata()

def getdata(id = None):
	data = {}
	if id is not None:
		data = {'id': id}
	json_data = json.dumps(data)
	r = requests.get(url = url, data = json_data )
	data = r.json()
	print(data)

getdata()

def update_data():
	data = {
		'id' : 5,
		'name' : 'Dhruvit',
		'city' : 'Surat'
	}

	json_data = json.dumps(data)
	r = requests.put(url = url , data = json_data)
	print(r.json())

# update_data()
def delete_data():
	data = {'id' : 6}

	json_data = json.dumps(data)
	r = requests.delete(url = url , data = json_data)
	print(r.json())

# delete_data()