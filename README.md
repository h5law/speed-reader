# speed-reader

This is a simple speed reader that takes input from a TXT file and reads through it, word by word.

## Installation

### git

```$ git clone https://github.com/h5law/speed-reader.git```

```$ cd speed-reader```

```$ pip install .```


## Usage

```$ speed-reader --help```


```Usage: speed-reader [OPTIONS] PATH```

```Options:```
```  --version      Show the version and exit.```
```  --wpm INTEGER  Read at specified WPM, defaults to 160```
```  --help         Show this message and exit.```


## Bugs

Currently the way I am calculating how long each word stays on the screen works perfectly for 160WPM (speed reading pace on wikipedia), but when changing the pace to 130WPM or another speed it doesn't match that pace. To fix this I must work out a nice algorithm that can weight each word? Help on this would be appreciated.

Also packaging the project for PyPi has lead to an error when installing from the PyPi index, but not when installed as shown above. See [Here](https://stackoverflow.com/questions/64405685/how-to-fix-a-modulenotfounderror-when-packaging-a-python-app-for-pypi) for details on this issue.


## Other
You can find the project homepage on [GitHub](https://github.com/h5law/speed-reader)

## Author
[h5law](https://github.com/h5law)