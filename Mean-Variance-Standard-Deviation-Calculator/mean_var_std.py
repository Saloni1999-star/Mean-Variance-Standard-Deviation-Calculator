import numpy as np

def calculate(lst):
    try:
        # Convert list into 3x3 matrix
        num_array = np.array(lst).reshape(3, 3)

        # Calculate mean
        mean_row = num_array.mean(axis=0).tolist()
        mean_col = num_array.mean(axis=1).tolist()
        mean_val = num_array.mean()

        # Calculate variance
        vari_row = num_array.var(axis=0).tolist()
        vari_col = num_array.var(axis=1).tolist()
        variance = num_array.var()

        # Calculate standard deviation
        sd_row = num_array.std(axis=0).tolist()
        sd_col = num_array.std(axis=1).tolist()
        sd = num_array.std()

        # Calculate max
        max_row = num_array.max(axis=0).tolist()
        max_col = num_array.max(axis=1).tolist()
        maximum = num_array.max()

        # Calculate min
        min_row = num_array.min(axis=0).tolist()
        min_col = num_array.min(axis=1).tolist()
        minimum = num_array.min()

        # Calculate sum
        sum_row = num_array.sum(axis=0).tolist()
        sum_col = num_array.sum(axis=1).tolist()
        sum_val = num_array.sum()

        # Return results as a dictionary
        calculation = {
            'mean': [mean_row, mean_col, mean_val],
            'variance': [vari_row, vari_col, variance],
            'standard deviation': [sd_row, sd_col, sd],
            'max': [max_row, max_col, maximum],
            'min': [min_row, min_col, minimum],
            'sum': [sum_row, sum_col, sum_val]
        }
        return calculation
    except ValueError:
        print('List must contain nine numbers.')
