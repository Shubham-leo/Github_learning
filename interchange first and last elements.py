#Python program to interchange first and last elements in a list
"""Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]"""

def interchange_list(input_list):
    lenth = len(input_list)
    temp = input_list[0]
    input_list[0] = input_list[lenth-1]
    input_list[lenth-1]=temp
    return input_list
def interchange_list(2input_list):
    get = input_list[0],input_list[-1]
    input_list[-1],input_list[0] = get
    print(get)
    return input_list
def interchange_list3(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList
Input = [12, 35, 9, 56, 24]
print(interchange_list3(Input))
