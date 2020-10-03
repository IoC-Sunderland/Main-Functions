from termcolor import colored


if __name__ == '__main__':
  print('Executing as a script...')

else:
  print('Importing import_me module...')
  print("The value of import_me's __name__ is:", colored(repr(__name__), 'green'))
