import boto3

def dynamodb_getitem(resource,table,movieTitle,movieYear):
    dynamodb = boto3.resource(resource)
    tabla = dynamodb.Table(table)
    
    title = movieTitle
    year = movieYear 

    response = tabla.get_item(
        Key = {
            'year': movieYear,
            'title': movieTitle
        },
        ProjectionExpression = "title, info.plot"
    )
    item = response['Item']
    print(item)
    return item

dynamodb_getitem('dynamodb','Movies','Titanic',1997)
dynamodb_getitem('dynamodb','Movies','Nebraska',2013)