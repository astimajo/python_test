'''
medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)
print(instructions)
'''
'''
name = 'world'
message = f'hello, {name}.'
print(message)

count = 10
value = 3.14
message = f'count to {count}. Multiply by {value}.'
print(message)
'''
'''
width = 5
height = 10

print(f'the perimeter is {(2 * width) + (2 * height)} and the area is {width * height}. ')
'''

value = 'hi'

print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')