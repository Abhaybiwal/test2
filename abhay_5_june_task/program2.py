# Retain records with N occurrences of K
def retainrecord(input_list,K,N):
    ans = list(filter(lambda x: x.count(K) == N, input_list))
    print(ans)

test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 2 
retainrecord(test_list,K,N)

test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 3 

retainrecord(test_list,K,N)