#!/usr/bin/env python3
import sys
import time
import click
from math import log
from pathlib import Path
from os import system, name


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def file_to_array(path, array):
    with open(path) as f:
        for line in f.readlines():
            for word in line.split(" "):
                array.append(word.strip())

def get_word_wait_time(word, wpm):
    wps = wpm / 60
    if len(word) <= 3:
        return (1/12) * wps
    else:
        return ((log(len(word), 2)) / (wps * 1.45))

def display_line(word, time=""):
    width = click.get_terminal_size()[0]
    if time != "":
        time = str(time) + "s"
    print(f"{word:}{time:>{(width - len(word) - 1)}}")

def read_array(array, wpm):
    clear()
    start_time = time.time()
    for word in array:
        elapsed = time.time() - start_time
        display_line(word, round(elapsed, 2))
        time.sleep(get_word_wait_time(word, wpm))
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
    taken = time.strftime("%Hh:%Mm:%Ss", time.gmtime(elapsed))
    display_line(f"Read {total_words} words in {taken}.")

@click.command()
@click.version_option("1.0.5_dev2")
@click.option("--wpm", default=160,
        help="Read at specified WPM, defaults to 160")
@click.argument("path", required=True, type=Path)
def read(path, wpm):
    if not path.exists():
        print(f"'{path}' doesn't exist")
        exit(1)

    words = []
    file_to_array(path, words)
    read_array(words, wpm)


if __name__ == "__main__":
    read()
