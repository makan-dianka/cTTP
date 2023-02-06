def solution(string:str)->str:
    """
    output line by line 
    the words in the parameter
    """
    liste = string.split()
    for word in liste:
        print(word)

def count_frequencies(word:list)->list:
    """
    output a list of integers 
    with the word repeated. 
    in ascending order
    """
    result = []
    test = []
    sort_list = sorted(word)
    for w in sort_list:
        if w not in test:
            counter = sort_list.count(w)
            result.append(counter)
            test.append(w)
    print(result)

def is_bool(a:int, b:int)->bool:
    """
    output true if one of param is 1 
    or sum of params are 1 otherwise output false
    """
    return a == 1 or b == 1 or a + b == 1

def average(table:list)->int:
    "output 0 if param is empty otherwise output mean of param"
    return sum(table) / len(table) if len(table) != 0 else 0

def find_sum_pair(numbers:list, k:int)->list:
    """
    output a list of two integers 
    from the index of the array 
    so the sum of the items is equal to k.
    else output a list with two integer zeros
    """
    pass

find_sum_pair([1, 5, 1, 8, 2], 13)