from urllib import request


data = {
    "keys" : ["123456789", "234567891", "345678912"],
    "123456789" : {
        "ID"                : "test1",
        "Sort"              : "test12",
        "type"              : "test13",
        "input"             : "test14",
        "input_length"      : "test15",
        "permutations"      : "test16",
        "permutation_count" : "test17",
        "run_time"          : "test18"
    },
    "234567891" : {
        "ID"                : "test2",
        "Sort"              : "test22",
        "type"              : "test23",
        "input"             : "test24",
        "input_length"      : "test25",
        "permutations"      : "test26",
        "permutation_count" : "test27",
        "run_time"          : "test28"
    },
    "345678912" : {
        "ID"                : "test3",
        "Sort"              : "test32",
        "type"              : "test33",
        "input"             : "test34",
        "input_length"      : "test35",
        "permutations"      : "test36",
        "permutation_count" : "test37",
        "run_time"          : "test38"
    }
}

# print(data[0])

# for operation in data:
#     print(data[operation]["ID"])

event = {
    "keys" : ["type"],
    "values" : ["test23"]
}



keys = event["keys"]
values = event["values"]
    
# if len(keys) != len(values):
#     return{
#         'statusCode': 400,
#         'body': json.dumps('Number of keys provided does not match number of values.')
    # }
    
request_data = {}

for index, value in enumerate(keys):
    request_data[value] = {
        'S': values[index]
    }
    
print(request_data)