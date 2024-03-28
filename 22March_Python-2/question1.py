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