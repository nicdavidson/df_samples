
# get the service and table name for the call. 
# should be able to put this script anywhere in DF event scripts without an issue. 

service_name = event.request.service
table_name = event.resource


## change what field types you want converted to a string. 
#You can find the field types by reading the schema endpoint for the table, add them to this list. 
field_types = ['bigint']

#build a schema endpoint name from the table/service names
schema_endpoint = f'/api/v2/{service_name}/_schema/{table_name}'

get_schema = platform.api.get(schema_endpoint)
results = json.loads(get_schema.read())
# each field will come back as dict with field information in it. 
field_data = results['field']

# grab every field name that matches the field_types, then return those field names. 

# If the type of the field matches one of the types you set above, then add the field name to 
# our list of matching fields. 
matching_fields = [field['name'] for field in field_data if field['type'] in field_types]
# grab the unaltered payload, it is mutable, so just make changes in place

# for every record in the initial payload, convert to a string for the matching fields. 
for record in event.response.content['resource']:
    for field in matching_fields:
        record[field] = str(record[field])