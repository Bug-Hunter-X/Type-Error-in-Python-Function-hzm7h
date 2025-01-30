def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, int) and isinstance(b, str):
        return a + int(b)
    elif isinstance(a, str) and isinstance(b, int):
        return int(a) + b
    else:
        return "Invalid input types"

result = function(5, '10')
print(result)
result = function(5,10)
print(result)
result = function('5','10')
print(result) 