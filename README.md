# GithubCLITool

This tool requires python3 and the dependencies listed in "requirements.txt".

1. Download and extract the zipped code form github.
2. If your machine does not have python3 installed, download it from [here](https://www.python.org/downloads/) for your operating system.
3. Open up the terminal and confirm that you have the latest version of python3 installed on your machine. This can be done by entering **python3 --version** on a mac terminal or by entering **python** on a windows cmd.

This explanation will use pip to install the dependencies, if you prefer to get your packages in a different manner go ahead.

4. In the terminal, in the same location as you installed python3, execute the following command **curl https:<i></i>//bootstrap.pypa.io/get-pip.py -o get-pip.py**.
5. Next, execute **python3 get-pip.py** to install pip.
6. You can check that pip has been correctly installed by executing **pip3 --version**
7. In the terminal, navigate to the folder where you downloaded the multitudesCLITool-main code.
8. To check you are in the correct directory, you can execute the **ls** command and it will list the files in the current directory. The files listed should be the 3 files you have downloaded; **README.md**, **multitudesCLI.py** and **requirements.txt**.
9. Here you will install the dependencies. To do so, execute the command **pip3 install -r requirements.txt**.
10. Once the dependencies are installed, run the program by executing the commnand **python3 multitudesCLI.py**. It will clear the console and the program will begin.

11. To use the program you must enter the owner of a repositry and the name of the repositry you would like to query.
