def main():
    run = True
    name = input(print("What is your name?:  "))
    frequency = input(print("How often would you like a letter to be printed?: "))
    get_name(name, run)
    show_name(name, frequency)


def show_name(name, frequency):
    for a in range(0, 4, frequency):
        print(name[a])


def get_name(name, run):
    while run == True:
        if name == '':
            print("Name cannot be blank")
        else:
            run = False