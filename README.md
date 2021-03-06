# PatInput

This package provides functions and tools to get input from standard input, like the input function. Furthermore, this package allows you to define a pattern and force user to enter the input in a defined pattern and restrict entering illegal characters as the input.

## Define Input Pattern
A pattern is defined as a function with three arguments which returns boolean. This function determines which character is allowed in defined position and situation. The first argument is the input character's ASCII code. The second one is the position of the cursor and the last one is the input string until that moment. Finally, returns True value if the input character is legal in this state and otherwise returns False value.
For example, if you want to get an positive only integer you can do it like this:
```
digits = b"0123456789"
pattern = lambda char, pos, inp: char in list(digits)
```
Or,
```
def pattern(char: int, pos: int, inp: str):
    return char in b"0123456789"
```
Or if you want your users can enter negative integers also,  you can do it like this:
```
def pattern(char: int, pos: int, inp: str):
    if pos == 0 and char == b'-'[0]:
        return True
    return char in b"0123456789"
```
Now, if you want your users to enter float numbers, you can do it as mentioned below:
```
def pattern(char: int, pos: int, inp: str):
    if pos == 0 and char == b'-'[0]:
        return True
    if char == b'.'[0] and '.' not in inp:
        return True
    return char in b"0123456789"
```
This pattern is like the previous one but it allows the user to enter a maximum of one dot (`.`) at the input.

### Pattern tools
In addition, you can use the pre-defined functions and byte strings that are defined in `patinput.input_pattern` to make patterns in an easier way. 

#### Pre-defined byte strings
There are some pre-defined byte strings that represent useful sets. These byte strings are listed below.
```
ASCII_EXTENDED = bytes(range(128, 255))
LOWER_ALPHABETS = b"abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABETS = LOWER_ALPHABETS + UPPER_ALPHABETS
DIGITS = b"0123456789"
LEGAL_SIGNS = b"~!@#$%^&()_+=-`;'.,}{[]"
ILLEGAL_SIGNS = b"\\/:*?\"<>|"
SIGNS = LEGAL_SIGNS + ILLEGAL_SIGNS
SPACE = b" "
```

#### Pre-defined patterns
There are some pre-defined patterns (functions) that represent useful patterns. These patterns are listed below:
- `patinput.input_pattern.ALOW_NUMBERS` is the pattern of digit-only inputs.
- `patinput.input_pattern.ALOW_ALPHABETS` is the pattern of alphabet-only inputs.
- `patinput.input_pattern.ALOW_NOSPACE` is the pattern of strings that does not include spaces and illegal signs which are useful for file names.

## Getting Input From STDIN
After defining pattern you should get input from STDIN. The function which get this input is `patinput.patinput` and accepts these arguments:


| Argument Name |  Type  | Default | Description |
| -----------   | ------ |  -----  |  ---------  |
| `allowness`   | `Callable(int, int, str) -> bool` | the function returns `True` always. | A function that determines which character is allowed in defined position and situation (Pattern function). |
| `prompt`      | String                            | `""`  | If the prompt argument is present, it is written to standard output without a trailing newline. |
| `default`     | String                            | `""`  | The default value that is pre-typed in input field. |
| `interrupt`   | `Callable(int, int, str) -> bool` | the function returns `False` always. | A function that determines when the input getting procedure must interrupt. |
| `ends_nl`     | Boolean                           | `True`| After receiving input from the user, print a new line, if this argument is True. |

For example, if want to use the pattern that we defined before to get float numbers from the user, we can do something like this:

```
from patinput import patinput

def pattern(char: int, pos: int, inp: str)
    if pos == 0 and char == b'-'[0]:
        return True
    if char == b'.'[0] and '.' not in inp:
        return True
    return char in b"0123456789"


user_input = patinput(pattern, "Please enter a float number: ")
```