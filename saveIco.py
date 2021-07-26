import requests  # https://docs.python-requests.org/en/master/

r = requests.get('https://lerneprogrammieren.de/favicon.ico')

print('Status Code:')
print(r.status_code) # https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

print('Content:')
open("icon.ico","wb").write(r.content)