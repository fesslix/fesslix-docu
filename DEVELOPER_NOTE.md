# Initial Inspiration

The template for this book is from:
https://github.com/readthedocs-examples/example-jupyter-book

# Building the book

## Local build

Install required Python dependencies (Sphinx etc.):
```
pip install -r docs/requirements.txt
```

Build the Spyhinx config-file:
```
jupyter-book config sphinx docs/
```

When updating css-sytling, a cleanup can help:
```
jupyter-book build docs/
```

Run Jupyter Book:
```
jupyter-book build docs/
```

View the docs with for instance firefox:
```
firefox docs/_build/html/index.html
```

## Working on the book

### Initial preparations

Make sure you are working in the correct virtual environment in Python; i.e.,:
```
source ~/.venv-fesslix/bin/activate
```

Also make sure the required packages are installed:
```
pip install jupyterlab ipykernel
```

Once Jupyter is installed, register your environment as a kernel:
```
python -m ipykernel install --user --name=.venv-fesslix --display-name "Python (.venv-fesslix)"
```

### Start JupyterLab
```
jupyter-lab
```


