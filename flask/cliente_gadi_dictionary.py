# -*- coding: utf-8 -*-

import os

res = -1
while res != 0:
    print "============================================="
    print "Pulse"
    print "============================================="
    print "0. Salir"
    print "1. Buscar Palabra en Gaditano"
    print "2. Buscar Palabra en Castellano"
    print "3. Borrar una entrada del diccionario Ga-Es"
    print "4. Crear nueva entrada"
    print "5. Actualizar entrada"
    print "============================================="

    res = int(raw_input())

    if res == 1:
        print "Introduce una palabra en gaditano: "
        p = raw_input()
        os.system('curl -i http://localhost:5000/ga_es/' + p)

    elif res == 2:
        print "Introduce una palabra en español: "
        p = raw_input()
        os.system('curl -i http://localhost:5000/es_ga/' + p)

    elif res == 3:
        print "Introduce la id de la palabra a borrar: "
        p = raw_input()
        os.system('curl -i -X DELETE http://localhost:5000/palabra/' + p)

    elif res == 4:
        print "Introduce la palabra en castellano: "
        es = raw_input()
        print "Introduce la traducción de " + es + " al gaditano: "
        ga = raw_input()
        palabra = '{"es":"' + es + '", "ga":"'+ga+'"}'

        # curl -i -H "Content-Type: application/json" -X POST -d '{"es":"hola", "ga":"q ase"}' http://localhost:5000/palabras
        orden = 'curl -i -H ' + '"Content-Type: application/json" -X POST -d ' + "'" + palabra + "'" + " http://localhost:5000/palabras"
        os.system(orden)

    elif res == 5:
        print "Introduce la id de la entrada del diccionario a modificar: "
        id = raw_input()
        print "Introduce la palabra en castellano: "
        es = raw_input()
        print "Introduce la traducción de " + es + " al gaditano: "
        ga = raw_input()
        palabra = '{"es":"' + es + '", "ga":"' + ga + '"}'
        # erwol@teseracto:~$ curl -i -H "Content-Type: application/json" -X PUT -d '{"es":"fg", "ga":"ggf"}' http://localhost:5000/palabras/1

        orden = 'curl -i -H ' + '"Content-Type: application/json" -X PUT -d ' + "'" + palabra + "'" + " http://localhost:5000/palabras/" + id
        print orden
        os.system(orden)