"""
TR 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
***
EN 3-Write a program that finds the largest of the three numbers entered by the user and prints the result.
*****
"""
print("\n *** Let's find which number is the biggest among three numbers you'll give \n")
num1 = int(input("Please enter first number.. "))
num2 = int(input("Please enter second number.. "))
num3 = int(input("Please enter third number.. "))

top_num = num1

if num2 > num1 and num2 > num3:
    top_num = num2
    print ("The biggest number is : ", top_num)
elif num3 > num1 and num3 > num2:
    top_num = num3
    print ("The biggest number is : ", top_num)
elif num1 > num2 and num1 > num3:
    print ("The biggest number is : ", top_num)
else:
    print("Please enter only the number or enter different numbers..")