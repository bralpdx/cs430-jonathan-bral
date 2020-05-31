from .model_dynamodb import model

# Sets the backend db to dynamodb instance
appmodel = model()

def get_model():
    return appmodel


