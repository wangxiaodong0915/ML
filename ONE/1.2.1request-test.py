# -*- coding: UTF-8 -*-
import requests
r = requests.get('https://api.github.com/users/acombs/starred')
print(r.json())