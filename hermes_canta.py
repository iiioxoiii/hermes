#!/usr/bin/env python

import httplib
import serial
import time
import os, sys
from string import Template
from datetime import datetime


# Creem la funcio per imprimir a la consola la cadena de temperatura, humitat i temps
def cadenatemphumitat(temperatura, humitat, now):
	print 'Temperatura:', temperatura, now
	print 'Humitat:', humitat, now

def segonacadena(temperatura, humitat):
    print temperatura, humitat

# Creem la funcio de creacio d'arxiu . A l'arxiu li posem de nom lectures.txt
# w: write, escritura. Abre el archivo en modo escritura. Si el archivo
# no existe se crea. Si existe, sobreescribe el contenido.
def creaciotxt():
    archi=open('lectures.txt','w')
    archi.close()

# Es crea un arxiu per emmagatzemar la linia que cantara el festival
def creacioapuntadortxt():
     archi=open('apuntador.txt','w')
     archi.close()

# Creem la funcio de grabacio amb el parametre d'a per anar afegint linees
def gravartxt():
    archi=open('lectures.txt','a')
    s = "Temp: %s Humitat: %s %s" % (temperatura, humitat, now) + '\n'
    # valor = (temperatura, humitat, now)
    # s = str(valor) + '\n'
    archi.write(s)
    archi.close()

# Es crea la funcio de gravacio amb el parametre d'w per sobreescriure cada lectura
def gravarapuntador():
    archi=open('apuntador.txt','w')
    t = "La temperatura actual daquesta sala es de %s graus i del %s per cent de humitat relativa." % (temperatura, humitat)
    archi.write(t)
    archi.close()

# Es crea l'arxiu per gravar
creaciotxt()

# Es crea l'arxiu de l'apuntador.txt
creacioapuntadortxt()

# Obrim la conexio al port serie

ser = serial.Serial('/dev/ttyACM0', 9600)
var1 = '0000a'

# llegim 4 caracters

while 1:

# llegim la trama de 5 en 5 caracters humitat i temperatura  amb un caracter de control
# per ejemple:  a2536 o 36a25 o 536a2 ...

	entradaPython = ser.read(5)
	print entradaPython

# separem la trama per caracters de entradaPython

	ca0, ca1, ca2, ca3, ca4 = entradaPython

# posem en la variable "now" una funcio de consulta de data que invocarem acompanyant
# les lectures seguents

   	now = datetime.now()


   	if var1 == entradaPython:
   		print 'sense canvis'

   	else:

# ordenem els caracters de la trama
# amb la premisa que els dos caracters de la dreta a partir de "a" son la temperatura
# els dos seguents son la humitat.

	    # Primera possibilitat : "a...."

		if ca0 == 'a':
			temperatura = ca1 + ca2
			humitat = ca3 + ca4
			cadenatemphumitat(temperatura, humitat, now)
			gravartxt()
			# print 'Temperatura:', temperatura, now
			# print 'Humitat:', humitat, now

	    # Segona possibilitat : ".a..."

		elif ca1 == 'a':
			temperatura = ca2 + ca3
			humitat = ca4 + ca0
			cadenatemphumitat(temperatura, humitat, now)
			gravartxt()
            # print 'Temperatura:', temperatura, now
			# print 'Humitat:', humitat, now

	    # Tercera possibilitat : "..a.."

		elif ca2 == 'a':
			temperatura = ca3 + ca4
			humitat = ca0 + ca1
			cadenatemphumitat(temperatura, humitat, now)
			gravartxt()
			# print 'Temperatura:', temperatura, now
			# print 'Humitat:', humitat, now

	    # Quarta possibilitat : "...a."

		elif ca3 == 'a':
			temperatura = ca4 + ca0
			humitat = ca1 + ca2
			cadenatemphumitat(temperatura, humitat, now)
			gravartxt()

			# print 'Temperatura:', temperatura, now
			# print 'Humitat:', humitat, now

		# Cinquena possiblitat : "....a"

		elif ca4 == 'a':
			temperatura = ca0 +ca1
			humitat = ca2 + ca3
			cadenatemphumitat(temperatura, humitat, now)
			gravartxt()
			# print 'Temperatura:', temperatura, now
			# print 'Humitat:', humitat, now

		# Sisena possiblitat: qualsevol altra cosa que no hagi coincidit

		else:
			 print 'Error de lectura:', entradaPython


        segonacadena(temperatura, humitat)
        gravarapuntador()



       #CREAMOS EL OBJETO JSON
#       reemplazamos los valores en una plantilla

        bodyTemplate = '''{
        "version":"1.0.0",
        "datastreams":[
                {"id":"1", "current_value":"$temperature"}
        ]
        }'''

        template= Template(bodyTemplate)
        bodyContent = template.substitute(temperature=temperatura)
        print bodyContent

#       LO ENVIAMOS A PACHUBE
#       aqui es necesario poner la key del usuario que tengais en pachube
#       y subir los datos a vuestro datastream

        headers={"X-PachubeApiKey":"J5g5W8gLflClYtEA66luoeu6_gSSAKxqWVhDQ2EwWDFscz0g"}
        connection =  httplib.HTTPConnection('api.pachube.com')
        connection.request('PUT', '/v2/feeds/116210', bodyContent, headers)
        response = connection.getresponse()
        print response.status, response.reason

###

        bodyTemplate = '''{
        "version":"1.0.0",
        "datastreams":[
                {"id":"2", "current_value":"$humidity"}
        ]
        }'''

        template= Template(bodyTemplate)
        bodyContent = template.substitute(humidity=humitat)
        print bodyContent

#       LO ENVIAMOS A PACHUBE
#       aqui es necesario poner la key del usuario que tengais en pachube
#       y subir los datos a vuestro datastream

        headers={"X-PachubeApiKey":"J5g5W8gLflClYtEA66luoeu6_gSSAKxqWVhDQ2EwWDFscz0g"}


        connection =  httplib.HTTPConnection('api.pachube.com')
        connection.request('PUT', '/v2/feeds/116210', bodyContent, headers)
        response = connection.getresponse()
        print response.status, response.reason


	var1 = entradaPython




