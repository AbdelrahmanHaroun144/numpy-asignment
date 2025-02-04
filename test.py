import numpy as np

# 1. Broadcasting
# a) Add a 1D array to each row of a 2D array
array_2d = np.array([[10, 20, 30], [40, 50, 60]])
array_1d = np.array([1, 2, 3])
result_1a = array_2d + array_1d
print("1a:", result_1a)
print("--------------------------------------------")
# b) Multiply a 2D array by a 1D array column-wise
array_2d_b = np.array([[1, 2], [3, 4]])
array_1d_b = np.array([10, 20])
array_1d_b_reshape=array_1d_b.reshape(-1,1)
result_1b = array_2d_b * array_1d_b_reshape
print("1b:", result_1b)
print("--------------------------------------------")

# 2. Indexing and Slicing
arr = np.arange(1, 25).reshape(2, 3, 4)

# a) Extract the second slice along axis 0
result_2a = arr[1]
print("2a:", result_2a)
print("--------------------------------------------")

# b) Extract all rows and the last column for all slices
result_2b = arr[:, :, -1]
print("2b:", result_2b)
print("--------------------------------------------")

# c) Reverse the order of slices along axis 0
result_2c = arr[::-1]
print("2c:", result_2c)
print("--------------------------------------------")

# d) Set all even elements in the array to -1
arr_even_replaced = np.where(arr % 2 == 0, -1, arr)
print("2d:", arr_even_replaced)
print("--------------------------------------------")

# 3. np.repeat
arr_repeat = np.array([1, 2, 3, 4, 5, 6])

# a) Repeat every odd element twice
result_3a = np.repeat(arr_repeat[arr_repeat % 2 == 1], 2)
print("3a:", result_3a)
print("--------------------------------------------")

# b) Repeat elements based on their value
result_3b = np.hstack([np.repeat(i, i) for i in arr_repeat])
print("3b:", result_3b)
print("--------------------------------------------")

# 4. Normalizing
arr_norm = np.array([10, 20, 30])
result_4a = (arr_norm - arr_norm.min()) / (arr_norm.max() - arr_norm.min())
print("4a:", result_4a)
print("--------------------------------------------")

