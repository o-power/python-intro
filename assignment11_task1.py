import json
import requests
import sys

try:
    response = requests.get('https://fakejsonapi.com/countries')
    countries = json.loads(response.text)
    print('First element')
    print(countries['country'][0])
    print('Fourth element')
    print(countries['country'][3])

    try:
        with open('countries.json','w') as file_stream:
            json.dump(countries, file_stream, indent=4)
    except:
        print('Something went wrong writing to the JSON file.')
        print(f'Error: {sys.exc_info()[0]}')
    else:
        print('Successfully wrote to JSON file.')
    
except json.decoder.JSONDecodeError:
    print('JSON response could not be deserialized.')
except:
    print('Something went wrong getting a response from the API.')
    print(f'Error: {sys.exc_info()[0]}')
    


