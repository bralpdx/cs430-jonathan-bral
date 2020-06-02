from .Model import Model
import boto3

class model(Model):
    def __init__(self):
        self.resource = boto3.resource("dynamodb", region_name="us-east-1")
        self.table = self.resource.Table("todo_list")
        try:
            """
            Tries to load the existing table.
            """
            self.table.load()
        except:
            """
            If table does not already exist,
            creates table.
            """
            self.resource.create_table(
                    TableName="todo_list",
                    KeySchema=[
                        {
                            "AttributeName": "title",
                            "KeyType": "HASH"
                        },
                        {
                            "AttributeName": "prio",
                            "KeyType": "RANGE"
                        }
                    ],
                    AttributeDefinitions=[
                        {
                            "AttributeName": "title",
                            "AttributeType": "S"
                        },
                        {
                            "AttributeName": "prio",
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


        return([ [f['title'], f['desc'], f['prio']] for f in gbentries['Items']])

    def insert(self, title, desc, prio):
        gbitem= {
                'title': title,
                'desc' : desc,
                'prio' : prio
            }

        try:
            self.table.put_item(Item=gbitem)
        except:
            return False
        
        return True
