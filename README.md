# k8s-tutorial
Implementing microservice based apps on k8s by following https://devopswithkubernetes.com/part-1/1-first-deploy


## Accessing the log-output endpoint

Access via http://localhost:8081 because we have forwarded port 8081 to port 80 on the loadbalancer/ingress at cluster creation.
## Setting up local k3d cluster

The addition to `/etc/hosts` is required, so it is possible to push (pull) images to (from) the cluster registry
```
k3d cluster create kalmis-local --volume $PWD/data:/tmp/k3dvol --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2 --registry-create kalmis-local-registry:0.0.0.0:2000
echo '127.0.0.1       kalmis-local-registry' >> /etc/hosts
```

## Deplyoing

```
./build_and_push.sh <tag>
# Modify the deployment.yaml to use the same tag for the image
kubectl apply -f manifests/
```

## Setting up development environment in VS code

Before starting the development, a correct version of Python, pre-commit hooks, and also styling settings are needed. This project uses flake8 for linting and black for automated code formatting (format on save is enabled). Pre-commit hook that runs black (autoformatting) and flake8 (linting & security/best practice warnings) automatically before each commit. If black needed to format the file or any flake8 errors were raised, then the commit will fail. Before running commit again, fix the problems and/or addto stage the modified files again.

1. Download and install pyenv (https://realpython.com/intro-to-pyenv/)
   1. Pyenv is used to ensure that everyone has the same (and correct) Python version installed. See `.python-version` for the current one
2. Open this repository in VS code if you haven't already
3. Open any of the `.py` files in this repository. VS Code should ask you to install Python extensions (or install Python extension manually)
4. Install the following extensions (and maybe find a few new ones for yourself!) CMD+SHIFT+P | Install extensions | Search
   1. Gitlens  (Read the description, but basically native git integration to VS Code + git blame on all rows etc. There's also UI on the left panel)
   2. Github Pull Requests and Issues (Integration with Github, so you can easily open the PR related to commits or create a new PR. There's also UI on the left panel)
   3. Kubernetes
   4. Markdown All in One (Preview markdown files and what not)
5. Open a terminal in VS Code if it is not open yet (View | Terminal)
6. Check which python version is required and install it
   1. Check the required python version by `pyenv versions`
   2. If it is not installed then run `pyenv install x.y.z` (```pyenv: version `3.10.6' is not installed (set by /Users/kimipaivarinta/git/kokko-clean/.python-version)```)
   3. If it is installed, you should see a asterix next to the correct version (`* 3.10.6 (set by /Users/kimipaivarinta/git/kokko-clean/.python-version)`)
7. Create a virtual environment called by `python -m venv venv`
8. Activate the virtual environment by `source venv/bin/activate` or on Windows (`.\venv\Scripts\Activate`) (this should be done automatically by VS Code when you open the project in the future)
9.  Update to the latest pip `pip install --upgrade pip`
10. Install dependencies by running  `pip install -r app/test-requirements.txt` (also install requirements.txt) and `pip install -r app/dev-requirements.txt`
   1. This will install 1) Normal depdencies (airflow, requests etc.), 2) Test dependencies (pytest etc.), and 3) Dev dependencies (lint/formatting etc.)
   2. While testing and running the Kokko code is most convenient inside a Docker container, all the dependencies should be installed in the virtual environment, so VS Code is able to locate them.
11. Install pre-commit hooks by running `pre-commit install`
12. You are all set! Some notes
    1.  Flake8 & Pylance will be automatically analysing all open files. You can see the problems in "Problems" tab at the bottom of VS code. Fix the problems while you see them.
    2.  Black autoformat on save is enabled. If you want to disable it (temporarily) you can do so by editing `.vscode/settings.json`
    3.  There are still files that have not been formatted by black. Try to start with black formatting and do a separate commit for that.
    4.  See using VS Code below