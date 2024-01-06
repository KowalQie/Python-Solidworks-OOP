# Open .txt file to input variable
f = open('dimensions.txt', 'w+')

# Ask user for input:
# Assign input values to variables
base_diameter = input('Base_diameter: ')
end_diameter = input('End_diameter: ')
height = input('Height: ')
end_extrusion = input('End_extrusion: ')
base_extrusion = input('Base_extrusion: ')
number_of_rotor_blades = input('Number_of_rotor_blades: ')

# Write to .txt file
# Place user input in .txt file
f.write(f'base_diameter = {base_diameter} \n')
f.write(f'end_diameter = {end_diameter} \n')
f.write(f'height = {height} \n')
f.write(f'end_extrusion = {end_extrusion} \n')
f.write(f'base_extrusion = {base_extrusion} \n')
f.write(f'number_of_rotor_blades = {number_of_rotor_blades} \n')

# Close .txt file
f.close()