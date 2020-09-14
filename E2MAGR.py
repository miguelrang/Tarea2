try:
    # Agrgué la librería time, y en la linea 10
    # explico el porque
    import time
    import requests
    import os
    import sys
    from bs4 import BeautifulSoup as bs
    import webbrowser
except:
    # En este caso decidí usar la funcion sleep porque
    # me gusta el aspecto que le da en la terminal al código
    print("Algunas librerias no estan instaladas")
    print("Instalando librerias..")
    time.sleep(3)
    os.system("pip install webbrowser")
    os.system("pip install beautifulsoup4")
    time.sleep(2)
    print("Ejecutando de nuevo el programa...")
    os.system("E2MAGR.py")
# Miguel Angel Guerra Rangel

print("Este script navega en las páginas de noticas de la UANL")
# El codigo pide dos datos de entrada para asi saber de que página a
# que página se va a mover
try:
    while True:
        inicioRango = 0
        finRango = 0
        if inicioRango > 0 or finRango > 0:
            inicioRango = int(input("Pagina inicial para buscar: "))
            finRango = int(input("Pagina final para buscar: "))
            break
        else:
            continue
except:
    inicioRango = 0
    finRango = 0
    print("Solo se aceptan números(enteros)")
    print("Ejecutando de nuevo el programa...")
    time.sleep(2)
    os.system("E2MAGR.py")

dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
# La siguiente condición se encarga de validar que la primera pagina
# sea menor que la segunda debido que no puede ser al reves y en caso
# de que no se cumpla la condición, cambia el valor de las variables
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    # validamos si esa página existe o funciona de manera correcta
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        # Comenzamos a ver contenido de las página donde nos encontramos
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    # Aqui ya comenzamos a revisar que en el contenido de la página
                    # menciona a la facultado que agregamos en un principio
                    if dependencia in elemento.getText():
                        # Si encuentra contenido sobre la dependencia, nos redirecciona
                        # a la página/link donde encontro dicha información
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
