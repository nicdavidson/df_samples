### This is meant to be a post process script which will take a SSN field and obfuscate all but the last 4 numbers. 


# field name as it appears in the database. 
field_name = 'acct_ssn'

records = event.response.content.resource

for record in records: # iterate through every record that was collected
    try:
        if not record[field_name]: # if the value of field_name is None (NULL)
            record[field_name] = 'err' 
        else:
            record[field_name] = str(record[field_name])[-4:]
    ## Generally not a best practice to catch every exception, but I'd rather do that than release a ssn. 
    except Exception as e: # if there is an exception or issue, just make it an err, print the err to the log
        print(str(e))
        record[field_name] = 'err'
