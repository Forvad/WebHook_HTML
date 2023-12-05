from requests import get, post

json = {'text': '''<!DOCTYPE html>
<html>
  <head>
    <title>Моя веб-страница</title>
  </head>
  <body>
    <h1>Привет, мир!</h1>
    <p>Это моя первая веб-страница.</p>
  </body>
</html>'''}

r = post('http://167.86.84.189:8000/convert', json=json)
print(r.text)

# r = get('http://167.86.84.189:8000/download/1701769879.6184957_result.html')
# print(r.text)

