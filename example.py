from patinput import patinput

def pattern(char: int, pos: int, inp: str):
    if pos == 0 and char == b'-'[0]:
        return True
    if char == b'.'[0] and '.' not in inp:
        return True
    return char in b"0123456789"


user_input = patinput(pattern, "Please enter a float number: ", str(22.11))
print("Entered Input:", float(user_input))
