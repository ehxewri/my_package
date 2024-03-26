from dotenv import load_dotenv
import os
import pandas as pd

# Set environment variables from the .env in the local environment
try:
    load_dotenv()   
    nyt_api_key = os.getenv("NYT_API_KEY")
    tmdb_api_key = os.getenv("TMDB_API_KEY")
    assert nyt_api_key is not None, 'NYT_API_KEY not found in .env file'
    assert tmdb_api_key is not None, 'TMDB_API_KEY not found in .env file'
    
except Exception as e:
    # Handle potential errors in loading .env or missing API keys
    print(f'An error occurred: {e}')
else:
    print('All keys laoded correctly') 
    
# next I will want to verify the Keys work for each api provider
# make a call to each and verify the status code of 200
