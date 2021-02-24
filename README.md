# Introduction to Programming with Python

Open VS Code.
Install the Python extension.

Create a new folder.
Open folder in VS Code.

Go to Command Palette.
Search for and select "Terminal: Select Default Shell".
Select Git Bash (need to have Git installed).
Search for and select "Terminal: Create New Integrated Terminal".
A Git Bash terminal will open within VS Code.

Create a virtual environment.
venv comes with Python3 (need to have Python3 installed).
```
$ python --version
Python 3.7.4
$ which python
/c/Users/your_userid/AppData/Local/Programs/Python/Python37-32/python
```
To create the a virtual environment called env.
```
$ python -m venv env
```
To start up the virtual environment.
```
$ source env/Scripts/activate
```
Go to Commmand Palette.
Python: Select Interpreter
Select .\env\Scripts\python.exe
```
(env) $ python --version
Python 3.7.4
(env) $ which python
.env/Scripts/python
```