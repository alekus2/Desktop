# import random
# import os

# numero_aleatorio=random.randint(1,10)
# chute=input ("Tente adivinhar o numero entre 1 e 10. \n")
# chute=int(chute)
# while True:
#     if chute == numero_aleatorio:
#         print ("Voce ganhou :D")
#         break
#     else:
#         print ("vc errou ,o numero era ",numero_aleatorio)


import csv

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# from pptx import Presentation

# apresentacao = Presentation()

# # editar o ppt 
# slide1 = apresentacao.slides.add_slide(apresentacao.slide_layouts[0]) # slide com titulo e subtitulo
# # slide1 = apresentacao.slides.add_slide(apresentacao.slide_layouts[6]) # slide em branco

# titulo = slide1.shapes.title 
# subtitulo = slide1.placeholders[1]

# titulo.text = "1º Slide do Lira"
# subtitulo.text = "Tamo criando ppt com Python"

# # salvar esse ppt
# apresentacao.save("MeuPPT.pptx")