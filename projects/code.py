# --------------
# Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Create the lists 
new_class = class_1 + class_2
print(new_class)
# Concatenate both the strings
new_class.append('Peter Warden')
new_class.remove('Carla Gentry')

# Append the list
print(new_class)
# Print updated list


# Remove the element from the list

# Print the list



# Create the Dictionary
courses = {"Math":65,"English":70,"History":80,"French":70,"Science":60}
print(courses)
total = sum(courses.values())
print(total)
percentage = (total/500)*100
# Slice the dict and stores  the all subjects marks in variable
print(percentage)

# Store the all the subject in one variable `Total`

# Print the total

# Insert percentage formula

# Print the percentage




# Create the Dictionary
mathematics = dict({"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,
                   "Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75})
topper = max(mathematics,key = mathematics.get)
print(topper)
type(topper)

# Given string
first_name = topper.split()[0]

# Create variable first_name 
last_name = topper.split()[1]
# Create variable Last_name and store last two element in the list
full_name = last_name +" "+ first_name
# Concatenate the string
print(full_name)
# print the full_name
certificate_name = full_name.upper()
# print the name in upper case
print(certificate_name)
# Code ends here


