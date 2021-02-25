# unigloo

A simple web app for warehouses inventory

### Virtual environment

- Testing against Python 3.7 to support data classes.

```bash 
virtualenv -p python3.7 uni_venv
```

- Activate the virtualenv
```bash
source uni_venv/bin/activate
```

### How to Run It

- Execute the program using:


      -  $ python main.py

- Run the Flask web app using:


      -  $ FLASK_APP=app.py flask run

### How to Run the Unit Tests

1. Install requirements as usual:
    ```bash
       pip install -r requirements.txt
       pip install -r test-requirements.txt
    ```
1. Run the tests:
    ```bash
       pytest
    ```

### Deployment

A running solution is hosted on heroku and can be accessed publicly at https://unigloo.herokuapp.com/