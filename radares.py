from lxml import etree
datos = etree.parse('radares.xml')

def contarradares(datos):
    nombres=datos.xpath("//NOMBRE/text()")
    return nombres

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
        

    print("")
    print("Elige una opción: ")
    print("1.- Mostrar el nombre de las provincias de las que tenemos información sobre radares: ")
    print("2.- Mostrar la cantidad de radares de los que tenemos información: ")
    print("3.- Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares: ")
    print("4.- Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares: ")
    print("5.- Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares: ")
    print("0.- salir: ")
    opcion=int(input("¿opcion?: "))
