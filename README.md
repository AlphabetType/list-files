# Alphabet FileList
A Python CLI script demo containing a little program to list files in a folder.

## Usage

To run Alphabet FileList, you can use the `filelist` command. To see all available arguments you can use the `-h` flag:

```console
$ filelist -h
```

If you want to investigate the command line arguments, then you can check out the [cli.py file](src/alphabet_filelist/cli.py) 

## Installation as a User

If you have Python installed on your system, then you can install Alphabet FileList with `pip`. Open the terminal and run this command:

```bash
$ python -m pip install git+https://github.com/AlphabetType/list-files
```

You can verify that the installation was succesful by running the `filelist` command in your terminal.

## Installation as a Developer

Clone this repository and navigate into the repository folder. After that, it's a good idea to create a virtual environment and activate it:

```bash
$ python -m venv venv/
$ source venv/bin/activate
(venv) $
```

Make sure that you're in the root folder of the cloned repository. Then, you can install Alphabet FileList as an installable package with `pip`:

```bash
(venv) $ python -m pip install -e .
```

You can verify that the installation was succesful by running the `filelist` command in your terminal.

To install all development requirements, run this command:

```bash
(venv) $ python -m pip install -r requirements.txt
```


## Code Conventions

To stick to the same code conventions of this Repo, please run `black`, `isort`, and `flake8` before committing changes:

```
(venv) $ black . && isort . && flake8
```

With this command, `black` and `isort` will fix any formatting in the files of the current working directory and its subdirectories. After that, you may need to fix the errors that `flake8` points out.
