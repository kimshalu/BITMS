import time

# Get the current time in seconds since the epoch (January 1, 1970)
current_time_seconds = time.time()
print("Current time in seconds since the epoch:", current_time_seconds)

# Convert the current time to a readable string
current_time_string = time.ctime(current_time_seconds)
print("Current time in readable string format:", current_time_string)

# Pause the program execution for 2 seconds
print("Pausing program execution for 2 seconds...")
time.sleep(2)
print("Resuming program execution after pause.")

# Measure the execution time of a piece of code
start_time = time.time()
# Your code here
time.sleep(1)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
