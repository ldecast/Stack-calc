import Postfijo
import Solver
import Graficador

class Inicio:
    from os import system
    def __init__(self):
        self.system('cls')
        print("                  ---------------------------------------------------")
        print("                  | Lenguajes formales y de programación Sección A- |\n                  | Luis Danniel Ernesto Castellanos Galindo        |\n                  | Carnet: 201902238                               |\n                  |                   Stack Calc                    |")
        print("                  ---------------------------------------------------")

        print("1. Cargar Archivo")
        print("2. Graficar operación")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        self.inicio(opcion)

    def inicio(self,opcion):
        if opcion=="1":
            fichero = input("Ingrese la ruta del archivo '.lfp'----> ")
            # fichero = "C:\\Users\\luisd\\Desktop\\Practica1\\archivo.lfp"
            self.cargar(fichero)
        elif opcion=="2":
            print("\n")
            entrada =input("Entrada: ")
            postfija = Postfijo.Postfijo().conversion(entrada.split())
            respuesta = Solver.Solver().resolver_post(postfija.split())
            print("Resultado: "+ str(respuesta))
            print("Generando gráfico...\n")
            Graficador.Graficador(postfija.split(),entrada)
            print("Gráfico de la operación graficada!\n")
            salir = input("Ingrese el comando 'exit' para regresar o cualquier tecla para salir:")
            if salir == 'exit':
                Inicio()
        elif opcion=="3":
            self.system('cls')
            print("\nSaliendo...")
            exit()
        else:
            opcion = input("Seleccione una opción valida [1-3]: ")
            self.inicio(opcion)

    def cargar(self,ruta):
        print("Leyendo: ---"+ruta+"---\n")
        try:
            archivo = open(ruta,"r")
            for linea in archivo.readlines():
                if 'IN' in linea:
                    op = linea[linea.index(':')+1:].replace("\n","")
                    postfija = Postfijo.Postfijo().conversion(op.split())
                    respuesta = Solver.Solver().resolver_post(postfija.split())
                elif 'POST' in linea:
                    op = linea[linea.index(':')+1:].replace("\n","")
                    postfija = op
                    respuesta = Solver.Solver().resolver_post(postfija.split())
                elif 'PRE' in linea:
                    op = linea[linea.index(':')+1:].replace("\n","")
                    postfija = op.split()
                    postfija.reverse()
                    respuesta = Solver.Solver().resolver_pref(postfija)
                elif '' in linea:
                    continue
                else:
                    print("La operación debe contener un prefijo válido.")
                print("Operación: "+op+"\nPost: "+str(postfija)+"\nResultado: "+str(respuesta)+"\n")
            archivo.close()
            
        except FileNotFoundError:
            print("El archivo seleccionado no se encuentra. Intente de nuevo")
        input("Presione Enter para continuar...")
        Inicio()

run=Inicio()