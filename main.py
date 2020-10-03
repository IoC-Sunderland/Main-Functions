from termcolor import colored
import import_me

def main_function():
  print("The value of main's __name__ is:", colored(repr(__name__), 'green'))

if __name__ == '__main__':
  main_function()
