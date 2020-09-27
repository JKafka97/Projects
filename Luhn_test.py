def Luhn_test(digits):
    reverse_list = digits[::-1]
    odd_list = []
    for my_numer in reverse_list:
        if not my_numer % 2 == 0:
            odd_list.append(my_numer)
        else: continue



