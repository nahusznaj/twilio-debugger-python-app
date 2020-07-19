This repository shares the code from my blogpost https://www.twilio.com/blog/handle-twilio-debugger-events-python-flask

It's a Flask application that will listen to your Twilio account's Debugger Alert Triggers, and write relevant content into a CSV file.

Always consult Twilio's official documentation as this is maintained, while blog posts may become out of date!

Relevant docs for this case: https://www.twilio.com/docs/usage/troubleshooting/debugging-event-webhooks and https://www.twilio.com/docs/usage/troubleshooting/alert-triggers 

# Steps to use this script

Create a folder, open a terminal and `cd` into the folder.

Create a virtual environment, in my case, I called it debugger-app-venv (the folder from my virtual environment is not included in this repository): 

```
$ python3 -m venv debugger-app-venv
```

Activate the virtual environment
```
$ source debugger-app-venv/bin/activate
```

Install the requirements with
```
$ pip3 install -r requirements.txt
```


This will basically install [Flask](https://www.palletsprojects.com/p/flask/), which will allow us to create the web application.

After the install is completed, you'll be good to go! More details and discussion on Twilio's [blog post](https://www.twilio.com/blog/handle-twilio-debugger-events-python-flask).


Once you're done and want to leave the virtual environment, you can simply run `deactivate`:

```
(debugger-app-venv) user$ deactivate 
user$ 
```


# To do:

Things I'd like to do in future with this project:
- I would put this app available in the internet through a cloud service, like AWS, instead of using ngrok. That way, I won't need the app running locally.

- I'd like to write a more sophisticated database, instead of a CSV file.