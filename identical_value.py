# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# pseudocode

#create a function to check if the list corresponds to the condition
def checking_same_value (random_list):

# print the random list
    print (f"Given list {random_list}")
    
# check if the first and last number is equal to each other
    if random_list[0] == random_list[-1]:
        return True
    
    else:
        return False

# create a list and print the result 
first_list = [10, 20, 30, 40, 10]
print ("This is", checking_same_value(first_list))

second_list = [75, 65, 35, 75, 30]
print ("This is", checking_same_value(second_list))