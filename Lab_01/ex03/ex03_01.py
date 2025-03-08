def tinh_tong_so_chan(lst):
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum += i
    return sum
input_list = input("Nhập dãy số cần tính tổng các số chẵn cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_so_chan(numbers)
print(f"Tổng các số chẵn trong dãy: {tong_chan}")
