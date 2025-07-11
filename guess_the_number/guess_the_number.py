import random

number = random.randint(1,1000000)
attempts = 0 

while True:
    guess = int(input('Введи число:'))
    attempts += 1
    if guess < number:
        print('загаданое число больше!')
    elif guess > number:
        print("загаданое число меньше!")
    else:
        print(f'Поздравляю! ты угадал число за {attempts} попыток')
        break
