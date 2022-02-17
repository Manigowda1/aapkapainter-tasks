''' Write a code that prints out the first occurrence of a duplicate in a given array of integers
    Sample Input: [1,2,3,2,1]
    Output: 2'''


def first_ocr_of_dup(L):
    l_s = [x for x in L if L.count(x) >= 2]
    print(f"first occurrence of a duplicate elements :{set(l_s)}")


L = list(map(int, input("Enter elements of list with space : ").strip().split()))

first_ocr_of_dup(L)

'''Output sample
Enter elements of list with space : 1 2 2 3 1
first occurrence of a duplicate elements :{1, 2}'''