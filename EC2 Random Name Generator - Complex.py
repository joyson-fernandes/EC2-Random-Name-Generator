######### EC2 Random Name Generator #############

##### scenario ######
#### Turn the foundation and advance python script into a Function and execute the Function. #####


import random
import string

def ec2_name_generator():
    # List of allowed departments
    allowed_departments = ['Marketing', 'Accounting', 'FinOps']

    # Ask user for the number of EC2 instances 
    num_instances = int(input('Enter the number of EC2 instances: '))

    # Ask user for their department name 
    department = input('Enter your department name (Marketing, Accounting, FinOps): ')

    # Validate the department
    if department not in allowed_departments:
        print("You should not use this Name Generator for your department.")
        return  # Exit the function if the department is not allowed

    # Generate Random letters and numbers
    def generate_name(department):
        random_letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        random_digits = ''.join(random.choices(string.digits, k=2))
        # Combine department name, random letters, and random digits
        return f'{department}-EC2-{random_letters}{random_digits}' 


    # Generate and print the unique names
    print('\nHere are your EC2 instance names:')
    for _ in range(num_instances):
        unique_name = generate_name(department)
        print(unique_name)

# Execute the function to verify that it works
ec2_name_generator()
