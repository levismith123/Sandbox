"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():

    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            Calculate_Fahrenheit()
        elif choice == "F":
            Calculate_Celcius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


    score = float(input("Enter score: "))
    check_score(score)
    print(score)


def check_score(score):
    if score > 100:
        print("Invalid score")
    elif score > 90 or score == 90:
        print("Excellent")
    elif score > 50 or score == 50:
        print("Passable")
    elif score < 50:
        print("Bad")
    elif score < 0:
        print("Must be positive")
    else:
        print("Error")


def Calculate_Celcius():
    fahrenheit = float(input("Farenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))


def Calculate_Fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))
main()