from Models.Passageiro import Passageiro
from Models.Motorista import Motorista
from Models.Corrida import Corrida
from DAO.Motorista_DAO import MotoristaDAO


class MotoristaCLI:
    def __init__(self, motorista_dao):
        self.dao = motorista_dao  # Store the instance of MotoristaDAO

    def menu(self):
        while True:
            opcao = input("Escreva a opção que deseja: \n"
                        "[0] - Sair \n[1] - Criar \n[2] - Ler\n[3] - Atualizar\n[4] - Deletar \n")
            opcao = int(opcao)
            if(opcao == 0):
                break
            if opcao == 1:
                MotoristaCLI.createMotorista(self)
            elif opcao == 2:
                MotoristaCLI.readMotorista(self)
            elif opcao == 3:
                MotoristaCLI.updateMotorista(self)
            elif opcao == 4:
                MotoristaCLI.deleteMotorista(self)

    def createMotorista(self):
        print('Dados do passageiro: ')
        nome = input("Nome: ")
        documento = input("Documento: ")
        passageiro = Passageiro(nome, documento)
        flag = 1
        corridas = []
        index = -1
        while (flag == 1):
            index+= 1
            print('Dados da corrida: ')
            nota = input("Nota: ")
            distancia = input("Distancia: ")
            valor = input("Valor: ")
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.insert(index,corrida)
            flag = int(input("Deseja continuar? [1] sim [0] não"))
        nota = input("Nota: ")
        motorista = Motorista(nota, corridas)

        MotoristaDAO.create(self.dao, motorista)

    def readMotorista(self):
        id = input("Id do motorista: ")
        MotoristaDAO.read_by_id(self.dao, id)


    def updateMotorista(self):
        id = input("Id do motorista: ")
        print('Dados do passageiro: ')
        nome = input("Nome: ")
        documento = input("Documento: ")
        passageiro = Passageiro(nome, documento)
        flag = 1
        corridas = []
        index = -1
        while (flag):
            index += 1
            print('Dados da corrida: ')
            nota = input("Nota: ")
            distancia = input("Distancia: ")
            valor = input("Valor: ")
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.insert(index,corrida)
            flag = int(input("Deseja continuar? [1] sim [0] não"))
        nota = input("Nota do motorista: ")
        motorista = Motorista(nota, corridas)
        motorista = MotoristaDAO.update(self.dao, id, motorista)

    def deleteMotorista(self):
        id = input("Id do motorista: ")
        MotoristaDAO.delete(self.dao, id)
