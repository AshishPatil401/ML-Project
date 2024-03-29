# ML-Project 
## House Price Prediction
## This is full stack machine learning project.

### Software and account Requirement
    1. Github Account
    2. Heroku Account
    3. VS Code IDE
    4. Git Bash/Command promt
    5. Git Documentation


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

To add all files to git:
```
git add .
```

NOTE: To ignore files or folders we can write name of file or folder in .gitignore file

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

To check remote url
```
git remote -v
```

To push code to remote repository
```
git push origin main
```

### To setup CI/CD pipeline in Heroku we need 3 information
    1. HEROKU_EMAIL     = ashish.patil401@gmail.com
    2. HEROKU_API_KEY   = <...>
    3. HEROKU_APP_NAME  = ml-regression4


Build Docker image
```
docker build -t <image_name>:<tag_name> .
```
NOTE: Image name for docker must be in lower case.


To list docker images:
```
docker images
```

Run docker image:
```
docker run -p 5000:5000 -e PORT=5000 <image id>
```

To check running containers in docker
```
docker ps
```

To stop docker container:
```
docker stop <container_id>
```

To install libraries mentioned in requirement.txt file
It will install all external libraries and packages mentioned in the file
```
python setup.py install
```


To install custom packages like housing, add -e . to requirements.txt
```
-e .
```
NOTE: Whenever we are going to install -e . at that time setup.py file should be present in current directory.


To install ipykernel
```
pip install ipykernel
```

Data Drift: 
    - When your datset stats gets change we call it as data drift.
    - To detect data drift we are using Evidently library.
    - Evidenty library internally uses ks_2samp from scipy.stats to compare the distribution of 2 arrays.

