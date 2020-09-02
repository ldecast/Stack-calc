from collections import deque

class Postfijo:
    pila = deque()
    salida = deque()

    def peek(self,stack):
        if stack:
            return stack[-1]    # retorna el ultimo elemento de la pila
        else:
            return None

    def conversion(self,expresion):
        self.salida.clear()
        for i in range(len(expresion)):
            if expresion[i].isdigit() or '[' in expresion[i] or '.' in expresion[i]:
                self.salida.append(expresion[i])

            elif expresion[i]=='(':
                self.pila.append(expresion[i])

            elif expresion[i]==')':
                while(self.peek(self.pila)!=0 and self.peek(self.pila)!='('):
                    self.salida.append(self.pila.pop())
                self.pila.pop()

            elif expresion[i]=='+' or expresion[i]=='-' or expresion[i]=='*' or expresion[i]=='/':
                while(self.prioridad_operacion(self.peek(self.pila)) >= self.prioridad_operacion(expresion[i]) and self.peek(self.pila)!=0):
                    self.salida.append(self.pila.pop())
                else:
                    self.pila.append(expresion[i])
        while True:
            try:
                self.salida.append(self.pila.pop())
            except IndexError:
                self.pila.clear()
                break
        return(' '.join(self.salida))

    def prioridad_operacion(self, op):
        if op == '*':
            prioridadop = 2
            return prioridadop
        elif op == '/':
            prioridadop = 2
            return prioridadop
        elif op == '+':
            prioridadop = 1
            return prioridadop
        elif op == '-':
            prioridadop = 1
            return prioridadop
        elif op == '':
            prioridadop = 0
            return prioridadop
        return 0