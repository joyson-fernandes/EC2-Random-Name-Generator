######### EC2 Random Name Generator #############

##### scenario ######
### Several departments share an AWS environment. 
### You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to.
### Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:
# 1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
# 2. Allow the user to input the name of their department that is used in the unique name.
# 3.Generate random characters and numbers that will be included in the unique name.
# 4.Push your code to GitHub and include the link in your LinkedIn write up.

import random
import string


# Ask user for the number of EC2 instances 
num_instances = int(input('Enter the number of EC2 instances: ')) 

# Ask user for their department name 
department = input('Enter your department name: ')
                        
# Generate Random letters and numbers
def generate_name(department):
    random_letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    random_digits = ''.join(random.choices(string.digits, k=2))
# Combine department name, random letters, and random digits
    return f'{department}-EC2-{random_letters}{random_digits}' 

# Generate and print the unique names
print('\nHere are your EC2 instance names:')
for i in range(num_instances):
    unique_name = generate_name(department)
    print(unique_name)

