from fastapi import FastAPI
from pydantic import BaseModel
import requests


class Text(BaseModel):
    content: str


app = FastAPI()


@app.post("/app2yaml/")
def load(body: Text):
    url = "https://www.javainuse.com/app2yaml"
    response = requests.post(url, json={"jsonText": body.content}, headers={'Content-Type': 'application/json;charset=UTF-8'})
    response_clean = response.text[3:-3]

    return {"result": response_clean}

#https://api-rodrigogcespedes.cloud.okteto.net/docs para acceder a la documentacion del endpoint