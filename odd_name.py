def main():
    run = True
    name = input(print("What is your name?:  "))
    get_name(name, run)
    show_name(name)


def show_name(name):
    for a in range(0, 4, 2):
        print(name[a])


def get_name(name, run):
    while run == True:
        if name == '':
            print("Name cannot be blank")
        else:
            run = False