dishes = {'eggs': 2, 'sausage': 20, 'bacon': 1, 'carrot': 0}

total = sum(dishes.values())
print(total)

max_value = max(dishes, key=dishes.get)
print(max_value)

