# capstone-coronaboard-scheduler

This is part of the another projects for capstone Udacity CloudDeveloper

## Scheduler

This objective for this scheduler is get data from api every 10 minutes about Corona virus and then put on Database!

## Install

To run this make sure you have a Postgres database and Python3 on your machine:

- Execute the [sql](https://raw.githubusercontent.com/claudioacioli/capstone-corona-deployment/master/coronaboard.sql) file to create the database columns
- Clone this project 
```bash
git clone https://github.com/claudioacioli/capstone-coronaboard-scheduler.git scheduler
```
- Create and active the environment
```bash
cd scheduler
python3 -m venv venv
source venv/bin/activate
```
- Install the requirements:
```bash
pip install requirements.txt
```

## Run

To execute this:

- Execute the environment file(Remember to edit it with your settings)
```bash
source env.sh
```
- Execute
```bash
python3 main.py
```
