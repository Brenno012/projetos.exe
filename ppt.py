import random
from tkinter import *

jogadas = ['pedra', 'papel', 'tesoura']

voce = 0
maq = 0
mensagem = ''

pessoa = 'a'
#função para botões de escolha de jogada
def pedra():
   global pessoa 
   pessoa = jogadas[0]

def papel():
   global pessoa 
   pessoa = jogadas[1]

def tesoura():
   global pessoa
   pessoa = jogadas[2]
#função para o botão de reset
def resetar():
   global voce
   global maq
   voce*=0
   maq*=0
#funções de vitoria e derrota
def ganhou():
   global voce
   voce += 1
   print(mensagem)
   print('computador =', maq, '\n', 'player', "=", voce)

def perdeu():
   global maq
   maq += 1
   print(mensagem)
   print('computador =', maq, '\n','você =', voce)
#função para criar botão para jogar
def comecar():
#mostra as escolhas do player
   if pessoa == jogadas[0]:
      escolha_player['text'] = 'você escolheu pedra'
   elif pessoa == jogadas[1]:
      escolha_player['text'] = 'você escolheu papel'
   elif pessoa == jogadas[2]:
      escolha_player['text'] = 'você escolheu tesoura'
#escolha aleatoria da maquina
   pc = jogadas[random.randint(0,2)]
#permite o uso das variaveis plac e mensagem
   global plac
   global mensagem
#escolhas da maquina
   if pc == jogadas[0]:
      escolha_pc["text"] = 'Pc escolheu pedra'
   elif pc == jogadas[1]:
      escolha_pc["text"] = 'Pc escolheu papel'
   elif pc == jogadas[2]:
      escolha_pc["text"] = 'Pc escolheu tesora'
#resultados possiveis
   if pessoa == pc:
      resultado["text"] = 'empate, vocês escolheram a mesma coisa'
      print('computado =', maq)
      print('Você =', voce)

   elif pessoa == jogadas[0]:
      if pc == jogadas[1]:
         resultado["text"] = "Você perdeu, papel vence de pedra"
         perdeu()
      else:
         resultado["text"] = "Você venceu, pedra vence de tesoura"
         ganhou()

   elif pessoa == jogadas[1]:
      if pc == jogadas[0]:
         resultado["text"] = "Você ganhou, papel vence pedra"
         ganhou()
      else:
         resultado["text"] = "você perdeu, tesoura vence papel"
         perdeu()

   elif pessoa == jogadas[2]:
      if pc == jogadas[0]:
         resultado["text"] = "você perdeu, pedra vence tesoura"
         perdeu()
      else:
         resultado["text"] = "você ganhou, tesoura vence papel"
         ganhou()
#mostra o placar   
   plac = f'''
   Player = {voce}
   Computador = {maq}'''
#atualiza o placar na janela
   placar["text"] = plac
#abrir a janela
tela1 = Tk()
tela1.title('Joken Po')
#nome da janela
titulo = Label(tela1, text='Pedra, Papel, Tesoura',)
titulo.grid(row=1, column=0)
#botões para escolher a jogada (variavel gramaticalmente errada de propósito)
preda = Button(tela1, text='pedra', command=pedra)
preda.grid(row=3, column=0, padx=100, pady=5)

papeu = Button(tela1, text='papel', command=papel)
papeu.grid(row=4, column=0, padx=100, pady=5)

tesora = Button(tela1, text='tesoura', command=tesoura)
tesora.grid(row=5, column=0, padx=100, pady=5)
#botão para fazer a jogada
jogar = Button(tela1, text='jogar', command=comecar)
jogar.grid(row=6, column=0, padx=100, pady=5)
#reseta o placar
reset = Button(tela1, text='resetar', command=resetar)
reset.grid(row=10, column=0)
#mostra o placar e atualiza a cada rodada
placar = Label(tela1, text='')
placar.grid(row=2, column=0)
#mostra o resultado de cada rodada
resultado = Label(tela1, text="Escolha sua jogada e clique em jogar")
resultado.grid(row=9, column=0)
#mostra a escolha do player e da maquina
escolha_player = Label(tela1, text='')
escolha_player.grid(row=7, column=0)
escolha_pc = Label(tela1, text="")
escolha_pc.grid(row=8, column=0)
#mantem a janela aberta
tela1.mainloop()