dict = {'a': '100', 'b': '200', 'c': '300', 'd': '400'}
new_dict = {i: x for x, i in dict.items()}

print(new_dict)
