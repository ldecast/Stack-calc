import os
from collections import deque

class Graficador:
    from math import factorial, sqrt
    node = -1
    aux2 = deque()
    def __init__(self, entrada, nombre):
        self.pila = deque()
        self.contenido = ''
        self.entrada = entrada
        self.nombre = nombre.replace(" ","").replace("*","x").replace("/","_")
        self.graficar(self.entrada)

    def peek(self,stack):
        if stack:
            return stack[-1]    #retorna el ultimo elemento de la pila
        else:
            return None

    def graficar(self,expresion):
        ruta = str(self.nombre)+'.dot'
        grafo = open(ruta,'w')
        grafo.write('digraph D {\n')
        grafo.write("rankdir=\"LR\";\n")
        grafo.write("node[shape = \"record\"color= \"#17202a\" fillcolor=\"#80cbc4\" style=filled];\n")
        grafo.write("edge[arrowhead=none color = \"white\"];\n")
        
        for i in range(len(expresion)):
            if expresion[i].isdigit() or '[' in expresion[i] or '.' in expresion[i]:
                self.node += 1
                if 'Pow' in expresion[i]:
                    pot1 = expresion[i][expresion[i].index('[')+1:expresion[i].index(',')]
                    pot2 = expresion[i][expresion[i].index(',')+1:expresion[i].index(']')]
                    resultado = float(pot1) ** float(pot2)
                    self.pila.append(resultado)
                    self.contenido += str(expresion[i])+'|'
                    grafo.write(str(self.node) + '[label = \"'+self.contenido+'\"];\n')

                elif 'Fact' in expresion[i]:
                    fact = expresion[i][expresion[i].index('[')+1:expresion[i].index(']')]
                    resultado = self.factorial(float(fact))
                    self.pila.append(resultado)
                    self.contenido += str(expresion[i])+'|'
                    grafo.write(str(self.node) + '[label = \"'+self.contenido+'\"];\n')

                elif 'Sqrt' in expresion[i]:
                    raiz = expresion[i][expresion[i].index('[')+1:expresion[i].index(']')]
                    resultado = self.sqrt(float(raiz))
                    self.pila.append(resultado)
                    self.contenido += str(expresion[i])+'|'
                    grafo.write(str(self.node) + '[label = \"'+self.contenido+'\"];\n')

                else:
                    self.pila.append(expresion[i])
                    self.contenido += str(expresion[i])+'|'
                    grafo.write(str(self.node) + '[label = \"'+self.contenido+'\"];\n')
            
            elif '+' in expresion[i]:
                aux2 =''
                self.node+=1
                grafo.write(str(self.node)+'[label = \"'+self.contenido+'+\"];\n')
                aux = float(self.pila.pop()) + float(self.pila.pop())
                # self.pila.append(aux)  
                # self.node+=1
                # while(self.peek(self.pila)!=None):
                for i in self.pila:
                    aux2 += str(self.peek(self.pila))+'|'
                self.pila.append(aux)
                self.contenido = str(aux)+'|'+str(aux2)
                self.node+=1
                grafo.write(str(self.node) + '[label = \"'+self.contenido+'\"];\n')
            
            elif '-' in expresion[i]:
                aux2 =''
                self.node+=1
                grafo.write(str(self.node)+'[label = \"'+self.contenido+'-\"];\n')
                aux = -float(self.pila.pop()) + float(self.pila.pop())
                # while(self.peek(self.pila)!=None):
                for i in self.pila:
                    aux2 += str(self.peek(self.pila))+'|'
                self.pila.append(aux)
                self.contenido = str(aux)+'|'+str(aux2)
                self.node+=1
                grafo.write(str(self.node) + '[label = \"'+self.contenido+'\"];\n')

            elif '*' in expresion[i]:
                aux2 =''
                self.node+=1
                grafo.write(str(self.node)+'[label = \"'+self.contenido+'*\"];\n')
                aux = float(self.pila.pop()) * float(self.pila.pop())
                for i in self.pila:
                    aux2 += str(self.peek(self.pila))+'|'
                self.pila.append(aux)
                self.contenido = str(aux)+'|'+str(aux2)
                self.node+=1
                grafo.write(str(self.node) + '[label = \"'+self.contenido+'\"];\n')
            
            elif '/' in expresion[i]:
                aux2 =''
                self.node+=1
                grafo.write(str(self.node)+'[label = \"'+self.contenido+'/\"];\n')
                aux = 1/float(self.pila.pop()) * float(self.pila.pop())
                for i in self.pila:
                    aux2 += str(self.peek(self.pila))+'|'
                self.pila.append(aux)
                self.contenido = str(aux)+'|'+str(aux2)
                self.node+=1
                grafo.write(str(self.node) + '[label = \"'+self.contenido+'\"];\n')
            # self.pila.clear()

        for i in range(self.node):
            grafo.write(str(i)+'->'+str(i+1)+'\n')

        grafo.write('}')

        grafo.close()
        pre = ruta[:ruta.index('.dot')]
        os.system('dot -Tpdf \"'+ruta+'\" -o \"Grafico ['+pre+'].pdf\"')
        os.startfile('\"Grafico ['+pre+'].pdf\"')