

## Connecting to Database UI

*URL*: http://localhost:8080/    
*SYSTEM*: projectetl  
*USER*: projectetl  
*PASSWORD*: projectetl   
*DB*: projectetl  

## Running the app

### Local Usage

```
export POSTGRES_DB=projectetl  
export POSTGRES_USER=projectetl  
export POSTGRES_PASSWORD=projectetl  
export DB_IP_ADDRESS=127.0.0.1  
# set if you want to run intergration tests
# export INTERGRATION_TEST=True
```

## Docker Setup

1. Install docker and docker-compose

2. ```sudo --preserve-env docker-compose up```

#### setup python environment

##### Initial setup

```apt-get update && \
sudo apt install -y python3-pip python3

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python-openssl git 

curl https://pyenv.run | bash 

export PATH="$HOME/.pyenv/bin:$PATH" 
eval "$(pyenv init -)" 
eval "$(pyenv virtualenv-init -)"

pyenv install 3.8.0 

pyenv virtualenv 3.8.0 app_3.8
```

##### using pyenv environment
```
pyenv activate app_3.8  
pip3 install -r requirements.txt  
sudo --preserve-env docker-compose up
```  

#### if you need to access the docker container
```
sudo docker ps
sudo docker exec -it <container name> bash
```
