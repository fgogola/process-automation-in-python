import datetime

import requests as r

url = "http://localhost:8080/get_all_people"
response = r.get(url)
assert response.status_code == 200

print(response.json())