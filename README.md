# ML-Project
## This is full stack machine learning project.

## Software and Account Requirement
1.  Github Account
2.  Heroku Account
3.  VS Code
4.  Git Bash/Command promt


Creating Conda Environment:
```
conda create -p venv python=3.7 -y
```
Why to use -p insted of -n? 
Virtual Environment got created in same directory with name venv where all project files are present. It will keep vertual env along with project files. If we use -n then venv will be created in c drive where anaconda files are present.


Activate vitual Evnvironment:
```
conda activate venv
```
or
```
conda activate venv\
```

Creating requirements.txt:

Install Flask:
```
pip install Flask
```
or
```
pip install -r requirements.txt
```
(All libraries and packages which are mentioned in requirements.txt file will get installed.)


Create app.py file to write flask app code.

TO add all files to git:
```
git add .
```

NOTE: To ignore or folder we can write name of file or folder in .gitignore file

To check git status:
```
git status
```

To check all versions maintained by git:
```
git log
```

To create version/commit all changes by git
```
git commit -m <message>
```


