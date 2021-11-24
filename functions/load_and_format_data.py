'''
FileName: load_and_format_data.py
Author: John Delgado
Created Date: 11/20/2021
Version: 1.0 Initial Development
'''
import os
from pathlib import Path
import re

master_dict = {}


def load_and_format_data():
    # first we need to iterate through all the text files in our data directory
    data_directory_file_path = Path(__file__).parent.parent / 'data'
    print("Reading data files from: " + str(data_directory_file_path))
    print("List of files to be read: ")
    data_files = os.listdir(data_directory_file_path)
    # Now that we have the data files, let's sort them by name
    data_files.sort()
    print(data_files)

    for file in data_files:
        curr_data_file_file_path = data_directory_file_path / file
        print("Reading From: " + str(curr_data_file_file_path))
        # Now that we're in the file we'll read in the file
        doc = input_from_file(curr_data_file_file_path)
        # now we'll clean the input
        cleaned_doc = clean_input(doc)
        # and then tokenize it. We'll also convert our list to a set, so that only unique words are stored
        tokenized_doc = set(tokenize_input(cleaned_doc))
        create_matrix(tokenized_doc, file)

    return master_dict


def input_from_file(file_path):
    try:
        # open the file read
        input_file = open(file_path, "r")
        # read the input
        input_to_process = (input_file.read())
        # close our open file
        input_file.close()
        # return the input
        return input_to_process
    except FileNotFoundError as fnf:
        print("Input file does not exist at {}. \n {}".format(
            file_path, fnf))


def clean_input(input_to_clean):
    # The first thing we are going to do is to remove all special characters
    # This regex will search for any special character and punctuation and remove them
    # This does not remove apostrophe's as they will be considered words in our case
    special_characters_regex = "[-()\"#/@;:<>{}`+=~|.!?,]"
    first_cleaned_input = re.sub(
        special_characters_regex, "", input_to_clean)
    # Now that we've removed the special characters, Let's convert all our words to lowercase
    second_cleaned_input = first_cleaned_input.lower()
    # Return our cleaned input
    return second_cleaned_input


def tokenize_input(input_to_tokenize):
    # first let's split the strings by whitespace to tokenize them
    list_of_words = input_to_tokenize.split()
    return list_of_words


def create_matrix(tokenized_doc, doc_id):
    for token in tokenized_doc:
        if token not in master_dict:
            master_dict[token] = []
        if token in master_dict:
            master_dict[token].append(doc_id)
