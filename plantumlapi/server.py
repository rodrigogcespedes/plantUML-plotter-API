import requests
from fastapi import FastAPI
from pydantic import BaseModel
from io import BytesIO


# from numpy import asarray
# from PIL import Image
# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array


class Text(BaseModel):
    content: str


app = FastAPI()


@app.post("/{imageFormat}")  # /png || /svg || /txt
def load(imageFormat: str, body: Text):
    url = "https://plantuml-rodrigogcespedes.cloud.okteto.net/"
    response = requests.post(url + "form", {"text": body.content})
    pInicial = response.text.find(url + imageFormat)
    pFinal = response.text.find("\"", pInicial)
    image = response.text[pInicial:pFinal]
    return {"result": image}


# https://api-rodrigogcespedes.cloud.okteto.net/docs para acceder a la documentacion del endpoint


# @app.post("/bytes/{imageFormat}")  # /png || /svg || /txt
# def load(imageFormat: str, body: Text):
#     url = "https://plantuml-rodrigogcespedes.cloud.okteto.net/"
#     response = requests.post(url + "form", {"text": body.content})
#
#     pInicial = response.text.find(url + imageFormat)
#     pFinal = response.text.find("\"", pInicial)
#     image = response.text[pInicial:pFinal]
#
#     r = requests.get(image)
#     rawimg = ""
#     abytes = ""
#     print("paso1")
#     if r.status_code in range(200, 299):
#         print("paso2")
#         rawimg = BytesIO(r.content)
#         print("paso3")
#         abytes = rawimg.getvalue()
#         print(abytes)
#         print(type(abytes))
#     else:
#         print(f'Something went wrong. Response: {r.status_code}')
#         abytes= "PlantUML Error"
#
#     cadena = abytes.decode('utf-8','ignore')
#     #cadena = str(abytes, 'UTF-32')
#
#     print("paso4")
#
#     return {"result": cadena}

# python -m uvicorn server:app --port 9500 --reload

@app.post("/bytes/{imageFormat}")  # /png || /svg || /txt
def load(imageFormat: str, body: Text):
    r = requests.get("https://plantuml-rodrigogcespedes.cloud.okteto.net/" + imageFormat + "/" + body.content)
    rawimg = ""
    abytes = ""
    if r.status_code in range(200, 299):
        rawimg = BytesIO(r.content)
        abytes = rawimg.getvalue()
        # print(abytes)
        # print(type(abytes))
    else:
        print(f'Something went wrong. Response: {r.status_code}')
        abytes = "PlantUML Error"

    cadena = abytes.decode('utf-8', 'ignore')
    # cadena = str(abytes, 'UTF-32')

    print("paso4")

    return {"result": cadena}
