import requests
import pandas as pd

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
    "referer": "https://www.udemy.com/courses/search/?src=ukw&q=python"
}

lista_cursos = []
for p in range(1,11): #pagina = 1

    url_api = "https://www.udemy.com/api-2.0/search-courses/?lang=es&q=python&sort=relevance&src=ukw&skip_price=true&p=" + str(p)

    #print(url_api)

    response = requests.get(url_api, headers=headers)
    data = response.json()

    #<response [200]> -> respuesta correcta.
    #<

    cursos = data["courses"]

    for i in cursos:
        lista_cursos.append({
            "Curso": i["title"],
            "Opiniones": str(i["num_reviews"]),
            "Puntaje": str(i["rating"])

        })
       #print("Curso: "+ i["title"])
       #print("Opiniones: "+ str(i["num_reviews"]))
       #print("Puntuación: "+ str(i["rating"]))
       #print("______________________________________________________________________________")

df = pd.DataFrame(lista_cursos)

print(df.head(50))

print(df.dtypes)
print("---------")

#Cambiar tipo de datos :

df['Opiniones'] = df['Opiniones'].astype(int)
df['Puntaje'] = df['Puntaje'].astype(float)

print("Nuevos tipos de datos ")
print(df.dtypes)

#Guardar Archivo en csv.

#df.to_csv("C:/Users/Net/PycharmProjects/pythonProject/CUARTO NIVEL - WEB SCRAPPING/1UdemyCSVFinal.csv",
#          index=True, sep="|", encoding='utf-8', float_format='%.0f')

