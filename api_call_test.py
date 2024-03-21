import requests
from my_keepass import get_keys

def get_tmdb():
    my_key,my_url = get_keys('tmdb')
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {my_key}"
    }
    response = requests.get(my_url, headers=headers)
    return (response)

def get_my_times():
    my_key,my_url = get_keys('ny_times')
    headers = f'{my_url}?api-key={my_key}'
    response = requests.get(headers)
    return (response)

def get_own():
    my_key,my_url = get_keys('owm')
    headers = f'{my_url}?lat={33.24}&lon={-96.96}&appid={my_key}'
    response = requests.get(headers)
    return (response)

def get_census():
    my_key,my_url = get_keys('census')
    headers = f'{my_url}?get=NAME,group(B01001)&for=us:1&key={my_key}'
    response = requests.get(headers)
    return (response)

# https://bulk.openweathermap.org/snapshot/weather_zip_us_mmddyy_hhmm.json.gz?appid={API key}
def main():
    print ('This only prints when testing this function\n')
    response = get_tmdb()
    print (f'The Movies DB \n{response.text}')
    response = get_my_times()
    print (f'NY Times \n{response.text}')
    response = get_own()
    print (f'Open Weather Map \n{response.text}')
    response = get_census()
    print (f'US Census Data \n{response.text}')
if __name__ == "__main__":
    main()