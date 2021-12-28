import requests

# adress = 'https://www.google.com/search?q=trident&ei=PkLoYM-jNd6G9u8P07y_kAk&start=10&sa=N&ved=2ahUKEwjPus_m_9XxAhVeg_0HHVPeD5IQ8tMDegQIARA8&biw=1536&bih=722'
# r = requests.get(adress)
# with open('trient-second-page.html', 'w', encoding='utf-8') as file:
#     file.write(r.text)

import time

lat = 48.38
lon = 31.18
cordinates = {
    'lat': lat,
    'lon': lon
}
url = "http://api.open-notify.org/iss-pass.json"
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
answer_obj = requests.get(url, params=cordinates)
result = answer_obj.json()
over_time = result['response'][0]['risetime']
normal_time = time.ctime(over_time)
print(normal_time)
