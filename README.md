# PyAutoType

PyAutoType is a (for now) macOS only auto typing program. PyAutoType takes any text file and after a user specified amount of time starts typing it simulating a keyboard.


## Usage

### Examples
```
# Begins typing out my_file.txt after 10 seconds in a slightly human way.
pyautotype --file my_file.txt --time 10 --mode humanlike

# Begins typing out my_file.txt as fast as the keyboard driver allows.
pyautotype --mode fast --file my_file.txt
```

### Options
```
--time INTEGER           Number of seconds till typing starts Default: 5.
--file PATH              The file to type out.
--mode [humanlike|fast]  How the program types out the file. Default: humanlike
--help                   Show this message and exit.
```

## Installation

### Requirements
1. Python 2.7
2. pip

### Installation Instructions
1. `git clone https://github.com/mholiv/pyautotype.git`
2. `cd pyautotype`
3. `pip install .`

## Future Features
1. MUCH more human like input
2. Clipboard integration
3. Linux Support
4. Windows Support
