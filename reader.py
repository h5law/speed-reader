#!/usr/bin/env python3
import click
import time
import numpy as np
from pathlib import Path

def file_to_array(path, array):
    print(f"Loading file...")
    with open(path) as f:
        for line in f.readlines():
            for word in line.split(" "):
                array.append(word.strip())


def get_word_wait_time(word, wpm):
    if len(word) <= 3:
        return (0.2)
    else:
        return ((np.log(len(word)) / ((wpm / 60) * 1.6)))


def display_line(word, time):
    click.clear()
    width = click.get_terminal_size()[0]
    print(f"{word:}{time:>{(width - len(word) - 1)}}s")


def read_array(array, wpm):
    total_words = len(array)
    start_time = time.time()
    with click.progressbar(length=total_words) as bar:
        while array[0] is not None:
            elapsed = time.time() - start_time
            display_line(array[0], round(elapsed, 2))
            time.sleep(get_word_wait_time(array[0], wpm))
            array.pop(0)


@click.command()
@click.version_option("1.0.1")
@click.option("--wpm", default=160,
        help="Read at specified WPM, defaults to 160")
@click.argument("path", required=True, type=Path)
def main(path, wpm):
    if not path.exists():
        print(f"'{path}' doesn't exist")
        exit(1)

    words = []
    file_to_array(path, words)
    read_array(words, wpm)


if __name__ == "__main__":
    main()
