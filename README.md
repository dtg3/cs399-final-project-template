# Final Project Template

This is the template for creating your final project. I have included with this a basic, but fully functioning
example application so you can observe how the code is working and map your implementation to this template. The
project is divided into two separate applications, the `frontend` which is all your React code, and the `backend` which
is all the Flask code.

## .flaskenv

I did not include a `.flaskenv` in this template. Some folks might be using external API keys in their project,
and I would like to avoid those becoming accessible via GitHub code.

To get your project started, you can create a `.flaskenv` in your `backend` directory with the following content to get started:

```
FLASK_APP=run
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=CHANGEMEPLEASE!
DATABASE=todo.db
```

## Running the project

To run this application you will:

1) Open a terminal and use the "split terminal button"
2) Keep one of the terminals in the `backend` folder and the other should be in the `frontend` folder
3) In the `backend` terminal, create the python venv and use pip to install all the dependencies from `requirements.txt`
4) Once you have all the dependencies installed, you have options:
    * You can initialize the sample database (it does not have data just a schema) using: `flask initdb`
    * You can run the test suite using; `pytest`
    * You can start the api service using: `flask run`
5) With the flask api service running in the `backend` terminal, switch to the `frontend` terminal
6) Install your dependencies using: `npm install`
7) Start your React frontend app using `npm run dev`

At this point the application is ready to run. In the future, you will only need to have your two terminals open,
ensure your `backend` terminal has your Python environment activated, and use `flask run` for the backend and
`npm run dev` from the `frontend` terminal window.
