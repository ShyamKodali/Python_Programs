# Sparse Data : Data that has mostly unused having most item values are zero

# Sparse Matrices : 1.CSR [Compressed Sparse Row] - Fast Row Slicing 
#                   2.CSC [Compressed Sparse Column] - Fast Column Slicing


import numpy as np
from scipy.sparse import csr_matrix, csc_matrix

arr = np.array([0,0,0,0,0,1,1,0,2])

print('CSR Matrix application shows the position of elements that are non-zero : ' + str(csr_matrix(arr)))

print('CSR Matrix application to only view data that are non zero : '+str(csr_matrix(arr).data))

print('CSR Matrix application to count non zero : '+str(csr_matrix(arr).count_nonzero()))

oldarr = arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csr_matrix(oldarr).tocsc()
print('Converting from CSR to CSC : ' + str(newarr))

ez_arr = csr_matrix(oldarr)
ez_arr.eliminate_zeros()
print('CSR Matrix application to Eliminate zero : '+str(ez_arr))

sdup = csr_matrix(oldarr)
sdup.sum_duplicates()
print('CSR Matrix application to Eliminate Duplicate Entries : '+str(sdup))