# speed-reader

This is a simple speed reader that takes input from a TXT file and reads through it, word by word.

## Installation

### git

```$ git clone https://github.com/h5law/speed-reader.git```

```$ cd speed-reader```

```$ pip install -r requirements.txt```


## Usage

```$ python3 reader.py --help```


```Usage: reader.py [OPTIONS] PATH```

```Options:```

```  --version      Show the version and exit.```

```  --wpm INTEGER  Read at specified WPM, defaults to 160```

```  --help         Show this message and exit.```


## Bugs

Currently the way I am calculating how long each word stays on the screen works perfectly for 160WPM (speed reading pace on wikipedia), but when changing the pace to 130WPM or another speed it doesn't match that pace. To fix this I must work out a nice algorithm that can weight each word? Help on this would be appreciated.


## Other
You can find the project homepage on [GitHub](https://github.com/h5law/speed-reader)

## Author
[h5law](https://github.com/h5law)
