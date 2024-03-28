# EN 2- Write a program that tells you whether the number it receives from the user is a perfect number or not.
# TR 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.

def findPerfectNumber(number):
    total = 0
    for i in range(1,number):
        if number % i == 0:
            total += i
    if total == number:
        print("it's a perfect number")
    else:
        print("it's not a perfect number")

findPerfectNumber(int(input("Enter a number..: ")))