#!/usr/bin/python

#-*- coding: iso-8859-15 -*-


import httplib
import serial
import time
import os, sys
from string import Template
from datetime import datetime


# Creem la funcio per imprimir a la consola la cadena de temperatura, humitat i temps
def cadenatemphumitat(temperatura, humitat, now):
    print 'Humitat:', temperatura, now
    print 'Temperatura:', humitat, now

def segonacadena(temperatura, humitat):
    print temperatura, humitat

# Creem la funcio de creacio d'arxiu . A l'arxiu li posem de nom lectures.txt
# w: write, escritura. Abre el archivo en modo escritura. Si el archivo
# no existe se crea. Si existe, sobreescribe el contenido.
def creaciotxt():
    archi=open('/home/root/lectures.txt','w')
    archi.close()

# Es crea un arxiu per emmagatzemar la linia que cantara el festival
def creacioapuntadortxt():
     archi=open('/home/root/apuntador.txt','w')
     archi.close()

# Creem la funcio de grabacio amb el parametre d'a per anar afegint linees
def gravartxt():
    archi=open('/home/root/lectures.txt','a')
    s = "Temp: %s Humitat: %s %s" % (temperatura, humitat, now) + '\n'
#    valor = (temperatura, humitat, now)
#    s = str(valor) + '\n'
    archi.write(s)
    archi.close()

# Es crea la funcio de gravacio amb el parametre d'w per sobreescriure cada lectura
def gravarapuntador():
    archi=open('/home/root/apuntador.txt','w')
    t = "La temperatura actual daquesta sala es de %s graus i del %s per cent de humitat relativa." % (temperatura, humitat)
    archi.write(t)
    archi.close()

# Es crea l'arxiu per gravar
creaciotxt()

# Es crea l'arxiu de l'apuntador.txt
creacioapuntadortxt()

# Obrim la conexio al port serie

ser = serial.Serial('/dev/ttyACM0', 9600)
var1 = '00.00a00.00'

# llegim 4 caracters

while 1:

# llegim la trama de 5 en 5 caracters humitat i temperatura  amb un caracter de control
# per ejemple:  a25.0036.50 o 5.0036.50a2 , etc

    entradaPython = ser.read(11)
    print entradaPython

# separem la trama per caracters de entradaPython

    ca0, ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10 = entradaPython

# posem en la variable "now" una funcio de consulta de data que invocarem acompanyant
# les lectures seguents

    now = datetime.now()


    if var1 == entradaPython:
        print 'sense canvis'

    else:

# ordenem els caracters de la trama
# amb la premisa que els dos caracters de la dreta a partir de "a" son la temperatura
# els dos seguents son la humitat.

        # Primera possibilitat amb el caracter de control a la primera posicio: "ann.nnnn.nn"

        if ca0 == 'a':
            temperatura = ca1 + ca2 + ca3 + ca4 + ca5
            humitat = ca6 + ca7 + ca8 + ca9 + ca10
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # Segona possibilitat amb el caracter de control a la segona posicio: "nann.nnnn.n"
        elif ca1 == 'a':
            temperatura = ca2 + ca3 + ca4 + ca5 + ca6
            humitat = ca7 + ca8 + ca9 + ca10 + ca0
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # Tercera possibilitat amb el caracter de control a la tercera posicio: "nnann.nnnn."
        elif ca2 == 'a':
            temperatura = ca3 + ca4 + ca5 + ca6 + ca7
            humitat = ca8 + ca9 + ca10 + ca0 + ca1
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # Quarta possibilitat amb el caracter de control a la quarta posicio: ".nnann.nnnn"
        elif ca3 == 'a':
            temperatura = ca4 + ca5 + ca6 + ca7 + ca8
            humitat =  ca9 + ca10 + ca0 + ca1 + ca2
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # cinquena possibilitat amb el caracter de control a la cinquena posicio: "n.nnann.nnn"
        elif ca4 == 'a':
            temperatura = ca5 + ca6 + ca7 + ca8 + ca9
            humitat =  ca10 + ca0 + ca1 + ca2 + ca3
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # sisena possibilitat amb el caracter de control a la sisena posicio: "nn.nnann.nn"
        elif ca5 == 'a':
            temperatura = ca6 + ca7 + ca8 + ca9 + ca10
            humitat =  ca0 + ca1 + ca2 + ca3 + ca4
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # setena possibilitat amb el caracter de control a la setena posicio: "nnn.nnann.n"
        elif ca6 == 'a':
            temperatura = ca7 + ca8 + ca9 + ca10 + ca0
            humitat =  ca1 + ca2 + ca3 + ca4 + ca5
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # vuitena possibilitat amb el caracter de control a la vuitena posicio: "nnnn.nnann."
        elif ca7 == 'a':
            temperatura = ca8 + ca9 + ca10 + ca0 + ca1
            humitat =  ca2 + ca3 + ca4 + ca5 + ca6
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # novena possibilitat amb el caracter de control a la novena posicio: ".nnnn.nnann"
        elif ca8 == 'a':
            temperatura = ca9 + ca10 + ca0 + ca1 + ca2
            humitat = ca3 + ca4 + ca5 + ca6 + ca7
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # desena possibilitat amb el caracter de control a la desena posicio: "n.nnnn.nnan"
        elif ca9 == 'a':
            temperatura = ca10 + ca0 + ca1 + ca2 + ca3
            humitat = ca4 + ca5 + ca6 + ca7 + ca8
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        # onzena possibilitat amb el caracter de control a la onzena posicio: "nn.nnnn.nna"
        elif ca10 == 'a':
            temperatura = ca0 + ca1 + ca2 + ca3 + ca4
            humitat = ca5 + ca6 + ca7 + ca8 + ca9
            cadenatemphumitat(temperatura, humitat, now)
            gravartxt()
            # print 'Temperatura:', temperatura, now
            # print 'Humitat:', humitat, now

        #dotzena possibilitat. Qualsevol altra cosa que no sigui lo anterior

        else:
            print 'Error de lectura:', entradaPython

        segonacadena(temperatura, humitat)
        gravarapuntador()

#       CREAMOS EL OBJETO JSON
#       reemplazamos los valores en una plantilla

        bodyTemplate = '''{
        "version":"1.0.0",
        "datastreams":[
                {"id":"2", "current_value":"$temperature"}
        ]
        }'''

        template= Template(bodyTemplate)
        bodyContent = template.substitute(temperature=temperatura)
        print bodyContent

#       ENVIEM LA HUMITAT A COSM
#       aqui es necesario poner la key del usuario que tengais a Cosm
#       y subir los datos a vuestro datastream

        headers={"X-PachubeApiKey":"key"}
        connection =  httplib.HTTPConnection('api.pachube.com')
        connection.request('PUT', '/v2/feeds/116210', bodyContent, headers)
        response = connection.getresponse()
        print response.status, response.reason

        bodyTemplate = '''{
        "version":"1.0.0",
        "datastreams":[
                {"id":"1", "current_value":"$humidity"}
        ]
        }'''

        template= Template(bodyTemplate)
        bodyContent = template.substitute(humidity=humitat)
        print bodyContent

#       ENVIEM LA TEMPERATURA A COSM
#       aqui es necesario poner la key del usuario que tengais a Cosm
#       y subir los datos a vuestro datastream

        headers={"X-PachubeApiKey":"key"}


        connection =  httplib.HTTPConnection('api.pachube.com')
        connection.request('PUT', '/v2/feeds/116210', bodyContent, headers)
        response = connection.getresponse()
        print response.status, response.reason


    var1 = entradaPython
