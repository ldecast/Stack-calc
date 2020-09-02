from collections import deque

class Solver:
    from math import factorial, sqrt

    resultado = 0
    def resolver_post(self,sufijo):
        pila = deque()
        self.resultado = 0
        for i in range(len(sufijo)):
            if sufijo[i].isdigit() or '.' in sufijo[i] or 'Pow' in sufijo[i] or 'Fact' in sufijo[i] or 'Sqrt' in sufijo[i]:
                if 'Pow' in sufijo[i]:
                    pot1 = sufijo[i][sufijo[i].index('[')+1:sufijo[i].index(',')]
                    pot2 = sufijo[i][sufijo[i].index(',')+1:sufijo[i].index(']')]
                    self.resultado = float(pot1) ** float(pot2)
                    pila.append(self.resultado)
                elif 'Fact' in sufijo[i]:
                    fact = sufijo[i][sufijo[i].index('[')+1:sufijo[i].index(']')]
                    self.resultado = self.factorial(float(fact))
                    pila.append(self.resultado)
                elif 'Sqrt' in sufijo[i]:
                    raiz = sufijo[i][sufijo[i].index('[')+1:sufijo[i].index(']')]
                    self.resultado = self.sqrt(float(raiz))
                    pila.append(self.resultado)
                else:
                    pila.append(sufijo[i])
            elif '+' in sufijo[i]:
                self.resultado = float(pila.pop()) + float(pila.pop())
                pila.append(self.resultado)
            elif '-' in sufijo[i]:
                self.resultado = - float(pila.pop()) + float(pila.pop())
                pila.append(self.resultado)
            elif '*' in sufijo[i]:
                self.resultado = float(pila.pop()) * float(pila.pop())
                pila.append(self.resultado)
            elif '/' in sufijo[i]:
                self.resultado = 1/float(pila.pop()) * float(pila.pop())
                pila.append(self.resultado)
        return self.resultado

    def resolver_pref(self,sufijo):
        pila = deque()
        self.resultado = 0
        for i in range(len(sufijo)):
            if sufijo[i].isdigit() or '.' in sufijo[i] or 'Pow' in sufijo[i] or 'Fact' in sufijo[i] or 'Sqrt' in sufijo[i]:
                if 'Pow' in sufijo[i]:
                    pot1 = sufijo[i][sufijo[i].index('[')+1:sufijo[i].index(',')]
                    pot2 = sufijo[i][sufijo[i].index(',')+1:sufijo[i].index(']')]
                    self.resultado = float(pot1) ** float(pot2)
                    pila.append(self.resultado)
                elif 'Fact' in sufijo[i]:
                    fact = sufijo[i][sufijo[i].index('[')+1:sufijo[i].index(']')]
                    self.resultado = self.factorial(float(fact))
                    pila.append(self.resultado)
                elif 'Sqrt' in sufijo[i]:
                    raiz = sufijo[i][sufijo[i].index('[')+1:sufijo[i].index(']')]
                    self.resultado = self.sqrt(float(raiz))
                    pila.append(self.resultado)
                else:
                    pila.append(sufijo[i])
            elif '+' in sufijo[i]:
                self.resultado = float(pila.pop()) + float(pila.pop())
                pila.append(self.resultado)
            elif '-' in sufijo[i]:
                self.resultado = float(pila.pop()) - float(pila.pop())
                pila.append(self.resultado)
            elif '*' in sufijo[i]:
                self.resultado = float(pila.pop()) * float(pila.pop())
                pila.append(self.resultado)
            elif '/' in sufijo[i]:
                self.resultado = float(pila.pop()) / float(pila.pop())
                pila.append(self.resultado)
        return self.resultado