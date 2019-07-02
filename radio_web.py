'''import random
import webbrowser
lista =[1,2,3,4]
escolha = ""
print("""     MENU ESTAÇÕES

          1. Rádio Central AM
          2. Rádio Nova Brasil FM
          3. Rádio UNIARA FM
          4. Pagode dos anos 90
          5. Rádio BRASIL FM (12:00)
                                     """ )

x = (input('Escolha sua rádio ou [A] para aleatório: ' ))

if x == 'a' or x == 'A':
   x = escolha
   escolha = random.choice(lista)  
if x == '1' or  escolha == 1:
   webbrowser.open('www.radiosaovivo.net/central/')
if x == '2' or  escolha == 2:
    webbrowser.open('http://www.novabrasilfm.com.br/live/1')
if x == '3' or  escolha == 3:
    webbrowser.open('https://tudoradio.com/player/radio/1277')

if x == '4' or  escolha == 4:
     webbrowser.open('https://www.kboing.com.br/playlist/1-48438_1038728_300288_43558_1002188_300316_43324_42750_70030_42525_44039_300317_70041_1054394_43085_1009434_60136_300285_1021572_44080_43311_1054943_1058093_41620_43123_43544_1058096_50750_43576_43515_1012519/')
     
if x == '5' or escolha == 5:
   webbrowser.open('https://www.guiademidia.com.br/ouvir/sp/radio-brasil-am-1270-campinas.htm')
 