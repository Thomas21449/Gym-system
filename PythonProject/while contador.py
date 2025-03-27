'''def main():
    valor = -1
    while valor <1 or valor >10:
        valor = int(input("Digite um valor: "))

if __name__=='__main__':
    main()'''

'''def main():

    while True:
        valor = int(input("informe um valor positivo:"))
        if valor>0 and valor<=10:
           break
           print(valor)

if __name__=='__main__':
    main()'''

def main():

   import random

   sorteio = random.randint(1,10)

   valor=0
   while valor!=sorteio:
       valor = int(input("Digite um valor: "))
       if valor==sorteio:
           print("voce acertou")
           break
       else:
           print("voce errou")

if __name__=='__main__':
    main()
