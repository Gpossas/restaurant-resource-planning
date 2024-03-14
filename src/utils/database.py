from fastapi import Request

def get_collection( request: Request, collection: str ):
    return request.app.database.get_collection(collection)