from fastapi import FastAPI
from pydantic import BaseModel
import requests


class Text(BaseModel):
    content: str


app = FastAPI()


@app.post("/{imageFormat}") #/png || /svg || /txt
def load(imageFormat: str, body: Text):
    url = "https://plantuml-rodrigogcespedes.cloud.okteto.net/"
    response = requests.post(url+"form", {"text": body.content})
    pInicial = response.text.find(url + imageFormat)
    pFinal = response.text.find("\"", pInicial)
    image = response.text[pInicial:pFinal]
    return {"result": image}

#https://api-rodrigogcespedes.cloud.okteto.net/docs para acceder a la documentacion del endpoint