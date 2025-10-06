#coding: utf-8
'''
 ******************************************************
 Exemplo de IA simbólica para o blog 
 https://inteligenciasemantica.wordpress.com/

 Sistema de diagnóstico para verificar se uma
 notícia é falsa. Implementa a árvore de 
 decisão apresentada no post.

 Autor: Daniel Nehme Muller
 Data: 05/06/2018

 Esta obra está licenciada com uma Licença 
 Creative Commons Atribuição 4.0 Internacional: 
 https://creativecommons.org/licenses/by/4.0/deed.pt_BR
 ******************************************************
'''
# avisos que se repetem ao longo do programa
def falsa():
  print("\nA notícia pode ser falsa, cuidado!")

def aviso():
  print("\nComece novamente e digite apenas 's' ou 'n'.")

# terceiro nível de ramos da árvore de decisão
def nivel3_nao():
  r3 = input("A notícia parece absurda?")
  if(r3 == 's'): falsa()
  elif(r3 =='n'): 
    print("\nNa dúvida, não compartilhe!")
  else: aviso() 

# segundo nível de ramos
def nivel2_sim_1():
  r21 = input("A data da publicação é recente?")
  if(r21 == 's'): print("\nA notícia provavelmente é verdadeira, mesmo assim, revise para compartilhar.")
  elif(r21 =='n'): print("\nA notícia pode ser verdadeira, mas na dúvida, não compartilhe!")
  else: aviso() 

def nivel2_sim_2():
  r22 = input("É um site de humor ou notícias falsas?")
  if(r22 == 's'): falsa()
  elif(r22 =='n'): nivel3_nao()
  else: aviso()

# ramos de primeiro nível
def nivel1_sim():
  r11 = input("Outras fontes confiáveis também publicaram?")
  if(r11 == 's'): nivel2_sim_1()
  elif(r11 =='n'): print("\nSe for verdade, outras fontes confiáveis vão publicar também. Aguarde!")
  else: aviso() 

def nivel1_nao():
  r12 = input("Algum outro site qualquer publicou?")
  if(r12 == 's'): nivel2_sim_2()
  elif(r12 =='n'): falsa()
  else: aviso() 

# ************ Início do programa - raiz da árvore **************
print("\nSISTEMA DE DIAGNÓSTICO DE NOTÍCIAS \n\n")
print("Vamos ver se uma notícia é falsa! \n")
print("Para cada questão, digite 's' para sim e 'n' para não. \n\n")

resp = input("A fonte da notícia é confiável?")
if(resp == 's'): nivel1_sim()
elif(resp =='n'): nivel1_nao()
else: aviso() 
# ************ Fim do programa **********************************