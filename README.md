Project is run from a virtual python environment.

Within WSL Ubuntu, the python venv was installed with:

`sudo apt update`
`sudo apt install python3.12-venv`

The following was then run from the root of the project to setup the venv:

`python3 -m venv .venv`

The env can now be activated with:

`source .venv/bin/activate`

There is a helper script to run the above rather than the long command, just do:

`source venv`

You are now inside the venv and are using the venv python.  Changes made to python, such as new pip modules, are only made inside this venv, they do not affect the global python.

To install the pip modules:

`pip install -r requirements.txt`

To deactivate the venv:

`deactivate`

The python interpreter has been set to the venv, so if running the code from an integrated terminal (or the `run` arrow`) there is no need to source the venv.

Note that this change means all python code run via vscode uses this venv, which will not be the desired behaviour if working across multiple projects.
