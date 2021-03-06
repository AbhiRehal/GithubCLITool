# GithubCLITool

This is a command line tool that you can use to query public repositories for its number of open pull requests. This can programme can be run on both Windows 10 and macOS.

This tool will require python3 and the dependencies listed in *requirements.txt*. For instructions on how to install and run the programme follow the steps below. If you are an experienced user and would like to know how the programme is run, skip to below.

# How to install

1. Download and extract the zipped code form github.
2. If your machine does not have python3 installed, download it from [here](https://www.python.org/downloads/) for your operating system. Remember to install the software.
3. To confirm that you have the latest version of python3 installed on your machine execute the following command in the terminal **python3 --version** (macOS) or **python** (Windows).

These instructions will use pip to download the dependencies, if you prefer another method you can skip the following section, otherwise continue reading.

4. In the terminal, in the same location as you installed python3, execute the following command **curl https:<i></i>//bootstrap.pypa.io/get-pip.py -o get-pip.py**. This will install pip onto your machine.
5. Next, execute **python3 get-pip.py** (macOS) to install pip. If you are on a Windows machine, execute the command **python get-pip.py**.
6. To confirm that pip has been correctly installed, execute **pip3 --version** (macOS) or **pip --version** (Windows).
7. In the terminal, navigate to the folder where you downloaded/extracted the *multitudesCLITool-main* code. You can do so by executing the command **cd GithubCLITool-main** (macOS). If you are on a Windows machine, navigate to the directory using the specific file path.
8. To confirm that you are in the correct directory, execute the command **ls** to list the files in the current directory. The files listed should be the 4 files in this github repoistry, namely; **READMEImages**, **README.md**, **multitudesCLI.py** and **requirements.txt**.
9. Next you will install the dependencies by executing the command **pip3 install -r requirements.txt** (macOS). For Windows, execute the command **pip install -r /path/to/requirements.txt** remembering to replace the **/path/to** with your specific path.
10. Done!

# Running the programme

This programme is run from the terminal by executing the command **python3 multitudesCLI.py** (macOS) or **python multitudesCLI.py** (Windows). Make sure you navigate to the correct directory before exectuing the command to start the programme. When the programme begins, the terminal will be cleared and you will be met with the following [screen](https://github.com/AbhiRehal/GithubCLITool/blob/main/READMEImages/p1.PNG).

You will be asked the to enter the **owner** of the repositry and the **name** of the repositry that you would like to query. Once you enter the requests, you will be met with an output that looks similar to [this](https://github.com/AbhiRehal/GithubCLITool/blob/main/READMEImages/p2.PNG). At this point you can press **y/Y** to rerun the programme or you can hit **enter/return** to exit the programme. If the inputs you enter result in an error, you will be [informed](https://github.com/AbhiRehal/GithubCLITool/blob/main/READMEImages/p3.PNG) in the terminal.
