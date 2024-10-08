#RoadMap Projeto

# 1 -> Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar 1 tecla
#pyautogui.click -> clicar em algum lugar da tela
#pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3

#abrir navegador (chrome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=706, y=752)
time.sleep(0.5)
pyautogui.click(x=1294, y=31)
pyautogui.click(x=967, y=67)

# entrar no link

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("tab")

#fazer login

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("AUSTRONAUTA123!!!!!yyy")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)

#importar base de dados

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

#Cadastrar um produto

for linha in tabela.index:
    #clicar no campo de codigo
    pyautogui.press("tab")

    #pegar da tabela valor do campo que a gente quer preencher

    codigo = tabela.loc[linha, "codigo"]

    #preencher o campo
    pyautogui.write(str(codigo))

    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    #dar scroll de tudo pra cima

    pyautogui.scroll(5000)
    pyautogui.click(x=831, y=222)

    #Repetir o processo
