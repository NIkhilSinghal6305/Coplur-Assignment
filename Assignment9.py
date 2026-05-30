# 1) Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array [[6, -8, 73, -110], [np.nan, -8, 0, 94]] 2) Move axes of 3D array to new positions 3) Replace NaN values with average of columns 4) Replace negative value with zero in numpy array using replace

import numpy as np
# 1) Replace NaN with 0 and Interchange 3 rows and 3 columns of 2D array
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr = np.nan_to_num(arr, nan=0)
arr = arr.T
print(arr)


# 2) Move axes of 3D array to new positions
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr_3d = np.transpose(arr_3d, (1, 0, 2))
print(arr_3d)


# 3) Replace NaN values with average of columns
arr_with_nan = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
col_mean = np.nanmean(arr_with_nan, axis=0)
inds = np.where(np.isnan(arr_with_nan))
arr_with_nan[inds] = np.take(col_mean, inds[1])
print(arr_with_nan)


# 4) Replace negative value with zero in numpy array using replace
arr_with_negatives = np.array([[1, -2, 3], [-4, 5, -6], [7, -8, 9]])
arr_with_negatives[arr_with_negatives < 0] = 0
print(arr_with_negatives)
