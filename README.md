# Introduction to Programming with Python

## Getting Started with VS Code and Python

1. Open VS Code (need to have VS Code installed).
2. Install the Python extension.
3. Create a new folder.
4. Open folder in VS Code.
5. Go to View > Command Palette.
6. Search for and select "Terminal: Select Default Shell". Select "Git Bash" (need to have Git installed).
8. Search for and select "Terminal: Create New Integrated Terminal". A Git Bash terminal will open within VS Code.
9. Create a virtual environment (follow instructions below).

## Virtual Environment

The venv module comes with Python3 (need to have Python3 installed). To check which version of Python is installed:
```console
$ python --version
Python 3.7.4
$ which python
/c/Users/your_userid/AppData/Local/Programs/Python/Python37-32/python
```
To create a virtual environment called env:
```console
$ python -m venv env
```
To start up the virtual environment:
```console
$ source env/Scripts/activate
```
Go to View > Commmand Palette. Search for and select "Python: Select Interpreter". Select ".\env\Scripts\python.exe".
```console
(env) $ python --version
Python 3.7.4
(env) $ which python
.env/Scripts/python
```
To shut down the virtual environment:
```console
(env) $ deactivate
```
