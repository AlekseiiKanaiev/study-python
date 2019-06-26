# This script does three things:

# 1) it sets ./src/main.py as the value of the FLASK_APP environment variable 
#   (this is needed by the last command);
# 2) it activates the virtual environment;
# 3) and it runs flask listening on all interfaces (-h 0.0.0.0).


#!/bin/bash
export FLASK_APP=./src/main.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0

# Then, to test everything, you can use the following commands:
# # make script executable
# chmod u+x bootstrap.sh

# # execute script in the background
# ./bootstrap.sh &

# # create a new exam
# curl -X POST -H 'Content-Type: application/json' -d '{
#   "title": "TypeScript Advanced Exam",
#   "description": "Tricky questions about TypeScript."
# }' http://0.0.0.0:5000/exams

# # retrieve exams
# curl http://0.0.0.0:5000/exams