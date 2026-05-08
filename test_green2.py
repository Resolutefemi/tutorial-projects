import os
if os.name == 'nt':
    os.system('color')
print('\033[32m', end='')
print("This should be green.")
print("This too.")
print('\033[0m', end='')
