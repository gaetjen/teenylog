#!/usr/bin/python3
# Simple tool to edit logfiles created with teenylog. Allows adding tags and redacting.
import sys


TAGS = {'s': "self/thoughts",
        'p': "interaction with other people",
        'm': "music / audio",
        'f': "film/movies",
        'w': "written text / reading"}

COMMANDS = {'r': "redact",
            'd': "delete",
            'q': "quit (only write the lines processed so far)"}
            # 'b': "back one line"}

REDACT_TEXT = "REDACTED"

NEW_PREFIX = "milled_"

TAG_OPEN, TAG_CLOSE = '{', '}'


def print_instructions():
    """Print reference for commands"""
    print("The file will be printed line by line. For each line input all the tags/instructions and press Enter.")
    print("Use the following tags:")
    for k, v in TAGS.items():
        print("{}: {}".format(k, v))
    print("Special commands:")
    for k, v in COMMANDS.items():
        print("{}: {}".format(k, v))
    print()


def get_tag_input():
    input_ok = False
    while not input_ok:
        inp = input('Your tags: ')
        input_ok = True
        for c in inp:
            if c not in TAGS.keys() and c not in COMMANDS.keys():
                print("Unknown tag/command: {}; Try again!".format(c))
                input_ok = False
                break
    if 'q' in inp:
        return None
    else:
        return inp


def process_line(line, tags):
    date_str = line[:18]
    content = line[18:].strip()
    if 'd' in tags:
        return None
    if 'r' in tags:
        content = REDACT_TEXT
    tag_str = ' ' + TAG_OPEN
    for c in tags:
        if c in TAGS.keys():
            tag_str += c
    return date_str + content + tag_str + TAG_CLOSE


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Provide file name!")
    else:
        logfile = sys.argv[1]
        edited_lines = []
        print_instructions()
        try:
            with open(sys.argv[1], 'r') as f:
                for line in f:
                    print(line, end='')
                    tags = get_tag_input()
                    if tags is not None:
                        new_line = process_line(line, tags)
                        if new_line is not None:
                            edited_lines.append(new_line)
                    else:
                        break

        except FileNotFoundError:
            print("File {} does not exist!".format(logfile))

        boardfile = NEW_PREFIX + logfile
        print("Done! Writing output to {}".format(boardfile))
        with open(boardfile, 'w') as f:
            f.writelines(l + '\n' for l in edited_lines)
