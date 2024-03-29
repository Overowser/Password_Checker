# Password Checker

This script checks a list of passwords against a password breach API (from https://haveibeenpwned.com/) to see if they have been leaked.

## Requirements
- Python 3
- `requests` library
- `argparse` library
- `hashlib` library

## Usage

To use the script, run the following command:

```
python3 main.py password1 password2 password3 ...
```

Replace `password1`, `password2`, `password3`, etc. with the passwords you want to check.

The script will print out a message indicating whether each password was found in the API's database and, if it was found, how many times it was found.

## Example

Here is an example of using the script to check two passwords:

```
$ python3 password_breach_checker.py tikchbilatiwliwla 123456
tikchbilatiwliwla was NOT found. Carry on!
123456 was found 9999 times... you should probably change your password!
```

## Note
- The maximum length for a password is 128 characters. If a password is longer than 128 characters, it will not be checked and an error message will be printed.
- If a password is empty, it will not be checked and an error message will be printed.
