import os
from pykeepass import PyKeePass

def get_keys(my_title):
    entry = PyKeePass("C:\SRC\AI\AI-TMP\\ai.kdbx",password=os.getenv("KEEPASS_PASSWORD")).find_entries(title=my_title, first=True)
    return(entry.custom_properties.get('key'),entry.url)

def main():
    my_title=input("enter the title for your key : ")
    my_key,my_url = get_keys(my_title)
    print(f'my key is \n{my_key} \nfor the url \n{my_url}')
    

if __name__ == "__main__":
    main()