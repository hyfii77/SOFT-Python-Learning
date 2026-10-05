
# Variables in Python

first_name = 'Muhammed Faris'
last_name = ''
country = 'India'
city = 'kochi'
age = 18
is_married = false
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Muhammed Faris',
    'lastname': '',
    'country': 'India',
    'city': 'kochi'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Muhammed Faris', '', 'kochi', 18 , False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('country :', country)
print('Age: ', age)
print('Married: ', is_married)