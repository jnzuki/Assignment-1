# Bad Calculator Program - Not following the correct guidelines

def calc():
    print("1.Add 2.Subtract 3.Multiply 4.Divide")
    choice = input("Choose: ")
    n1 = input("First num: ")
    n2 = input("Second num: ")

    if choice == '1':
        print(float(n1) + float(n2))
    elif choice == '2':
        print(float(n1) - float(n2))
    elif choice == '3':
        print(float(n1) * float(n2))
    elif choice == '4':
        if float(n2) != 0:
            print(float(n1) / float(n2))
    else:
        print("error")


calc()
