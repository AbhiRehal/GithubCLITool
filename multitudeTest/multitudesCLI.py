import os
from github import Github
from termcolor import colored
from pyfiglet import Figlet
import colorama

# function to clear the conosle based on the operating system of the machine
def clearConsole():
    if os.name in ('nt', 'dos'):
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

clearConsole()

# required to use colored method from termcolor library on windows
colorama.init()

# Header
print(colored(Figlet(font='standard').renderText('Multitudes   CLI'), 'green'))

print(colored('Enter the owner of the repositry:', 'green'))
owner = input()

print(colored('\nEnter the name of the repositry:', 'green'))
repo_name = input()

print('\nQuerying repositry ' + colored(owner + '/' + repo_name, 'magenta') + ' for open pull requests, please wait...')

# Using PyGithub library, create a Github() object and query for the repo specified by the user for open pull
# requests and returns the size of the paginatedList. Casts it to string and prints to console.
try:
    print('Open pull requests -> ' + str(Github().get_user(owner).get_repo(repo_name).get_pulls(state='open').totalCount))
except:
    print('An error has occured, please check that your input is correct and try again.')
finally:
    print('Press any key to exit...')
    input()

input("hit")