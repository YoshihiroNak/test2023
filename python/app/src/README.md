# Terminal_app_T1A3

# [GithubRepo](https://github.com/YoshihiroNak/Terminal_app_T1A3/tree/main/src)

# [Source Control Repo](https://github.com/YoshihiroNak/Terminal_app_T1A3/commits/main)

# [Projects](https://github.com/users/YoshihiroNak/projects/1)
## Statement of Purpose

"Catering Services for your party" This is an application that is a food catering planning guide for users.
The final quote changes depending on the user's selections, and the user can confirm their selections on the final screen.

The purpose of this application is to represent skills in utilizing all operational system functions.

It is a requirement to accept user input and produce printed output or interact with the file system

## Target Audience

The application is designed to be relatable to a wide range of age groups so that anyone can be targeted.

Catering services are familiar in daily life, and the appliocation is designed to allow you to easily select a plan and check the total cost.

## Features of Catering Services

### 1: Display menu and price list

This feature appears shortly after the application has started. The title can be expressed with more impact by importing pyfiglet. The contents of the menu and price list displayed after the title are managed in advance by a dictionary and are designed to be easily changed. Changes are designed to link to other features.

### 2:　Menu Selection

This feature is designed to output the user's selections and record the user's selections. The loop is designed so that if there is a mistake in the selection, an error message will be displayed and the process will be retried.

### 3:　Exit or Retry

This feature will appear at the end of this application. It is designed so that the user can select "Yes" to start over or "No" to exit the application.

### 4:　Main Function

This feature is the core of this application.
Most functions are called from the main function and are designed to cycle through outputs and selections to help users navigate the application.

It also has a function that automatically calculates the information received from the user, and displays and the total amount to the user on the final screen.

## Code Style Guide and Styling Conventions

I followed PEP8 guidelines in coding with python. I wrote the code with a consistent style such as indentation and line length of 79 characters or less. [PEP8 Style Guide](https://peps.python.org/pep-0008/)

## Implementation Plan

I used one of github's features, projects, to manage tasks. kanban style task management was very efficient and gave me a great view of tasks ahead. I prioritized tasks on a small, medium, and large scale as needed.

### Projects screenshots

#### projects_25th_oct

Checklists includes features:
Features are function of menu, loops for user input, calculation for total price and confirmation for user.

![projects_25th_oct](/docs/projects_25th_oct.png)

#### projects_26th_oct

![projects_26th_oct](/docs/projects_26th_oct.png)

#### projects_27th_a_oct

![projects_27th_a_oct](/docs/projects_27th_a_oct.png)


#### projects_27th_b_oct


Deadlines are attached to tasks that should have deadlines in consideration of other tasks.

![projects_27th_b_oct](/docs/projects_27th_b_oct.png)

#### projects_28th_oct

Some tasks are set with small or medium or large.
These means that Large, medium, and small represent the amount of work involved in a task.
Large: 6-8 hours
Medium: 4-6 hours
Small: 2-4 hours

![projects_28th_oct](/docs/projects_28th_oct.png)
#### projects_29th_oct

![projects_29th_oct](/docs/projects_29th_oct.png)


## Help Documentation

Currently, this application is only suppoerted on Linux and macOS. If you are a windows user, please make sure you have WSL Ubuntu on your PC. If you don't have, please follow this guide to install : [WSL Ubuntu](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview)

### Open the terminal

Linux systems usually come with Python pre-installed.
Please check the version following this command.

### Check a version of Python you have installed

```
python --version
```

- If you don't have Python installed or you have a version less than 3.10, please follow this guide to install : [Python](https://www.python.org/downloads/)

- You need to have Bash to run this applocation.
 Terminal for MacOS and Linux
 Git Bash for windows

### Copy a file from github and Clone in your terminal

Please create new file and move into your new file in the termianl.

```
mkdir newfile
cd newfile
```

![Tgit clone](/docs/gitclone.png)

```
git clone https://git@github.com:YoshihiroNak/Terminal_app_T1A3.git
```

After that,
1.

```
cd Terminal_app_T1A3

```
2.
```
cd src
```
3.
```
bash catering.sh
```
You run the catering Services Application

### Installation Process

Please make sure where you are located in termainl.
```
pwd
```

```
/newfile/Terminal_app_T1A3/src
```

Execute permission is already astivated, However, it can be reenabled with this command.

```
chomd +x catering.sh
```

It can be run with this command.

```
./catering.sh
```

## How to operate in the apllication

Navigation within the application is simple:
enter the number 1, 2, 3,
'y' or 'n' to select Yes or No, and then type only to enter allergies.

## Dependencies

```
colorama==0.4.6
iniconfig==2.0.0
packaging==23.2
pluggy==1.3.0
pyfiglet==1.0.2
pytest==7.4.3
pytest-mock==3.12.0
tenacity==8.2.3
```

## Reference List

Rossum, G., Warsaw, B., & Conghlan, A. (2001, Jul 5)
PEP 8 – Style Guide for Python Code
[https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)