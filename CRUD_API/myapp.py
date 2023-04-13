import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
     data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data()        

def post_data():
   data = {
      'name':'Varun',
      'roll': 212,
      'city':'Loharu'
   }

   json_data = json.dumps(data)
   r = requests.post(url=URL, data=json_data)
   data = r.json()
   print(data)

# post_data()

#Function for updating data
def update_data():
   data = {
      'id':4,
      'name':'Ahuja',
      'city':'Rewari'
   }

   json_data = json.dumps(data)
   r = requests.put(url=URL, data=json_data)
   data = r.json()
   print(data)

# update_data()


#Function for deleting data

def delete_data():
   data = {
      'id':4
   }

   json_data = json.dumps(data)
   r = requests.delete(url=URL, data=json_data)
   data = r.json()
   print(data)

delete_data()

