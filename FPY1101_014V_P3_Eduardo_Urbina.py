import random
import os
os.system('cls')
#v1,v2,v3,v4,v5,v6,v7,v8,v9
def GrabarAuto():
    listaAutos=[]
    tipoA_val=""
    while tipoA_val=="":
        tipoAuto=input("Ingrese El Tipo de Auto:\nAutomovil - Camion - Camioneta - Moto\n>")
        tipoA_val=tipoAuto.replace(" ","")
        if tipoA_val=="":
            print("Tipo de Auto no Valido")

    patenteAuto=""
    while True:
        patenteAuto=input("ingrese la Patente del auto:\n>")
        valPatente=patenteAuto.replace(" ","")
        if len(patenteAuto) > 0 and len(patenteAuto) <= 6:
            break
        elif valPatente=="":
            print('Patente No Valida')
        else:
            print('Patente No Valida')

    marcaAuto=""
    while True:
        marcaAuto=input("Ingrese la Marca del Auto:\n>")
        valMarca=marcaAuto.replace(" ","")
        if len(marcaAuto) < 2 or len(marcaAuto) > 15:
            print("Marca No valida")
        elif valMarca == "":
            print("Marca No valida")
        else:
            break

    precioAuto=0    
    while True:
        try:        
            precioAuto=int(input("Ingrese El Valor del Auto:\n>"))
        except:
            precioAuto=0

        if precioAuto < 5000000:
            print("Valor Invalido")
        else:
            break
    multa=0
    listaMultas=[]
    valorMulta=0
    while True:
        try:
            multa=int(input("Cuantas Multas Tiene?\n>"))
        except:
            multa=-1
        if multa == 0:
            break
        elif multa > 0:   
            for valor in range(multa):      
                try:
                    diaMulta=int(input("Ingrese Dia Multa: "))
                    mesMulta=int(input("Ingrese Mes Multa: "))
                    anioMulta=int(input("Ingrese Año Multa: "))
                except:
                    diaMulta=-1
                    mesMulta=-1
                    anioMulta=-1

                if diaMulta == 0 or diaMulta >31:
                    print("Dia No Valido")
                elif mesMulta == 0 or mesMulta > 12:
                    print("Mes No Valido")
                elif anioMulta > 2024:
                    print("Año No Valido")
                
                fechaMulta=(f"{diaMulta}/{mesMulta}/{anioMulta}")
                Multas={'Valor de la Multa':{valorMulta},
                        'Fecha de la Multa':{fechaMulta}
                }
                listaMultas.append(Multas)
                valor = multa+1
            break

    fechaRegistro=""
    while True:
        print("ingrese la Fecha del Registro del Vehiculo:")
        try:
            diaReg=int(input("Ingrese Dia Registro: "))
            mesReg=int(input("Ingrese Mes Registro: "))
            anioReg=int(input("Ingrese Año Registro: "))
        except:
            diaReg=-1
            mesReg=-1
            anioReg=-1
        if diaReg <= 0 and diaReg >31:
            print("Dia No Valido")
        elif mesReg <= 0 and mesReg >12:
            print("Mes No Valido")
        elif anioReg >= 2024:
            print("Año No Valido")
        else:
            fechaRegistro=(f"{diaReg}/{mesReg}/{anioReg}")
            break
        

    while True:
        nombreDueño=input("ingrese el Nombre del Dueño;\n>")
        valNombre=nombreDueño.replace(" ","")

        if valNombre != "":
            if len(nombreDueño)>3:
                break
        elif valNombre == "":
            print('Nombre No Valido')
        else:
            print('Nombre No Valido')

    runDueño=0
    while True:
        try:
            runDueño=int(input("Ingrese el Run del Dueño:\n>"))
        except:
            runDueño=0
        
        if  runDueño < 1000000:
            print("Rut no Valido")
        elif runDueño > 1000000:
            print("Run Valido")
            break
        
            
    RegAuto={'Dueño':f'{nombreDueño}',
             'Run':f'{runDueño}',
             'Tipo Auto':f'{tipoAuto}',
             'Marca Auto':f'{marcaAuto}',
             'Patente Auto':f'{patenteAuto}',
             'Precio Auto':f'{precioAuto}',
             'Multas':f'{multa}',
             'Valor y Fechas Multas':f'{listaMultas}',
             'Fecha de Registro':f'{fechaRegistro}'}
    
    listaAutos.append(RegAuto)

    return patenteAuto

def buscarAuto(v1):
    while True:
        vPatente=input("ingrese la Patente del Auto:\n>")
        ValPatente=vPatente.replace(" ","")
        if ValPatente=="":
            print("No existe la patente")
        elif vPatente != v1:
            print("No existe la patente")
        else:
            print(listaAutos(e for e in listaAutos if e[{v1}] == vPatente)[0])



listaAutos=[]
patenteAuto=""
emision=random.randrange(1500,3000)
anotaciones=random.randrange(1500,3000)
multas  =random.randrange(1500,3000)

while True:

    try:
        vOpcion=int(input("Bienvenido a la Automotora 'Auto Seguro'\n1)Grabar Datos de Vehiculo.\n2)Buscar Auto por Patente\n3)Imprimir Certificados.\n4)Salir\n>"))
    except:
        print("Caracter No Valido\n")
        vOpcion=-1
    
    if vOpcion == 1:
        GrabarAuto()
    elif vOpcion == 2:
        buscarAuto(patenteAuto)
    elif vOpcion == 3:
        try:
            opcCerti=int(input("Que Certificado desea imprimir?\1)Emision de Contaminantes\n2)Anotaciones Vigentes.\n3)Mutlas\n>"))
        except:
            opcCerti=-1
            
        if opcCerti == 1:
            print(emision)
        elif opcCerti == 2:
            print(anotaciones)
        elif opcCerti == 3:
            print(multas)
    elif vOpcion == 4:
        print("Adios Nos Vemos!\nEduardo Urbina V 1.0")
        break
    elif vOpcion > 4:
        print('Opcion No Valida\n')