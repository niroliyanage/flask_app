import json
def myapp_handler(event, context):
    myapplication = {
        'Version' : 'VersionNumber',
        'Description' : 'VersionDescription',
        'lastcommitsha' : 'VersionCommit'
    }
    return {
        "statusCode": 200,
        "body": json.dumps(myapplication)
    }
