#Generador de Soluciones

from random import randint


print("Bienvenido al Calculador de Temperaturas \n Seleccione una opcion del Menú ")
menu= int(input("Menu \n 1- Generar Temperaturas Aleatorias Julio 2022. \n 2- Conocer cantidad de temperaturas generadas. \n 3- Ingresar una temperatura manualmente. \n 4- Encontrar Temperatura Máxima. \n 5- Encontrar Temperatura Mínima. \n 6- Mostrar Temperaturas Menores de 20 Grados. \n 0- Salir. "))
temperatura= [randint(0, 45)for _ in range(31)]

while menu != 0:
      if menu == 1:
        calor = temperatura
        print("Las temperaturas medias de Julio Fueron: ", calor)
        
      elif menu == 2:
        saber= len(temperatura)
        print("Se tomaron ", saber, " Mediciones de temperatura ")
        
      elif menu == 3:
        agrega= int(input("Ingrese una nueva temperatura a la lista "))
        sumar_temp= temperatura.append(agrega) 
        print("Se agregó ", agrega, "a la los valores de temperaturas ", temperatura)
        
      elif menu == 4:
        maxima = max(temperatura)
        print("La temperatura maxima es ", maxima)
        
      elif menu == 5:
        minima= min(temperatura)
        print("La temperatura minima es ", minima)
        
      elif menu == 6:
          ordenada= sorted(temperatura)
          for x in ordenada:
              if x < 21:
                print("Los valores de menos de 20 Grados son: ", x)
        
      else:
         print("***Seleccione una opcion correcta***")

      menu= int(input("Menu \n 1- Generar Temperaturas Aleatorias Julio 2022. \n 2- Conocer cantidad de temperaturas generadas. \n 3- Ingresar una temperatura manualmente. \n 4- Encontrar Temperatura Máxima. \n 5- Encontrar Temperatura Mínima. \n 6- Mostrar Temperaturas Menores de 20 Grados. \n 0- Salir. "))

 

        
