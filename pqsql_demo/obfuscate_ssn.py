
### This is meant to be a post process script which will take a SSN field and obfuscate all but the last 4 numbers. 


# field name as it appears in the database. 
field_name = 'acct_social'

records = event.response.content


for record in records:
    print(record)
    print('\n...\n')
