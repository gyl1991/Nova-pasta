# passo a passo do projeto:
# 1 - entrar no sistema da empresa:
#     https://dlp.hashtagtreinamentos.com/python/intensivao/login;
# 2 - fazer login;
# 3 - importar a base de dados;
# 4 - cadastrar 1 produto;
# 5 - repetir o cadastro para todos os produtos;

import pyautogui
import time
pyautogui.PAUSE = 0.2
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(3)

pyautogui.click(x=437, y=66)

link = ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

pyautogui.write(link)
pyautogui.press('enter')

time.sleep(2)
pyautogui.click(x=557, y=405)
time.sleep(2)
email = ('gylloureiro@gmail.com')
pyautogui.write(email)
pyautogui.press('tab')
senha = ('12345')
pyautogui.write(senha)
pyautogui.press('enter')

import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=503, y=289)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, "tipo"]
    categoria= tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]


    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(400000)