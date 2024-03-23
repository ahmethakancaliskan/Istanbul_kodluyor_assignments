# EN 1- Let's write a loop that creates a Fibonacci series as a list with at least 20 elements, the first two elements of which are equal to 1.
# TR 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

def fibonacci(n):  
    a, b = 1, 1
    fibonacci_list = [a, b]
    for i in range(n - 2):  # -2 çünkü ilk iki elemanı zaten mevcut 20 olması için 18 gerek
        a, b = b, a + b     # -2 because the first two elements are already present, 18 is needed to make 20 
        fibonacci_list.append(b)
    return fibonacci_list

print(fibonacci(20))


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

# EN 3- Write a program that finds the GCF and LCM of the number entered by the user.
# TR 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

def ebob(a, b):
    while b: # ne zaman FALSE olursa dur
        a, b = b, a % b
    return a

def ekok(a, b):
    return (a * b) // ebob(a, b)

a = int(input("first_number: "))
b = int(input("second_number: ")) 

print(f"ebob({a}, {b}) = {ebob(a, b)}")
print(f"ekok({a}, {b}) = {ekok(a, b)}")


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



