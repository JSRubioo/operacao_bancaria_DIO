print("seja bem vindo ao banco")
prox_op = -1
saldo = 0
extrato = ""
limite_de_saque = 500
saque_diario = 3


while prox_op != 0:
 
 print(
  '''
  ------------MENU------------
  
  [1] saque
  [2] depósito
  [3] extrato
  [0] sair

  ----------------------------
  '''
       )

 prox_op = float(input("Informe a operação: "))  
 if prox_op == True:
    saque =  float(input("informe o valor que deseja sacar: "))
    if saque <= limite_de_saque and saque_diario > 0 and saque > 0:
        if saldo >= saque:
            saldo -= saque 
            extrato += f"Saque: R$ {saque: .2f}\n"
            saque_diario -= 1   
        else:
           print("Saldo insuficiente")    
    elif saque > limite_de_saque:
       print("Limite de saque excedido")
    elif saque_diario ==0:
       print("Limite de saque diario excedido")

    else:
       print("Valor invalido")
 elif prox_op == 2:
     deposito = float(input("informe quanto deseja depositar: "))
     if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
     else:
        print("Falha na operação. Valor invalido")
      
 elif prox_op == 3 :
   print("\n","EXTRATO".center(40, "-") )
   print("Não foram realizadas movimentaçoes" if not extrato else extrato)
   print(f"Seu saldo na conta é de: R$ {saldo: 12.2f}")
   print("".center(40,"-")) 
   print(" ")

 elif prox_op == 0:
    break
 else :
   print("Opção invalida\n")
