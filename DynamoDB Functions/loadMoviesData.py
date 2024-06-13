import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb','us-west-1')

tabla = dynamodb.Table('Movies')

with open("datosPeliculas.json") as JSONFile:
    movies = json.load(JSONFile, parse_float=decimal.Decimal)
    for movie in movies:
        year = int(movie["year"])
        title = movie["title"]
        info = movie["info"]

        print("Movie added:", year, title)

        tabla.put_item(
            Item = {
                "year": year,
                "title": title,
                "info": info
            }
        )