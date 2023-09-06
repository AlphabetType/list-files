# Alphabet FileList
A Python CLI script demo containing a little program to list files in a folder.

## Usage

To run Alphabet FileList, you can use the `filelist` command. To see all available arguments you can use the `-h` flag:

```console
$ filelist -h
```

If you want to investigate the command line arguments, then you can check out the [cli.py file](src/alphabet_filelist/cli.py) 

## Installation as a User

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
