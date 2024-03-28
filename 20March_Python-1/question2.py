#TR 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
#EN 2-Calculate the increased salary of the worker whose salary and increase rate is entered and display it on the screen.

print("\n *** Let's how your new salary is satisfied for you...\n")

salary = float(input("Please enter your monthly salary: \n"))
raise_rate = float(input("Please enter the last salary increase you received: \n"))

current_salary = salary + (salary * (raise_rate / 100))

hr_message = f"Your current salary is: {current_salary}"

print(hr_message)