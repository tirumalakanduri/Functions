def palindrome(string):
    if string == string[::-1]:
        print("given string is palindrome")
    else:
        print("given string is not a palindrome")
string = input("enter the string : ")
print(palindrome(string))