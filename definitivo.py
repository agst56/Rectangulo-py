posibles = ['si', 'no', 'bueno', '', 'yes', 'ok', 'dale']
from math import ceil
def cuadrantes(cuadrante=[],count=1, nombre=0):
    posicion = 'cuadrante '+str(count)
    if count != 10:
        try: nombre += 1
        except: nombre = input('para el '+posicion+' desea: ')
        if rectangulo.espaciohorizontal <= len(str(nombre)):
            print('por favor repite')
            count -= 1
        cuadrante.append((posicion, nombre))
        cuadrantes(cuadrante, count+1, nombre)
    return cuadrante


def ingreso(user, deseo = ''):
    while True:
        try:
            exec(user)
            if deseo == ('si' or 'yes' or 'ok' or 'bueno' or 'dale'):
                rectangulo.centrado()

        except AssertionError:
            print('Desea centrar?')
            deseo = input('')
        except AttributeError: print('por favor, elija una de las opciones')
        except ValueError: print('por favor coloque un numero')
        else:
            break


class Rectangulo:
    def __init__(self):
        self.pantalla = 186
        self.anchor = 4

    def construccion(self):
        try:
            assert 100>self.largor>=4 and 100>self.altura>=6
        except:
            if (self.largor or self. altura) > 100:
                self.largor = 70
                self.altura = 40
            else:
                self.largor = 4
                self.altura = 6
        self.espaciohorizontal = self.largor-2
        self.rayitas =  ('-  '*(self.largor)).rstrip()
        self.espaciados = "{0}{0:>{1}}{0:>{1}}{0:>{1}}".format("'", self.largor-1)

    def centrado(self):
        self.rayitas='{:^{}}'.format(self.rayitas, self.pantalla)
        self.espaciados = '{:^{}}'.format(self.espaciados, self.pantalla)


    def __next__(self):
        #minimo anchor=7
        self.anchor = self.anchor +3
        espacio_de_cuadrante = (self.anchor-4)/3
        #condicion para hallar la 'mitad' de la anchura de un cuadrante
        condicion = espacio_de_cuadrante/2
        #si no hay mitad se considera el mayor
        self.medio_minianchor = ceil(condicion)
        return self.anchor

    def __iter__(self):
        return self

    def default(self):
        self.modo=self.default = dict(cuadrantes())
        return self.modo

    def personalizado(self):
        self.modo=self.personalizado = dict(cuadrantes(nombre='1'))
        return self.modo

    def __setattr__(self, name, value):
        if name == 'peticion':
            self.name = eval(value)
        else:
            self. __dict__[name] = value

    def caracteres(self, desde, hasta):
        largor=self.rayitas.find('-')+1
        informacion = ''
        for triple in range(desde, hasta):
            if triple == desde:
                informacion += "{:>{}}{:^{}}".format("'",largor, modo['cuadrante '+str(triple)], rectangulo.espaciohorizontal)
                continue
            informacion += "{}{:^{}}".format("'", modo['cuadrante '+str(triple)], rectangulo.espaciohorizontal)
        return informacion + "'"

print('Bienvenido a la creacion de su rectangulo con 9 cuadrantes')
rectangulo=Rectangulo()
ingreso("rectangulo.largor = int(input('Largor de su rectangulo: '))" )
ingreso("rectangulo.altura = int(input('Anchor de su rectangulo: '))" )
rectangulo.construccion()

for progresion in rectangulo:
    if abs(progresion-rectangulo.altura)==1 or progresion==rectangulo.altura:
        rectangulo.altura = progresion
        break

print("Sera un rectangulo con ajustes 'default' o 'personalizado'?")
analisis = ("rectangulo.peticion  = 'Rectangulo.' + input('') + '(self)'")
ingreso(analisis)
print("Desea que el rectangulo este 'centrado'?")
deseo = input('')
ingreso('assert '+'deseo'+'.lower()' + ' in posibles', deseo)

#rectangulo.name = rectangulo.peticion
modo = rectangulo.name
#preparacion para la progresion
desde, hasta = (-2,1)
rectangulito=''
count = 0
for i in range(rectangulo.altura):
    count += 1
    if i % (int(rectangulo.altura/3)) == 0:
        rectangulito+='''
'''+rectangulo.rayitas
        count = 0

    elif rectangulo.medio_minianchor == count:
        #progresion
        desde, hasta = desde+3, hasta+3
        rectangulito += '''
'''+rectangulo.caracteres(desde, hasta)

    else:
        rectangulito+='''
'''+rectangulo.espaciados

print(rectangulito)
input("Press <enter>")
