from functools import reduce


arr = [x for x in range(10)]
narr = reduce(lambda x,y: x+y, arr)
print(f"Sum of array is {narr}")