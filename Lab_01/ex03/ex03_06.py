def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return dictionary
    else:
        return False
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print(f"Dictionary sau khi xóa phần tử có key là '{key_to_delete}':", result)
else:
    print(f"Key '{key_to_delete}' không tồn tại trong dictionary.")