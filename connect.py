
# importing the requests library
import requests
  
# api-endpoint
#URL = "http://localhost:8080/camera/licencePlate/"
  
# location given here
#location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API
#PARAMS = {'address':location}
  
# sending get request and saving the response as response object
#r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
#data = r.json()

API_ENDPOINT= 'http://localhost:8080/camera/licencePlate/something'
        
        #datas = {'licensePlate':licensePlate}

        #header = {'content-type': 'application/json'}

r = requests.post(url = API_ENDPOINT, data = "REINE")
        # headers = header,

print(r.status_code)
print(r.json)
