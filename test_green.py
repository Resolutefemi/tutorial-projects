import sys
import os

if os.name == 'nt':
    os.system('color')

class GreenStdout:
    def __init__(self, stdout):
        self.stdout = stdout
    def write(self, text):
        if text.strip():
            self.stdout.write('\033[32m' + text + '\033[0m')
        else:
            self.stdout.write(text)
    def flush(self):
        self.stdout.flush()

sys.stdout = GreenStdout(sys.stdout)

print("This is a test.")
