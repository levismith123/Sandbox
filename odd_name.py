run = True
name = input(print("What is your name?:  "))
while run == True:
    if name == '':
        print("Name cannot be blank")
    else:
        run = False
for a in range (0,4,2):
    print(name[a])