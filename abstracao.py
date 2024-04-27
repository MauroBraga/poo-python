from abc import ABC, abstractmethod


print("\nExemplo de abstração:")

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self)->None:
        pass

    def ligar(self):
        return "Carro ligado"

    def desligar(self):
        return "carro desligado"

carro = Carro()

print(carro.ligar())
print(carro.desligar())