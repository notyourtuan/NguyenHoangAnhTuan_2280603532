def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập dãy số cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
tuple_result = tao_tuple_tu_list(numbers)
print("List:", numbers)
print("Tuple từ list:", tuple_result)