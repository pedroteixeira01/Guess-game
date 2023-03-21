from random import randint

print('#############################')
print('####    guessing game    ####')
print('#############################')

while True:
    
    option = input('''
    Choose the difficulty level:
    1) Easy
    2) Hard
    ''')
    if option == '1':
        
        attempt = 10
        break
    elif option == '2':
        
        print('\nyou will have 3 attempts to hit the number\n')
        attempt = 3
        break
    else:
        
        print('Unexpected option')
num = randint(0, 20)
count = 1
while count <= attempt:

    guess = int(input('Choose a number from 0 to 20 -> '))
            
    if guess < 0 or guess > 20:
        
        print('Out of range number')
        continue
    if guess == num:
        
        print('You got it right!')
        replay = input('Want to play again ?(press y or press another key to exit) ').lower()
        if replay == 'y' or replay == 'yes':
            
            count = 1
            num = randint(0, 20)
        else:
            
            print('Thank you for playing')
            break
    
    elif guess < num:

        print('Guess was less than the number.')
        if attempt > 4:
            attempt += 1
    else:

        print('Guess was greater than the number.')
        if attempt > 4:
            attempt += 1
    count += 1
