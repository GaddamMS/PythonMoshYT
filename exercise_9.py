# Program to convert input phone number to english numbers
phone = input("Enter Phone number : ")

num_to_char = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}


if len(phone) != 10:
    print("Phone number should have 10 digits")

else:
    char = []
    num = ""
    for number in phone:
        char.append(num_to_char.get(number, " - NOT A NUMBER - "))
        num += num_to_char.get(number, " - NOT A NUMBER - ") + " "
    print(char)
    print(num)
