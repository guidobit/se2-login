# System Engineering 2 (HVA)

## Docker Login Microservice
This is a microservice created as part of an education program @ Hogeschool van Amsterdam

### Getting started
#### Prerequisites:
Get Docker
Clone this project from github
Virtualenv (or windows equivalent)

#### How to use:
1. Build the container: `docker build -t se2-login:latest .`  (don't forget the `.` at the end)
2. Run the container: `docker run se2-login:latest`

#### How this works
The Dockerfile instructs the docker deamon to copy over the project files and install the requirements, after this is done it will run the program by running `python3 run.py`

### VirtualEnv
1. Run `virtualenv --python=python3 env` to create a Python3 virtual environment
2. Run `source env/bin/activate` to enable the virtual environment
3. To verify if you now have a Python3+ environment: `python --version`

### Developing
For now the process is as followed.

#### Flow
1. Activate the virtualenv
2. If you have new dependencies, install with `pip install your-dependency`
3. If you want to commit the dependency to git or test it in the Dockerfile, run `pip freeze`, find the line with the dependency and add this to a newline in `requirements.txt`
4. After changes to your code, re-run the `docker build` && `docker run` command.

Step 4 might need some improvement, but this will be added in a later iteration.
 
#### GIT use
To work on a feature, create a seperate branch as followed:
`git branch` --> this prints your current branch
`git checkout master` ---> if you are not on master
`git checkout -b feature/my-cool-feature` --> to work on your awesome feature

