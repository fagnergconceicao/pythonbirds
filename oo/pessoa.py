class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)


    def cumprimentar(self):
        return f'olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    Fagner.sobrenome = 'Gonzaga'
    Fagner.filhos
    print(Fagner.__dict__)
    print(Márjorie.__dict__)
    print(Adriele.__dict__)
   # Pessoa.olhos=3
    print(Pessoa.olhos)
    print(Fagner.olhos)
    print(Márjorie.olhos)
    print(Adriele.olhos)
    print(id(Pessoa.olhos), id(Fagner.olhos), id(Márjorie.olhos), id(Adriele.olhos))
    print(Pessoa.metodo_estatico(), Fagner.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Fagner.nome_e_atributos_de_classe())






