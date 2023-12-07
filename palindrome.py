# palindrome.py


def is_palindrome(string):
    ignore_chars = list(" ?!.,:;")
    ignore_chars_table = {ord(c): "" for c in ignore_chars}
    processed_string = string.lower().translate(ignore_chars_table)

    return processed_string == processed_string[::-1]
