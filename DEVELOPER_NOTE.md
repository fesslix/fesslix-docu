# Initial Inspiration

The template for this book is from:
https://github.com/readthedocs-examples/example-jupyter-book


# Building the book

## Local build

### initially: setting things up
Make sure you are working in the correct virtual environment in Python; i.e.,:
```
source ~/.venv-fesslix/bin/activate
```

Install required Python dependencies (Sphinx etc.):
```
pip install -r docs/requirements.txt
```

Build the Spyhinx config-file:
```
jupyter-book config sphinx docs/
```


### perform the build

Run Jupyter Book:
```
jupyter-book build docs/
```
To check for missing references during build:
```
jupyter-book build -W -n --keep-going docs/
```

### View the book

View the docs with for instance firefox:
```
firefox docs/_build/html/index.html
```

### clean things up

To enforce a *full build*, you can clean-up the build directory (e.g., after updating css-sytling):
```
jupyter-book clean docs/
```


## Working on the book

### initially: setting up JupyterLab

Also make sure the required packages are installed (sytem-wide):
```
jupyterlab ipykernel ipympl
```

Once Jupyter is installed, register your environment as a kernel:
```
python -m ipykernel install --user --name=.venv-fesslix --display-name "Python (.venv-fesslix)"
```

### Start JupyterLab
```
jupyter-lab
```


