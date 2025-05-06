# Installation

The recommended method of installation for most users is via `pip`.

(content:start:install:pipvenv)=
## Install with pip and venv

In order to install Fesslix using `pip` inside a virtual environment of Python, please follow the steps outlined in the following.

(content:start:install:pipvenv:S1)=
### Step 1) Make sure Python is installed

As Fesslix is a Python module, you must have [Python][python] installed.

::::{tab-set}
:sync-group: os

:::{tab-item} Linux
:sync: Linux
Python comes preinstalled on most Linux distributions, and is available as a package on all others.
:::

:::{tab-item} Windows
:sync: Windows
Please [download][python-download] and [install][python-install] Python.
:::

:::{tab-item} macOS
:sync: macOS
Install a recent version of Python; e.g., using [Homebrew][homebrew]:
```bash
# If you have not already installed Homebrew, install it:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Use Homebrew to install Python:
brew install python
```
To update Python, run:
```bash
brew update
brew upgrade python
```
:::

::::

(content:start:install:pipvenv:S2)=
### Step 2) Create a virtual environment in Python

::::{tab-set}
:sync-group: os

:::{tab-item} Linux
:sync: Linux
```bash
python -m venv ~/.venv-fesslix
```
:::

:::{tab-item} Windows
:sync: Windows
```bat
py -m venv C:\path\to\new\virtual\environment\venv-fesslix
```
:::

:::{tab-item} macOS
:sync: macOS
```bash
python3 -m venv ~/venv-fesslix
```
:::

::::

(content:start:installation:activate-venv)=
### Step 3) Activate the virtual environment

::::{tab-set}
:sync-group: os

:::{tab-item} Linux
:sync: Linux
```bash
source ~/.venv-fesslix/bin/activate
```
:::

:::{tab-item} Windows
:sync: Windows
```bat
path\to\new\virtual\environment\venv-fesslix\Scripts\activate
```
:::

:::{tab-item} macOS
:sync: macOS
```bash
source ~/venv-fesslix/bin/activate
```
:::

::::

```{important}
Whenever you want to work with Fesslix, you need to **activate the virtual environment before starting Python**.
```

### Step 4) Install Fesslix as Python module

::::{tab-set}
:sync-group: os

:::{tab-item} Linux
:sync: Linux
```bash
pip install fesslix
```
:::

:::{tab-item} Windows
:sync: Windows
```bat
py -m pip install fesslix
```
:::

:::{tab-item} macOS
:sync: macOS
```bash
pip install fesslix
```
:::

::::


## Verifying the Installation

After installing NumPy, verify the installation by running the following commands in a Python shell or script:

```python
import fesslix as flx
print(flx.__version__)
```

This should print the installed version of Fesslix without errors.


## Keeping Fesslix up to date

::::{tab-set}
:sync-group: os

:::{tab-item} Linux
:sync: Linux
```bash
pip install --upgrade fesslix
```
:::

:::{tab-item} Windows
:sync: Windows
```bat
py -m pip install --upgrade fesslix
```
:::

:::{tab-item} macOS
:sync: macOS
```bash
pip install --upgrade fesslix
```
:::

::::

## Install as a local build

### new installation

Follow {ref}`Step 1<content:start:install:pipvenv:S1>`, {ref}`Step 2<content:start:install:pipvenv:S2>` and {ref}`Step 3<content:start:installation:activate-venv>` in section {ref}`content:start:install:pipvenv`.

Fetch the source code:
```bash
git clone https://github.com/fesslix/fesslix.git
cd fesslix
```

Trigger the local build:
```bash
pip install . -v
```

### updating an existing installation

To update an existing local build, change into the source directory of Fesslix and execute the following commands:
```bash
git pull
pip install . -v
```

### compile in debug mode

```bash
git pull
pip install . -v --config-settings=cmake.build-type="Debug" --config-settings=cmake.args=-DFLX_DEBUG=ON
```

[python-download]: https://www.python.org/downloads/windows/ "Python Releases for Windows"
[python-install]: https://docs.python.org/3/using/windows.html "Using Python on Windows"
[python]: https://www.python.org/ "Official website of Python"
[homebrew]: https://brew.sh/ "The Missing Package Manager for macOS (or Linux)"

