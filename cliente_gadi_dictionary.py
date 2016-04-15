# -*- coding: utf-8 -*-

import os

print "============================================="
print "Pulse"
print "============================================="
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

else if res == 4:

# else if res == 5:
