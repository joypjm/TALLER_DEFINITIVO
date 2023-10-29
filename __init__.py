from operations import subtract
def game():
    score = 0
    while True:
        print('======== Menu ========'
              '\n1. Subtract'
              '\n0. Exit')
        option = int(input('\nChoose an option: '))
        if option == 0:
            break
        num_1 = input('Enter first number: ')
        num_2 = input('Enter second number: ')
        answer = int(input('Enter your answer: '))
        if option == 1:
            result = subtract(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
    
    print(f'======== Game Over ========'
          f'\nYour score is {score}'
          '\nKeep going!')

game()
