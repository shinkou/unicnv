# Unicode Official Document Converter

## How To Use

### Install

Change to the `dist` directory the issue the following commands:

```
$ python setup.py test
$ pip install .
```

### Run

```
$ unidoc-utf16 /path/to/input/data/file
```

### Prepare a Docker Image

You can also prepare a Docker image if you don't want to install on your
host machine.  Simply change to the top directory and run:

```
$ docker build -t TAG .
```

where _TAG_ can be simply *shinkou/unicnv*.

### Run from the Docker Image

Issue the following command to run:

```
$ docker run -v "/directory/to/mount:/data" --rm -i TAG \
  /relative/path/to/input/data/file
```
