### Import modules and libraries in Python
# Importing an entire module

import statistics
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = statistics.mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts)

median_failed_attempts = statistics.median(monthly_failed_attempts)
print("median:", median_failed_attempts)

# Importing specific functions from a module
from statistics import mean, median
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts)
median_failed_attempts = median(monthly_failed_attempts)
print("median:", median_failed_attempts)