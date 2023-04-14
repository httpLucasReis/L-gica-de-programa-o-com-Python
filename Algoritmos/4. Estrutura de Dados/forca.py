import os

print('-------------------------------')
print('-- Bem vindo ao jogo da Forca--')
print("-------------------------------\n")

secret_word = "BISCOITO"
wrong_attempts = 0
right_answer_values = ['_', '_', '_', '_', '_', '_', '_', '_',] 
right_answer = False
gibbeted = False

### Laço que mantêm o jogo rodando.
while (not right_answer and not gibbeted):
    print('Dica da palavra: {}\n'.format(right_answer_values))
    print('Total de erros: {}\n\n'.format(wrong_attempts))
    guess = input("Qual é a letra? ")

    if(guess.upper() in secret_word):
        position = 0
        for letter in secret_word:
            if (guess.upper() == letter.upper()):
                print('Encontrei a letra {} na posição {}\n'.format(letter, position+1))
                right_answer_values[position] = guess.upper()
            position += 1
    else:
        wrong_attempts+=1
       
    gibbeted = wrong_attempts == 8
    right_answer = '_' not in right_answer_values
    print(right_answer_values)
    print('Total de erros: {}\n'.format(wrong_attempts))
    os.system('clear') or None

if(right_answer):
    print("Você ganhou!!!")
else:
    print("Você perdeu!!!")

print("fim de jogo")