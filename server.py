from fastapi import FastAPI
from pydantic import BaseModel
import requests


class Text(BaseModel):
    content: str


app = FastAPI()


@app.post("/{imageFormat}")
def load(imageFormat: str, body: Text):
    url = "http://plantuml-rodrigogcespedes.cloud.okteto.net/"
    response = requests.post(url + "form", body)
    pInicial = response.text.find(url + imageFormat)
    pFinal = response.text.find("\"", pInicial)
    image = response.text[pInicial:pFinal]
    return {"result": image}
