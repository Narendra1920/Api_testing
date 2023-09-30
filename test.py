import requests

response= requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=634e0cb65c019e74f06325e1d3aae02f&user_id=199227158%40N02&format=json&nojsoncallback=1")
print (response.json)
print (response.status_code)
