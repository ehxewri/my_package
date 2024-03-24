import os   
from dotenv import load_dotenv
from pathlib import Path

# this is just to see the working directory that vs is using
current_working_directory = Path.cwd()
print(current_working_directory)

dotenvpath = os.getenv('dotenv_path')
print (dotenvpath)
load_dotenv(dotenv_path=dotenvpath,verbose=True)

# this reads the two fake key from the file. 
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')

# this prints the fake values. replace with your real keys after you test.
print(database_url)
print(api_key)