#!/usr/bin/env python3
import click
import time
import numpy as np
from pathlib import Path

class Node:
    def __init__(self, data):
        self.word = data
        self.nref = None
        self.pref = None

class Reader:
    def __init__(self):
        self.start_node = None
        self.length = 0

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("Node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node
        self.length += 1

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n
        self.length += 1

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_node.pref = None
        self.length -= 1

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not none:
            n = n.nref
        n.pref.nref = none
        self.length -= 1

    def traverse_list(self, wpm):
        if self.start_node is None:
            print("List has no elements")
            return
        else:
            n = self.start_node
            start_time = time.time()
            total_time = self.length / (wpm * 60)
            while n is not None:
                elapsed = time.time() - start_time
                display_line(n.word, round(elapsed, 2))
                time.sleep(get_word_wait_time(n.word, wpm))
                if n.nref is not None:
                    n = n.nref
                else:
                    taken = time.strftime("%Hh:%Mm:%Ss", time.gmtime(elapsed))
                    print(f"{self.length} words read in {taken}")
                    return

def display_line(text, time):
    click.clear()
    width = click.get_terminal_size()[0]
    word = click.style(text, bold=True, underline=True)
    print(f"{text:}{time:>{(width - len(word)) + 6}}s")


def get_word_wait_time(word, wpm):
    if len(word) <= 3:
        return (0.25)
    else:
        return ((np.log(len(word)) / ((wpm / 60) * 1.65)))

def file_to_array(path):
    line_list = word_list = []
    with open(path) as f:
        line_list = f.readlines()

    line_list = [x.strip() for x in line_list]
    words_list = [x.split(" ") for x in line_list]

    return words_list

def array_to_dll(array, dll):
    for line in array:
        for word in line:
            dll.insert_at_end(word)

@click.command()
@click.version_option("1.0.0")
@click.option("--wpm", default=160,
        help="Read at specified WPM, defaults to 160")
@click.argument("path", required=True, type=Path)
def read(path, wpm):
    if not path.exists():
        print(f"Input file `{path}' doesn't exist")
        exit(1)

    # create new DLL
    speed_reader = Reader()
    # read file into DLL structure
    array = file_to_array(path)
    array_to_dll(array, speed_reader)
    # read through DLL
    speed_reader.traverse_list(wpm)


if __name__ == "__main__":
    read()
