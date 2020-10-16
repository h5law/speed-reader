#!/usr/bin/env python3
import sys
import time
import argparse
import numpy as np
from pathlib import Path

class Node:
    def __init__(self, data):
        self.item = data
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

    def read_list_from_start(self, wpm):
        if self.start_node is None:
            print("List has no elements")
            return
        else:
            n = self.start_node
            counter = 0
            start_time = time.time()
            total_time = self.length / (wpm * 60)
            while n is not None:
                counter += 1
                elapsed = time.time() - start_time
                print(f"-> {n.item}")
                print(f"{round(elapsed, 2)}s")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                time.sleep(get_wait_time(n.item, wpm))
                if n.nref is not None:
                    n = n.nref
                else:
                    taken = time.strftime("%Hh:%Mm:%Ss", time.gmtime(elapsed))
                    print(f"{self.length} words read in {taken}")
                    return


def get_wait_time(word, wpm):
    if len(word) <= 0:
        return 1/8
    else:
        return (np.log(len(word)) / ((wpm / 60) * 1.75))

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='reader',
            description="A speed reader implemented in Python")
    parser.add_argument('-i', '--input', action='store', type=Path,
            help="Input file to read from")
    parser.add_argument('-w', '--wpm', action='store', type=int,
            default=160, help="Words to display per minute")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"{__file__}: Input file `{args.input}' doesn't exist")
        exit(1)
    elif not args.input:
        print(f"{__file__}: No input file provided");
        exit(1)

    # create new DLL
    speed_reader = Reader()

    # read file into DLL structure
    array = file_to_array(args.input)
    array_to_dll(array, speed_reader)

    # read through DLL
    speed_reader.read_list_from_start(args.wpm)
