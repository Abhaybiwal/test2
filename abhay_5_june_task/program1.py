# Replace index elements with elements in Other List
def replacelement(list1,list2):
    list3=[list1[i] for i in list2]
    print(list3)

test_list1 = ['Abhay', 'is', 'developer']
test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

replacelement(test_list1,test_list2)