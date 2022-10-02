idade = input('Digite sua idade: ')
peso = input('digite seu peso: ')
altura = input('Digite sua altura: ')

if int(idade) < 18 or int(peso) < 55 or float(altura) < 1.65:
    print('Nao foi dessa vez soldado...\n voce nao esta apto ao exercito')
else:
    print('PARABENS!!! Voce esta totalmente apto!\nSe prepare solado...')