# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.



# Crie uma instância da classe carro.


# Faça o carro "andar" utilizando os métodos da sua classe.


# Faça o carro "parar" utilizando os métodos da sua classe.


class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = ""
        self.modelo = ""
        self.velocidade = 0

    def liga(self):
        self.ligado = True
    
    def desliga(self):
        self.ligado = False
        self.velocidade = 0
    
    def acelera(self, km):
        self.velocidade = self.velocidade+km

    def desacelera(self, km):
        self.velocidade = self.velocidade-km

    def __str__(self) -> str:
        return f'Carro - ligado {self.ligado} - cor {self.cor} - modelo {self.modelo} - velocidade {self.velocidade}'


carro_1 = Carro()
carro_1.liga()
carro_1.acelera(16)
print(carro_1)
carro_1.acelera(30)
print(carro_1)
carro_1.desacelera(10)
print(carro_1)
carro_1.desliga()
print(carro_1)