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

while True:
    owner = input(colored('Enter the owner of the repositry:\n', 'green'))
    repo_name = input(colored('Enter the name of the repositry:\n', 'green'))
    print('Querying repositry ' + colored(owner + '/' + repo_name, 'magenta') + ' for open pull requests, please wait...')

    try:
        # Using PyGithub library, create a Github() object and query for the repo specified by the user for open pull
        # requests and returns the size of the paginatedList. Casts it to string and prints to console.
        print('Open pull requests -> ' + str(Github().get_user(owner).get_repo(repo_name).get_pulls(state='open').totalCount))
    except:
        print('An error has occured, please check that your input is correct and try again.')
    finally:
        rerun = input('Enter ' + colored('y', 'green') + ' to rerun the script, else press ' + colored('enter', 'green') + ' to exit...\n')
        if rerun == 'y' or rerun == 'Y':
            continue
        else:
            break