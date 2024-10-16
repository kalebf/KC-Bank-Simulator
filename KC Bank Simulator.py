balance = 1000

while True:
    print('Welcome to KC Bank!')
    print()
    print(f'Account balance: ${balance}')
    print()
    print('KC Bank:\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit')

    for counter in range(1, 4):
        menu = int(input('Choose an operation (1-4): '))
        if 0 < menu < 5:
            break
        
        else:
            print('Invalid option. Please enter a number between 1 and 4')
            print(f'You used {counter} attempt(s)')
            
    else:
        break

    if menu == 1:
        deposite = float(input('Enter the deposite amount: '))
        balance += deposite
        print(f'Deposite successful. New balance: ${balance: .2f}')
        print(f'Account balance: ${balance:.2f}')
        print()
        
    elif menu == 2:
        withdraw = float(input('Enter the withdraw amount: '))
        if balance > withdraw:
            balance -= withdraw
            print(f'Withdraw successful. New balance: ${balance: .2f}')
            print(f'Account balance: ${balance:.2f}')
            print()
            
        else:
            print('Error: Insufficient funds. Withdraw amount exceeds the current balance')
            print(f'Account balance: ${balance:.2f}')
            print()
            
    elif menu == 3:
       print(f'Current balance: ${balance: .2f}')
       print(f'Account balance: ${balance:.2f}')
       print()
       
    elif menu == 4:
        print('Exiting Kc Bank. Thank you!')
        break
    
        
