# pi.ai_automation

To set up project

In Linux:

Create a virtual environment 
```bash
python -m venv .venv
```
Activate the environment 
```bash
source .venv/bin/activate
```
Install packages
```bash
pip install playwright
```
```bash
playwright install
```
Create a dir called .auth #not a rule but thats how i did it
```bash
mkdir .auth
```
Create a Json file to store login state to re-use later
```bash
touch .auth/pi.json
```

Also don't forget to fill your correct Facebook idp in piAiLogin.py file
