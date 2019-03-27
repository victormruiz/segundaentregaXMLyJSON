from lxml import etree
datos = etree.parse('radares.xml')

def contarradares(datos):
    nombres=datos.xpath("//NOMBRE/text()")
    return nombres

def cantidadradares(datos):
    contar=datos.xpath("//PUNTO_INICIAL/PK/text()")
    numero=len(contar)
    return numero
def carreterasdeprovincias(provincia,datos):
    lista=[]
    carretera=datos.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA/DENOMINACION/text()' % provincia)
    for i in carretera:
        if i not in lista:
            lista.append(i)
    contarradar=datos.xpath('count(//PROVINCIA[NOMBRE="%s"]/CARRETERA/RADAR)' % provincia)
    lista=','.join(lista)
    print("Por la provincia %s pasan las siguientes carreteras: " % provincia, end="")
    for i in lista:
        print(i,end="")
    print(" Y tiene un total de %i radares." % int(contarradar))
def carreteraysusprovincias(carretera,datos):
    provincia=datos.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()' % carretera)
    print("Pasa por:")
    for i in provincia:
        radares=datos.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/PK/text()' % (i,carretera))
        print(i,"y tiene",len(radares), "radares en ese tramo.")

def localizacionderadares(carretera,datos):
    radares=datos.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/PK/text()' % carretera)
    print("Esa carretera tiene",len(radares),"radares.")
    print("Estas son sus localizaciones:")
    latitud=datos.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()' % carretera)
    longitud=datos.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()' % carretera)
    for x, y in zip(latitud, longitud):
        print("http://www.openstreetmap.org/#map=14/%s/%s" % (x,y))


print("Elige una opción: ")
print("1.- Mostrar el nombre de las provincias de las que tenemos información sobre radares: ")
print("2.- Mostrar la cantidad de radares de los que tenemos información: ")
print("3.- Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares: ")
print("4.- Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares: ")
print("5.- Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares: ")
print("0.- salir: ")
opcion=int(input("¿opcion?: "))

while opcion >= 0:
    if opcion== 0:
        print("Saliendo del programa.")
        break
    elif opcion == 1:
        nombres=contarradares(datos)
        nombres=','.join(nombres)
        print("tenemos información de las siguientes provincias: ", end="")
        print(nombres)
    elif opcion == 2:
        contar=cantidadradares(datos)
        print("Tenemos información de un total de",contar,"radares.")
    elif opcion == 3:
        provincia=input("Escribe el nombre de la provincia: ")
        carreterasdeprovincias(provincia,datos)
    elif opcion == 4:
        carretera=input("Escribe la denominacion de la carretera: ")
        carreteraysusprovincias(carretera,datos)
    elif opcion == 5:
        carretera=input("Escribe la denominacion de la carretera: ")
        localizacionderadares(carretera,datos)

    print("")
    print("Elige una opción: ")
    print("1.- Mostrar el nombre de las provincias de las que tenemos información sobre radares: ")
    print("2.- Mostrar la cantidad de radares de los que tenemos información: ")
    print("3.- Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares: ")
    print("4.- Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares: ")
    print("5.- Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares: ")
    print("0.- salir: ")
    opcion=int(input("¿opcion?: "))
