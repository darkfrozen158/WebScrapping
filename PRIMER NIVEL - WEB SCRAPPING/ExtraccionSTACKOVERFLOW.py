import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

# URL SEMILLA
url = 'https://stackoverflow.com/questions'

# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url, headers=headers)

# PARSEO DEL ARBOL CON BEAUTIFUL SOUP
soup = BeautifulSoup(respuesta.text)

contenedor_de_preguntas = soup.find(id="questions") # ENCONTRAR UN ELEMENTO POR ID

lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="question-summary") # ENCONTRAR VARIOS ELEMENTOS POR TAG Y POR CLASE

for i in lista_de_preguntas: # ITERAR ELEMENTO POR ELEMENTO

  # METODO #1: METODO TRADICIONAL
  texto_pregunta = i.find('h3').text # DENTRO DE CADA ELEMENTO ITERADO ENCONTRAR UN TAG
  descripcion_pregunta = i.find(class_='excerpt').text # ENCONTRAR POR CLASE
  descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '').strip()
  print ("Titulo de la pregunta: " + texto_pregunta)
  print ("Descripcion de la pregunta: " + descripcion_pregunta)
  print ()

  #METODO 2 :

for e in lista_de_preguntas:
    elemento_texto_pregunta = e.find('h3') #obtener el H3
    texto_pregunta2 = elemento_texto_pregunta.text
    elemento_texto_pregunta2 = elemento_texto_pregunta.find_next_sibling('div').text #OBTENER EL SIGUIENTE ELEMENTO DESPUES DE H3
    elemento_texto_pregunta2 = elemento_texto_pregunta2.replace('\n', "").replace('\r', "").strip() #LIMPIAR ESPACIOS Y SALTOS DE LINEA.
    print(texto_pregunta2)
    print(elemento_texto_pregunta2)
    print()













