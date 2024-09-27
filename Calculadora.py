class Calculadora:
                            
    def adicao(self, a, b):
        
        return a + b

    def subtracao(self, a, b):
        
        return a - b

    def multiplicacao(self, a, b):
        
        return a * b

    def divisao(self, a, b):
        
        if b == 0:
            return "Erro: Divisão por zero não é permitida."
        return a / b

    def fatorial(self, n):
        
        if n < 0:
            return "Erro: Fatorial de número negativo não é definido."
        if n == 0:
            return 1
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    def potencia(self, base, expoente):
        
        return base ** expoente


if __name__ == "__main__":
    calc = Calculadora()
    
   