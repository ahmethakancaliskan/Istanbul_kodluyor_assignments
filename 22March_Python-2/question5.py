# EN 5- Write a program that finds the prime factors of the number entered by the user.
# TR 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

def primeOrNot(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i ==0:
            return False
    return True

def findPrimeFactors(number):
    if number < 2:
        return False
    for i in range(1, number):
        if number % i == 0:
            prime_factors.append(i)
    if primeOrNot(number) == True:
        prime_factors.append(number)        
    print(prime_factors)

prime_factors = []
number = int(input("Enter your number : "))

if findPrimeFactors(number) == False:
    print("invalid number")