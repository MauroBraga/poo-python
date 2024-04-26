#POO

# Classe exemplo
class Pessoa:
    def __init__(self,nome,idade) -> None:
        self.nome=nome
        self.idade=idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

pessoa = Pessoa("Mauro",40)
mensagem = pessoa.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Rodrigo", idade=32)
mensagem = pessoa2.saudacao()
print(mensagem)