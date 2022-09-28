# API for PlantUML

API that receives a plantUML text and returns a png or svg image url with the generated diagram.

Run using ```docker run -p 9500:9500 -it -d --rm rodrigogcespedes/plantuml-api:0.7```

Generate the diagrams sending a POST request to:
* ```https://API-plantUML-rodrigogcespedes.cloud.okteto.net/png``` in order to get a png image or
* ```https://API-plantUML-rodrigogcespedes.cloud.okteto.net/svg``` in order to get a svg image,

Any of them with the body:
```json
{
  "content": "PLANTUML TEXT HERE"
}
```
In order to ger a response like:
```json
{
  "result": "YOUR DIAGRAM URL HERE"
}
```

Repositorio generado para Junkode, 2022
