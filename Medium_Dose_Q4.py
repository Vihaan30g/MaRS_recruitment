# Medium dose Q4

import numpy as np

# to extract input data from a text file.
def read_data_from_file(log):
    input_data =  np.genfromtxt(log, delimiter=',', dtype=int)
    return input_data


# Muchiko filter implementation    
def muchiko_filter(data, window_size):
    smoothed_data = []
    
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]  # evaluating window_size number elements
        smoothed_data.append(round(float(sum(window) / window_size),2))  # average (roundede to 2 decimal places)
    
    return smoothed_data


# Sanchiko filter implementation  
def sanchiko_filter(data, window_size):
    smoothed_data = []

    for i in range(len(data) - window_size + 1):
        window = sorted(data[i:i + window_size])
        mid = window_size // 2

        if window_size % 2 == 1:
            median = window[mid]
        else:
            median = (window[mid - 1] + window[mid]) / 2

        smoothed_data.append(median)

    return smoothed_data



# reading data from log.txt
sensor_data = read_data_from_file('log.txt')
window_size = 3   # assuming wondow size to be 3
# sample input: sensor_data = np.array([12, 14, 15, 100, 16, 17, 13, 120, 14, 15])


# Applying all filter combinations
sanchiko_result = sanchiko_filter(sensor_data, window_size)
muchiko_result = muchiko_filter(sensor_data, window_size)
sanchiko_then_muchiko = muchiko_filter(sanchiko_result, window_size)
muchiko_then_sanchiko = sanchiko_filter(muchiko_result, window_size)


# Average deviation between two data sets
def mean_absolute_deviation(original, filtered):
    l = min(len(original), len(filtered))
    ttl_dev = 0

    for i in range(l):
        diff = abs(original[i] - filtered[i])
        ttl_dev += diff

    avg_dev = ttl_dev / l
    return avg_dev


# Print results
print(f"Original Data:{sensor_data}\n")
print(f"Sanchiko Only: {sanchiko_result} , mean abs deviation: {mean_absolute_deviation(sensor_data,sanchiko_result)} \n" )
print(f"Muchiko Only: {muchiko_result}, mean abs deviation: {mean_absolute_deviation(sensor_data,muchiko_result)} \n" )
print(f"Sanchiko then Muchiko: {sanchiko_then_muchiko}, mean abs deviation: {mean_absolute_deviation(sensor_data,sanchiko_then_muchiko)} \n" )
print(f"Muchiko then Sanchiko: {muchiko_then_sanchiko}, mean abs deviation: {mean_absolute_deviation(sensor_data,muchiko_then_sanchiko)} \n" )

