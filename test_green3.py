import os
import atexit

if os.name == 'nt':
    os.system('color')
print('\033[32m', end='')
atexit.register(lambda: print('\033[0m', end=''))

print("This is green.")
