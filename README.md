# GithubCLITool

This is a command line tool that you can use to query public repositories for its number of open pull requests. This can programme can be run on both Windows 10 and macOS.

This tool will require python3 and the dependencies listed in *requirements.txt*. For instructions on how to install and run the programme follow the steps below. If you are an experienced user and would like to know how the programme is run, skip to step 11.

# How to install

1. Download and extract the zipped code form github.
2. If your machine does not have python3 installed, download it from [here](https://www.python.org/downloads/) for your operating system. Remember to install the software.
3. To confirm that you have the latest version of python3 installed on your machine execute the following command in the terminal **python3 --version** (macOS) or **python** (Windows).

These instructions will use pip to download the dependencies, if you prefer another method you can skip the following section, otherwise continue reading.

4. In the terminal, in the same location as you installed python3, execute the following command **curl https:<i></i>//bootstrap.pypa.io/get-pip.py -o get-pip.py**
5. Next, execute **python3 get-pip.py** to install pip.
6. To confirm that pip has been correctly installed, execute **pip3 --version** (macOS) or **pip --version** (Windows)

7. In the terminal, navigate to the folder where you downloaded/extracted the *multitudesCLITool-main* code. You can do so by executing the command **cd multitudesCLITool-main**
8. To confirm that you are in the correct directory, execute the command **ls** to list the files in the current directory. The files listed should be the 3 files in this repoistry; **README.md**, **multitudesCLI.py** and **requirements.txt**
9. Next you will install the dependencies by executing the command **pip3 install -r requirements.txt**
10. Done!

# Running the programme

This programme is run from the terminal by executing the command **python3 multitudesCLI.py** (macOS) or **python multitudesCLI.py** (Windows). When running on Windows, make sure you navigate to the correct directory before exectuing the command to start the programme. When the programme begins, the terminal will be cleared and you will be met with the following screen:



You will be asked the owner of the repositry you would like to query and the name of the repositry you would like you query.
