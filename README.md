# API for PlantUML

The content of the directory "plantumlapi" is an API that receives a plantUML text and returns a png or svg image url with the generated diagram.

The variable ```url``` contains the direction of the instance of PlantUML that is running, it can be chaged for a local docker imgage of PlantUML or for the currently running official PlantUML web service (not recommended).

Run locally using ```docker run -p 9500:9500 -it -d --rm rodrigogcespedes/plantuml-api:0.7``` to use a local local PlantUML.

Run locally using ```docker run -p 9500:9500 -it -d --rm rodrigogcespedes/plantuml-api:0.9``` to use the cloud PlantUML instance of Junkode.

Generate the diagrams sending a POST request to:
* ```{Instance-URL}/png``` in order to get a png image or
* ```{Instance-URL}/svg``` in order to get a svg image,

Where Instance-URL is ```localhost:9500``` when runing local.

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

Further documentation of the endpoints can be accessed in ```/docs```

Further documentation of PlantUML can found in 

Service created for Junkode, 2022.


# API App2Yaml

The content of the directory "java properties to yaml" is an API that receives the text of an ```application.properties``` java file and returns its equivalent in yaml format.

This project provides an HTTP interface for the javainuse convertion web services. Special greetings to them.

Run locally using ```docker run -p 9550:9550 -it -d --rm rodrigogcespedes/app2yaml:0.1```.

Convert properties files by sending a POST request to:
```{Instance-URL}/png```

Where Instance-URL is ```localhost:9550``` when runing local.

Any of them with the body:
```json
{
  "content": "APPLICATION.PROPERTIES TEXT HERE"
}
```
In order to ger a response like:
```json
{
  "result": "YAML TEXT HERE"
}
```

Further documentation of the endpoints can be accessed in ```/docs```

Service created for Junkode, 2022.
