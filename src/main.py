import uvicorn
from fastapi import FastAPI
import motor.motor_asyncio
from decouple import config
from v1.endpoints.restaurant import router as RestaurantRouter

app = FastAPI()

#TODO: fix use of deprecated methods
@app.on_event( 'startup' )
def startup_db_client():
    MONGO_DETAILS = config( "MONGO_DETAILS" )
    app.mongodb_client = motor.motor_asyncio.AsyncIOMotorClient( MONGO_DETAILS )
    app.database = app.mongodb_client.morama
    print( 'Porject connected to mongodb 🍃' )

@app.on_event( 'shutdown' )
def shutdown_db_client():
    app.mongodb_client.close()

def get_collection(collection: str):
    return app.mongodb_client.get_collection(collection)


app.include_router(RestaurantRouter, tags=["Restaurant"], prefix="/restaurants")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello world!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)