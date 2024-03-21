# Using Password vaults in PY code. 
As a security professional I hate when security information is in code or stored in easily access manors. 
the goal is to have a local keepass repository with Functions to pass sensitive information into PY code. 
User name, password, keys and other sensitive information can be passed to PY during execution. 

I need to document how to 
- get keepass loaded locally.
- how to add entries to keepass
- how to import keepass
- how to retrieve information from kepass

current files

-my_keepass

-- function get_keys(title)
when getpass entry is setup there is a unique title specified. this hast to be passed when calling get_pass this returns 

      --- url

      --- key

-my_call_test.py
This is a way store the URL and key used in API calls. 
currently 4 site keys have been stored. looking to improve this

other improvement will be adding entries in a programatic way
More to come.. 
