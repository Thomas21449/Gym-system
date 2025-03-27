def main():

   soma=0
   dias=0
   maior=-10000
   menor= 10000
   while True:
       temperatura = float(input(f' Temperatura (dia {dias}):'))
       soma+=temperatura
       if temperatura > maior:
           maior = temperatura
       if temperatura < menor:
           menor = temperatura
       dias+=1
       if dias == 8:
           break
   print(f'A media de temperatura foi de: {soma/7}C°')
   print(f'A temeratura foi de: {maior}C°')


if __name__ == '__main__':
    main()