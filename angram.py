def check(s1, s2):
    if s1 == '' and s2 == '':
        print("strings are empty")
    elif s1 == '':
        print("string 1 is  empty")
    elif s2 == '':
        print("string 2 is  empty")
    else:
        if sorted(s1) == sorted(s2):
            print("Two given strings are Anagram")
        else:
            print("Two given strings are not Anagram")


s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

check(s1, s2)
