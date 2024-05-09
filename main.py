import time
###############################
# Desafio Formação Python Dio #
# versão: 0.1                 #
###############################

def main():
    msg = """
            - Banco Dio -
            Bom dia, como podemos ajudar hoje?
            (1) - Depositar
            (2) - Sacar
            (3) - Extrato
            (4) - Sair
        """
    
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    opt = 0
    while opt != 4:
        print(msg)
        print(f"Saldo: {saldo}")
        print("Escolha uma opção : ", end=" ")
        try:
            opt = int(input())

            match opt:
                case 1:
                    saldo = deposito(saldo,extrato)
                case 2:
                    saldo,numero_saques = saque(saldo,extrato,numero_saques,LIMITE_SAQUES,limite)
                case 3:
                    ext(extrato)
                case 4:
                    print("Foi um prazer atende-lo, por favor volte sempre!")
                case _:
                    print("Não encontrei essa opção, por favor selecione dentre as opção disponíveis!")
        except:
              print("Não encontrei essa opção, por favor digite um dos valores numericso acima!")
    # o delay não é necessário para o funcionamento, foi adicionado por questão de UX
        time.sleep(1)

# Função que irá realizar o deposito
def deposito(saldo,lista):
    val = input("Digite o valor a ser depositado: ")
    try:
        v = float(val)
        lista.append("Desposito de R${:.2f}".format(v))
        print("Depositado com sucesso!")
        return saldo + v
    except:
        print("Encerrando a operação. Valor digitado não é compativel, por favor digite números!")
        return saldo

# Função que irá realizar o saque
def saque(saldo,lista,numsaque,limsaque,limitevalor):
    if numsaque < 3 :
        print(f"O Senhor possui {limsaque} saques diario.\n Foram realizados {numsaque}")
        if saldo == 0:
            print("O Senhor não possui saldo, por favor deposite para que possa ser realizado a operação")
            return saldo,numsaque
        else:
            val = input("Digite o valor a ser sacado: ")
            try:
                v = float(val)
                if v > saldo:
                    print("Encerrando operação, valor informado é maior que o saldo.")
                    return saldo,numsaque
                elif v > limitevalor:
                    print("Encerrando operação, valor informado é maior que o limite de saque.")
                    return saldo,numsaque
                else:
                    lista.append("Saque de R${:.2f}".format(v))
                    print("Saque realizado com sucesso!")
                    return saldo - v, numsaque + 1
            except:
                print("Encerrando a operação. Valor digitado não é compativel, por favor digite números!")
                return saldo,numsaque
    else:
        print("O Senhor(a) alcancou o limite de saques diarios, por favor retorne amanhã")
        return saldo,numsaque

# Função que irá mostrar o extrtto
def ext(lista):
    for i in lista:
        print(i)

if __name__ == "__main__":
    main()