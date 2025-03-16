def is_list_of_integers(list):
    for number in list:
        if not isinstance(number, int):
            return False
    return True

def sum_list(list):
    sum = 0
    for number in list:
        sum += number
    return sum

def product_list(list):
    product = 1
    for number in list:
        product *= number
    return product

if __name__ == '__main__':
    list = [1,2,3]
    print(is_list_of_integers(list) == True)
    print(sum_list(list) == 6)
    print(product_list(list) == 6)
    print(is_list_of_integers(list) == False)


