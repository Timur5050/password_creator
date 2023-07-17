import random

digit = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"


def parol():
    srt = ""
    lst = []
    if nums.lower() == "yes":
        srt += digit
    if upper_letters.lower() == "yes":
        srt += uppercase_letters
    if lower_letters.lower() == "yes":
        srt += lowercase_letters
    if simbols.lower() == "yes":
        srt += punctuation
    for i in range(num):
        s = ""
        for j in range(length):
            s += random.choice(srt)
        lst.append(s)

    return lst


num = int(input("how many paroles do you need? : "))
length = int(input("what is the length of passwords ? : "))
nums = input("Do I include numbers 0123456789 ? (yes/no) : ")
upper_letters = input("Include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ ? (yes/no) : ")
lower_letters = input("Do I include the lowercase letters abcdefghijklmnopqrstuvwxyz ? (yes/no) : ")
simbols = input("Do I include the symbols !#$%&*+-=?@^_ ? (yes/no) :")
print("------------------------------------")
print(parol())
print("------------------------------------")
answer = input("Do you want to repeat ? (yes/no) : ")
while answer.lower() != "no":
    if answer.lower() == "yes":
        num = int(input("how many paroles do you need? : "))
        length = int(input("what is the length of passwords ? (yes/no) : "))
        nums = input("Do I include numbers 0123456789 ? (yes/no) : ")
        upper_letters = input("Include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ ? (yes/no) : ")
        lower_letters = input("Do I include the lowercase letters abcdefghijklmnopqrstuvwxyz ? (yes/no) : ")
        simbols = input("Do I include the symbols !#$%&*+-=?@^_ ? (yes/no) : ")
        print("------------------------------------")
        print(parol())
        print("------------------------------------")
    else:
        answer = input("incorrect answer, Try to write again (yes/ no) ")

print("Thank you, have a nice day")
