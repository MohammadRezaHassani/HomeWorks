def beautiful_num():
    my_bool=True
    counter = 1
    my_num  = 0
    number=int(input())
    while my_bool:
        my_num +=counter
        if(number_of_divisors(my_num)>number):
            return my_num
        counter +=1


def number_of_divisors(number):
    return len([i for i in range(1,number+1) if number%i==0])

print(beautiful_num())