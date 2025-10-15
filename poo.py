class Paciente:
    def __init__(self, nome_paciente, idade, endereco_paciente, nome_mae):
        self.nome_paciente = nome_paciente
        self.idade = idade
        self.endereco_paciente = endereco_paciente
        self.nome_mae = nome_mae

    def __str__(self):
        return f'Paciente: {self.nome_paciente}, {self.idade} anos, Endereço: {self.endereco_paciente}, Mãe: {self.nome_mae}'

    def getDataNascimento(self):
        return self.idade

    def foiatendido(self, atendido):
        if atendido:
            print(f'O paciente {self.nome_paciente} foi atendido')
        else:
            print(f'O paciente {self.nome_paciente} não foi atendido')


paciente1 = Paciente("Pedro", 33, "Rua Espanha,13", "Ana")
print(paciente1)
print(paciente1.nome_paciente)
print(
    f'A idade do Paciente {paciente1.nome_paciente} é {paciente1.getDataNascimento()}')
print(paciente1.foiatendido(True))
