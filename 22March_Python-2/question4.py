# EN 4- Write a program that tells the user whether the number entered is a prime number or not.
# TR 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

def primeOrNot(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i ==0:
            return False
    return True
    
number = int(input("Enter a number..: "))
if primeOrNot(number):
    print("it's a prime number")
else:
    print("it's not a prime number")
