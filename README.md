# Myfastapi

-> Create Virtual environment

# Windows

py -3 -m venv env

# Linux and Mac

python3 -m venv env
-> Activate environment

# Windows

.\env\Scripts\activate

# Linux and Mac

source env/bin/activate
-> Install Requirements

pip install -r requirements.txt
-> Make sure project is running

uvicorn main:app --reload
