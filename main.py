import requests
import argparse
import hashlib

def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    with requests.get(url) as res:
        res.raise_for_status()
        return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('passwords', nargs='+', help='The passwords to check')
    args = parser.parse_args()

    # Check each password
    for password in args.passwords:
        if not password:
            print('Error: password cannot be empty')
            continue
        if len(password) > 128:
            print(f'Error: password "{password}" is too long (maximum length is 128 characters)')
            continue
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')


if __name__ == '__main__':
    main()
