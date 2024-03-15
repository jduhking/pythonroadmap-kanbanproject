### How to run

In order to start the virtual environment, make sure you are in the project directory and then run the following command

```
python3 -m venv .venv

```
### Activate the environment

Next, activate the virtual environment

```
. .venv/bin/activate
```

Finally, run the flask program

```
flask --app main run
```

Open up the browser at http://127.0.0.1:5000 in order to test that it is working, you should see hello world