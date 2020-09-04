class Carro:
   pass


Norte = 'Norte'
Sul = 'Sul'
Leste = 'Leste'
Oeste = 'Oeste'

class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL, LESTE, LESTE: NORTE}

    def __init__(self):
       self.valor = NORTE

    def girar_a_direita_dct(self):
       self.valor = self.rotacao_a_direita_dct [self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_direita_dct [self.valor]

class Motor:
    def __init__(self):
        self.velocidade=0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max (0,self.velocidade)

        if __name__ == '__main__':
            motor = Motor()
            motor.velocidade






#class Direcao:
  #  def __init__(self, direcao, 'Norte', 'Sul', 'Leste', 'Oeste'):

>> >  # Testando motor
>> > motor = Motor()
>> > motor.velocidade
0
>> > motor.acelerar()
>> > motor.velocidade
1
>> > motor.acelerar()
>> > motor.velocidade
2
>> > motor.acelerar()
>> > motor.velocidade
3
>> > motor.frear()
>> > motor.velocidade
1
>> > motor.frear()
>> > motor.velocidade
0










