# We do not do tdd
# run pgbackup postgre... --driver s3 bucketname
#                         -- driver local/path/ti/file


# SET UP
# mkdir -p ./project/pgbackup/src
# cd project/pgbackup
# touch README.md setup.py src/.gitkeep

#vi setup.py -> see setup.py to check what's inside

# Once done, pipenv --python python3.7
# First I add to do this pip3 install --user pipenv
# and include the the localisation into my path
# pipenv shell

# Now let's populate de README.md

# Then git init
# git add --all .
# git status
# Add a gitignore, we can find lot of example on github : https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
# git add --all .
# git status
# git commit -m 'Initial commit'

### SETTING UP EXTERNAL DEPENDENCIES
# exit
# pip3 install --user awscli
# aws configure
# -> AWS Access Key Id : 
# -> AWS Secret Access Key : 
# this will create a file in ~/.aws/{config,credentials}
# ssh cloud-user@{ip_adress}

### BUILDING THE CLI ###
# WE would like to create a package...
# mkdir src/pgbackup
# touch src/pgbackup/__init__.py

# To test everything is fine python -i src/pgbackup/cli.py
# I everything is ok, we can commit : 
# git add --all
# git commit -m 'Created pgbackup package and cli module'

### INTERACTING with EXTERNAL  ###
# PYTHONPATH=./src python
# this command loads the packages who exists
# from pgbackup import pgdump
#dump = pgdump.dump('blabla//demo:id_adress')
# f =open('dump.sql', 'w+b')
# f.write(dump.stdout.read())
# f.close()

# git add --all
# git commit -m 'Add pgdump module'

### STORING DATA LOCALLY ###

### INTERACTING WITH AWS S3 ###
# pipenv install boto3 (official amazon client library)
# echo "UPLOADED" > example.txt
# PYTHONPATH=./src python
# import boto3
# from pgbackup import storage
# client = boto3.client('s3')
# infile = open('exampel.txt, 'rb')
# storage.s3(client, infile, 'python-backups', infile.name)
# rm example.txt

### WIRING THE PIECES TOGETHER ###
## Be sure the virtual env is active
## pip install -e .

### DISTRIBUTING the PACKAGE ###
# python setup.py --help
# python setup.py bdist_wheel
#ls -> we'll see we have a dist and a build directory
# ls dist/
# the .whl fil is our wheel fil that we can actually install
# pip uninstall pgbackup
# pip install dist/pgbackup-0.1.0-py3-none-any.whl 
# python 
# import boto3
# f = opent('dist/pgbackup-0.1.0-py3-none-any.whl', 'rb')
# client = boto3.client('s3')
# client.upload_fileobj(f, 'python_backups', 'pgbackup-0.1.0-py3-none-any.whl')
# exit()
# Now, exit the pipenv -> exit
# pip3 install --user https://s3.balblab/python-backups/pgbackup-0.1.0-py3-none-any.whl
