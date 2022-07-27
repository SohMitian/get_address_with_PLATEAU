import googlemaps

def rev_geo(lat, lon):
  googleapikey = 'APIKeyをここに入れる'
  gmaps = googlemaps.Client(key=googleapikey)

  geocord = lat + ", " + lon

  results = gmaps.reverse_geocode((geocord), language='ja')
  add = [d.get('formatted_address') for d in results]
  list_add = add[1].split()
  return list_add[1]
