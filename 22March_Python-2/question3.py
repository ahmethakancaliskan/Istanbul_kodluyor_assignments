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