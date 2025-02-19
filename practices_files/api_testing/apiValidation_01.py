import  requests
import json

baseUrl= "https://reqres.in/"

response = requests.get(baseUrl+"/api/users/2")

## Approach 1 to get the response data
# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)   # converting into dict or list
# print(type(dict_response))
# print(dict_response['data']['email'])

## Approach 2 to get the response data
# response_json = response.json()
# print(response_json['data']['email'])


### Example 3
# response= requests.get(baseUrl+"/api/users?page=2",params={"page":2})
# response = response.json()
# print(response)
# print(type(response))
# for actualData in response['data']:
#     print(type(actualData))
#     if actualData["email"]=="rachel.howell@reqres.in":
#         print(actualData)
#         break
# expected_data = {'id': 12, 'email': 'rachel.howell@reqres.in', 'first_name': 'Rachel', 'last_name': 'Howell', 'avatar': 'https://reqres.in/img/faces/12-image.jpg'}
# assert actualData==expected_data
# assert response.status_code ==200
# assert response.headers['Content-Type']== 'application/json'


### Post Request
req_json= {
    "name": "morpheus",
    "job": "leader"
}
response= requests.post(baseUrl+'/api/users',json=req_json)
print(response.json())
response = response.json()
assert response['name']=='morpheus'
# assert response.status_code ==200





