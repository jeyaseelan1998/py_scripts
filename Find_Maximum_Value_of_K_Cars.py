#################### JEYASEELAN CODE ###############################

def find_sum (list_a):
    '''Gets a list as a argument and return the sum of the given list'''
    sum = 0
    for i in list_a:
        sum += int(i)
    return sum

def find_maximum_price(k, price_list, n):
    maximum_selling_price = 0

    for i in range(k+1):
        list_from_front = find_sum(price_list[0:k-i])   #from the front entrance
        list_from_end = find_sum(price_list[n-i:n])     # from the back endrance

        selling_price = list_from_front + list_from_end 

        if selling_price > maximum_selling_price:
            maximum_selling_price = selling_price
        
    print(maximum_selling_price)

def main():
    #inputs
    k = int(input())
    price_list = input().split()

    n = len(price_list)
    find_maximum_price(k, price_list, n)

# main()

#################### ARUNPRASATH CODE ###############################
# n = int(input())
# cars_value = list(map(int,input().split()))
# val_list = []

# start_val_list =cars_value[:n]
# start_val = 0
# for i in start_val_list:
#     start_val= start_val + i
# val_list.append(start_val)

# end_val_list = cars_value[-n:]
# end_val = 0

# for j in end_val_list:
#     end_val = end_val + j
#     val_list.append(end_val)
# answer = max(val_list)
# list_a = []
# for k in range(1,n):
#     f= cars_value[:k]
#     s= cars_value[-(n-k):]
#     f_s = f+s
#     val_list.append(sum(f_s))
    
# answer = max(val_list)    
# print(answer)