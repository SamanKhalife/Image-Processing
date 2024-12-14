import numpy as np
f = np.array([[128, 55],
              [80, 100],
              [69, 124]])
vector_column_first = f.flatten(order='C')
print("first : ")
print(vector_column_first)
vector_column_second = f.flatten(order='F')
print("second : ")
print(vector_column_second)