import requests

res = requests.get('http://127.0.0.1:8000/api-auth/get_animal_list/').json()
# print(res.get('Cur_OfficialRate'))
print(res)
