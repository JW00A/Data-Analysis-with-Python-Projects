import numpy as np

def calculate(list):
    if len(list) == 9:
        np_arr = np.array(list).reshape(3, 3)
    else:
        raise ValueError('List must contain nine numbers.')

    mean1 = np.mean(np_arr, axis=0).tolist()
    mean2 = np.mean(np_arr, axis=1).tolist()
    mean = np.mean(np_arr)

    var1 = np.var(np_arr, axis=0).tolist()
    var2 = np.var(np_arr, axis=1).tolist()
    var = np.var(np_arr)

    std1 = np.std(np_arr, axis=0).tolist()
    std2 = np.std(np_arr, axis=1).tolist()
    std = np.std(np_arr)

    max1 = np.max(np_arr, axis=0).tolist()
    max2 = np.max(np_arr, axis=1).tolist()
    max_flattened = np.max(np_arr)

    min1 = np.min(np_arr, axis=0).tolist()
    min2 = np.min(np_arr, axis=1).tolist()
    min_flattened = np.min(np_arr)

    sum1 = np.sum(np_arr, axis=0).tolist()
    sum2 = np.sum(np_arr, axis=1).tolist()
    sum_flattened = np.sum(np_arr)

    final_dict = {
        'mean': [mean1, mean2, mean],
        'variance': [var1, var2, var],
        'standard deviation': [std1, std2, std],
        'max': [max1, max2, max_flattened],
        'min': [min1, min2, min_flattened],
        'sum': [sum1, sum2, sum_flattened]
    }
    return final_dict