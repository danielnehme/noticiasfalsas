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
import streamlit as st

c =  st.container()

col1, col2 = st.columns(2)

# avisos que se repetem ao longo do programa
def falsa():
    with col2:
        st.write("**A notícia pode ser falsa, cuidado!**")

# terceiro nível de ramos da árvore de decisão
def nivel3_nao():
	with col1:
		if st.checkbox("A notícia parece absurda?"): 
			falsa()
		else:
			with col2: 
				st.write("**Na dúvida, não compartilhe!**")

# segundo nível de ramos
def nivel2_sim_1():
	with col1:
		if st.checkbox("A data da publicação é recente?"): 
			with col2:
				st.write("**A notícia provavelmente é verdadeira, mesmo assim, revise para compartilhar.**")
		else: 
			with col2: 
				st.write("**A notícia pode ser verdadeira, mas na dúvida, não compartilhe!**")

def nivel2_sim_2():
	with col1:
		if st.checkbox("É um site de humor ou notícias falsas?"): 
			falsa()
		else: 
			nivel3_nao()

# ramos de primeiro nível
def nivel1_sim():
    with col1:
        if st.checkbox("Outras fontes confiáveis também publicaram?"): 
            nivel2_sim_1()
        else:
            with col2:
                st.write("**Se for verdade, outras fontes confiáveis vão publicar também. Aguarde!**")

def nivel1_nao():
	with col1:
		if st.checkbox("Algum outro site qualquer publicou?"): 
			nivel2_sim_2()
		else: 
			falsa()

# ************ Início do programa - raiz da árvore **************
c.title("\nSISTEMA DE DIAGNÓSTICO DE NOTÍCIAS \n\n")
c.write("*Vamos ver se uma notícia é falsa!*")
c.write("*Para cada questão, marque a que considerar pertinente.*\n\n")

with col1:
	if st.checkbox("A fonte da notícia é confiável?"): 
		nivel1_sim()
	else: 
		nivel1_nao()
# ************ Fim do programa **********************************
