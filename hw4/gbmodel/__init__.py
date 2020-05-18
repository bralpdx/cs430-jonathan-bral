"""
Imports the model form the sqlite databackend file
"""
# model_backend = 'sqlite3'
model_backend = 'dynamodb'

if model_backend == 'sqlite3':
    from .model_sqlite3 import model
elif model_backend == 'dynamodb':
    from .model_dynamodb import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
