from math_game import add, mult, resta,div

def game():
    
    while True:
        score = 0
        print('======== Menu ========\n1. Add\n2.mult\n3. resta\n4.div')
        operation = float(input("Choice an operation"))
        num_1 = float(input('Enter first number: '))
        num_2 = float(input('Enter second number: '))
        answer = float(input('Enter you answer: '))
        
        if operation == 1:
            resulta = add(num_1, num_2)
            if resulta == answer:
                score += 1
                print("Correct!!")
            else: 
                print("incorrect")
                break

        if operation ==2:
            resultm = mult(num_1,num_2)
            if resultm == answer:
                score += 1
                print("Correct!!")
            else: 
                print("incorrect")
                break

        if operation ==3:
            resultr = resta(num_1,num_2)
            if resultr == answer:
                score += 1
                print("Correct!!")
            else: 
                print("incorrect")
                break

        if operation ==4:
            resultd = div(num_1,num_2) 
            if resultd == answer:
                score += 1
                print("Correct!!")
            else: 
                print("incorrect")
                break
    print(f"======== Game Over ========\nYou score is{score}\nKeep going!")
    
#num_1=float(input("ingrese un número:"))
#num_2=float(input("ingrese un número:"))
game()
