
import cv2 # Biblioteca de manipulação de imagens de forma mais eficiente 
import os

def transformar_desenho(arquivo, qtde_filtro):# Função que irá transformar todas as imagens contidas na pasta img em desenho ,recebendo como parametro o arquivo e a qauntidade de filtro

    imagem = cv2.imread(f"img/{arquivo}")# Variavel para a imagem , logo depois  ler essa imagem especificando o local
    imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)# Variavel da imagem em preto em branco, cvtColor é uma função de conversão as cores de uma imagem
    imagem_invertida = cv2.bitwise_not(imagem_pb)#Inverter as cores da imagem 
    imagem_blur = cv2.GaussianBlur(imagem_invertida, (qtde_filtro, qtde_filtro), 0)# aplicar a variavel da imagem,dupla com a quantidade de filto largura e altura,
    #somente com números positivos e ímpares(Kernel_size) e a Sigma X, que é um desvio padrão
    imagem_blur_invertida = cv2.bitwise_not(imagem_blur)#Inverter a imagem blur 
    imagem_desenho = cv2.divide(imagem_pb, imagem_blur_invertida, scale=256.0)#Dividir a imagem preto e branco pela blur invertida,

    cv2.imwrite(f"img_tratado/{arquivo}", imagem_desenho)#Salvar a imagem na pasta 

lista_arquivos = os.listdir("img")#listando os arquivos para transformar todos eles

for arquivo in lista_arquivos:
    transformar_desenho(arquivo, 55)