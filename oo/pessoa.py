class Pessoa:
    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)


    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    Márjorie = Pessoa (nome='Márjorie', idade=2)
    Adriele = Pessoa (nome='Adriele', idade=0)
    Fagner = Pessoa(Márjorie, Adriele,  nome='Fagner')
    print(Pessoa.cumprimentar(Fagner))
    print(Pessoa.cumprimentar(Márjorie))
    print(Pessoa.cumprimentar(Adriele))
    print(id(Fagner))
    print(id(Márjorie))
    print(id(Adriele))
    print(Fagner.cumprimentar())
    print(Fagner.nome)
    print(Fagner.idade)
    for filho in Fagner.filhos:
        print(filho.nome, filho.idade)


