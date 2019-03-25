def nombreyanopeliculas(datos):
    nombre=[]
    year=[]
    duration=[]
    for i in datos:
        duracion=i["duration"]
        duracion=duracion[2:len(duracion)-1]
        duration.append(duracion)
        nombre.append(i["title"])
        year.append(i["year"])
    combinado=zip(nombre,year,duration)
    return combinado

def nombreyactores(datos):
    nombre=[]
    numactores=[]
    for i in datos:
        nombre.append(i["title"])
        numactores.append(len(i["actors"]))
    combinado=zip(nombre,numactores)
    return combinado

def buscarsinopsis(palabra1,palabra2,datos):
    sinopsis=[]
    for i in datos:
        if palabra1 in i["storyline"] and palabra2 in i["storyline"]:
            sinopsis.append(i["title"])
    return sinopsis

def buscarpeliporactor(actor,datos):
    peliculas=[]
    for i in datos:
        for x in i["actors"]:
            if actor == x:
                peliculas.append(i["title"])
                break
    return peliculas

def sacartrespelis(fecha1,fecha2,datos):
    peliculas=[]
    url=[]
    media=[]
    completa=[]
    suma=0
    cont=0
    for i in datos:
        if i["releaseDate"] >= fecha1 and i["releaseDate"] <= fecha2:
            peliculas.append(i["title"])
            url.append(i["posterurl"])
            for x in i["ratings"]:
                suma=suma+x
                cont=cont+1
            media.append(suma/cont)
            cont=0
            suma=0
    completa=zip(peliculas,url,media)
    return completa


import json
with open("movies.json") as fichero:
	datos=json.load(fichero)

print("Elige una opción: ")
print("1.- Listar el título, año y duración de todas las películas: ")
print("2.- Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una: ")
print("3.- Mostrar las películas que contengan en la sinopsis dos palabras dadas: ")
print("4.- Mostrar las películas en las que ha trabajado un actor dado: ")
print("5.- Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas: ")
print("0.- salir: ")
opcion=int(input("¿opcion?: "))
while opcion >= 0:
    if opcion == 0:
        print("Saliendo del programa.")
        break
    if opcion == 1:
        for i in nombreyanopeliculas(datos):
            print("la película",i[0],"Se estrenó el año",i[1],"con una duracion de",i[2],"minutos")
    if opcion == 2:
        for i in nombreyactores(datos):
            print("La pelicula",i[0],"tiene",i[1],"actores")
    if opcion == 3:
        palabra1=input("Escribe una palabra que contenga la sinopsis: ")
        palabra2=input("Escribe otra palabra que contenga la sinopsis: ")
        resultado= buscarsinopsis(palabra1,palabra2,datos)
        if len(resultado)==0:
            print("No hay coincidencias.")
        else:
            print("Las peliculas que encajan con los palabras dadas son:")
            for i in resultado:
                print(i)
    if opcion == 4:
        actor=input("Escribe el nombre del actor: ")
        resultado=buscarpeliporactor(actor,datos)
        if len(resultado) == 0:
            print("Ese actor no aparece en ninguna pelicula.")
        else:
            print("ese actor aparece en:")
            for i in resultado:
                print(i)
    if opcion == 5:
        fecha1=input("Escribe la primera fecha (ej:. 1992-07-26): ")
        fecha2=input("Escribe la segunda fecha (ej:. 1992-07-26): ")
        resultado=sacartrespelis(fecha1,fecha2,datos)
        resultado=list(resultado)
        resultado.sort(key=lambda nota: nota[2])
        resultado=resultado[len(resultado)-3:]
        if len(resultado)==0:
            print("No hay peliculas en ese rango de fecha.")
        else:
            print("Las peliculas con ese rango de fechas son:")
            for i in resultado:
                print("titulo:",i[0],"Cartel:",i[1])

    print("")
    print("Elige una opción: ")
    print("1.- Listar el título, año y duración de todas las películas: ")
    print("2.- Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una: ")
    print("3.- Mostrar las películas que contengan en la sinopsis dos palabras dadas: ")
    print("4.- Mostrar las películas en las que ha trabajado un actor dado: ")
    print("5.- Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas: ")
    print("0.- salir: ")
    opcion=int(input("¿opcion?: "))
