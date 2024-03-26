import requests
import time
from dotenv import load_dotenv
import os

def key_check(key_path=None):
    try:
        load_dotenv(key_path,override=True)   
        nyt_api_key = os.getenv("NYT_API_KEY")
        tmdb_api_key = os.getenv("TMDB_API_KEY")
        assert nyt_api_key is not None, 'NYT_API_KEY not found in .env file'
        assert tmdb_api_key is not None, 'TMDB_API_KEY not found in .env file'
        responce=requests.get(f'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={nyt_api_key}')
        assert responce.status_code == 200, f'The key provided failed to authenticate nyt_api_key {nyt_api_key} code {responce.status_code}'
        responce=requests.get(f'https://api.themoviedb.org/3/movie/11?api_key={tmdb_api_key}')
        assert responce.status_code == 200, f'The key provided failed to authenticate tmdb_api_key {tmdb_api_key} code {responce.status_code}'
    except Exception as e:
        # Handle potential errors in loading .env or missing API keys
        print(f'An error occurred: {e}')
        return (False)
    else:
        print('All keys laoded correctly')
        return(True)


if __name__ == "__main__":
    print (key_check())