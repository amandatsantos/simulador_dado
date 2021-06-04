#simulador de dado
#objetivo é exibir um valor de 1 até 6
from random import  randrange
import time

print("-----DESEJA JOGAR O DADO ?-----\n")
opcao = int(input(" 1- sim   2- não : "))

print("\naguarde um momento... processando\n")
time.sleep(0.5)

if opcao != (1, 2):
    while(opcao):
        opcao= int(input(" opção invalida!\n 1-sim 2-não : "))
if opcao is 1:
    print("correto, você escolheu jogar o dado:) ?\n \n processando ...")
    time.sleep(0.5)

    dado =randrange(1,7)
    print("****dado jogado****")
    time.sleep(0.10)

    print("dado:", dado)
    dado = str(input("jogar novamente aperte '1' "))
    while dado == 1:
        print("****dado jogado****")
        time.sleep(0.10)
        print("dado:", dado)
elif opcao is 2:
    print (" você preferiu não jogar\n Deseja reconsiderar?")
    
""" while opcao != (1 and 2):
    opcao= int(input(" opção invalida!\n 1-sim 2-não : ")) """


