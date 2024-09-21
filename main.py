from fastapi import FastAPI


APPNAME = "Terminal"
APPDESCRIPTION="Blog Website"


app = FastAPI(
        title=APPNAME,
        description=APPDESCRIPTION,
    )


@app.get("/")
async def home():
    return {"message":"This is home page"}
