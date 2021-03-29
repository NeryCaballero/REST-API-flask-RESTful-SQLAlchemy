# Heroku required files for deployment

1. `runtime.txt` : Define in here the version of Python.
   

2. `requirements.txt`: List all the required dependencies in here.
   Note: `psycopg2` is a library to interact with postgreSQL and its used in Heroku.


3. `uwsgi.ini`: this are the configuration parameters for the UWSGI process to run our app.
   
    ```python
    [uwsgi]
    http-socket = :$(PORT)
    master = true
    die-on-term = true
    module = run:app
    memory-report = true
    ```
   Note: You don't have to install UWSGI. 
   
   If you try, likely it will fail because you need a C Compiler to install UWSGI.
   Heroku will be able to install it and use it.
    
   - First: Declare the section `[uwsgi]`
   
   - Next: Specify the port `http-socket = :$(PORT)`, this instructs to read the port number from the Heroku configuration.
   
   - Next: `master = true`, which means we're going to use a master process when we run UWSGI.
   
   - Next: `die-on-term = true`, when a process terminates, we're going to kill the UWSGI process just to free up the resources.
   
   - Next: `module = run:app`, indicate that the module that we're running is the Flask app, which we want to initialize from `run.py` and the variable is called `app`.
   Heroku it's going to look at that variable and that's what it's going to run as a UWSGI application.
   
   - Lastly: `memory-report = true`.


4. Procfile
   
   ```python
   web: uwsgi uwsgi.ini
   ```
   
   We're going to put here the dyno we want to use in Heroku. A dyno is the server which have specific types.

   This dyno is going to connect to a HTTP port, so it's important that it is a dyno of type web.

   Then we declare what process it's going to run and what application it's going to run.
      - So here we could do something like `web: python3.5 app.py`, and that would presumably use the python3.5 process to run app.py.

   But we're not going to do that because we're using UWSGI so, all that we have to do is say `web: uwsgi, uwsgi.ini`.


5. `run.py` : this file is created to initialize the app from Heroku.