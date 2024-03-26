# this is a small sample code for the try command. 

for seeing what this does. try commenting out the 

# from   dotenv import load_dotenv

also try to change the key in each of these to see the way it handles a failure to get a key

    nyt_api_key = os.getenv("NYT_API_KEY")
    tmdb_api_key = os.getenv("TMDB_API_KEY")

    if you change "NYT_API_KEY" to "NYT_API_KEY_test"

    hope this helps
