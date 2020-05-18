from .Model import Model
from datetime import datetime
import boto3

class model(Model):
    def __init__(self):
        self.resource = boto3.resource("dynamodb", region_name="us-east-1")
        self.table = self.resource.Table('cartlist')
        try:
            self.table.load()
        except:
            self.resource.create_table(
                TableName="cartlist",
                KeySchema=[
                    {
                        "AttributeName": "name",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "date",
                        "KeyType": "RANGE"
                    }
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "name",
                        "AttributeType": "S"
                    },
                    {
                        "AttributeName": "date",
                        "AttributeType": "S"
                    }
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1
                }
            )

    def select(self):
        try:
            gbentries = self.table.scan()
        except Exception as e:
            return([['scan failed', '.', '.', '.']])

        return([[
            f['name'],
            f['street'],
            f['city'],
            f['state'],
            f['zipcode'],
            f['hours'],
            f['phone'],
            f['rating'],
            f['review'],
            f['foodtype'],
            f['date']] for f in gbentries['Items']])

    def insert(self,name, street, city, state, zipcode, hours, phone, rating, review, foodtype):
        gbitem = {
            'name' : name,
            'street':street,
            'city':city,
            'state':state,
            'zipcode':zipcode,
            'hours':hours,
            'phone':phone,
            'rating':rating,
            'review':review,
            'foodtype':foodtype,
            'date' : str(datetime.today())
            }

        try:
            self.table.put_item(Item=gbitem)
        except:
            return False

        return True

