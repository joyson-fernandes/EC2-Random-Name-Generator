######### EC2 Random Name Generator #############

##### scenario ######

# The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. 
# List these departments as options and if a user puts another department, 
# print a message that they should not use this Name 

import random
import string

# List of allowed departments
allowed_departments = ['Marketing', 'Accounting', 'FinOps']

# Ask user for the number of EC2 instances 
num_instances = int(input('Enter the number of EC2 instances: ')) 

# Ask user for their department name 
department = input('Enter your department name (Marketing, Accounting, FinOps): ')

# Validate the department
if department not in allowed_departments:
    print("You should not use this Name Generator for your department.")
else:
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
