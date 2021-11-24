'''
FileName: query_processing.py
Author: John Delgado
Created Date: 11/20/2021
Version: 1.0 Initial Development
'''

from pathlib import Path
from typing import cast
from functions import load_and_format_data as lnf
import pprint


def query_processing(inverted_index):
    # first we need to get all the queries to perform from our query file
    tokenized_queries = read_queries_from_file()
    print("Query dictionary:")
    pprint.pprint(tokenized_queries, indent=4, width=100, sort_dicts=False)
    results = perform_queries_on_inverted_index(
        tokenized_queries, inverted_index)
    return results


def read_queries_from_file():
    # Here we are going to tokenize our queires, and then
    # create our query dictionary
    query_file_path = Path(
        __file__).parent.parent / 'queries' / 'query.txt'
    print("Reading query file from: " + str(query_file_path))

    file1 = open(query_file_path, 'r')
    lines = file1.readlines()

    counter = 1
    query_dict = {}
    for line in lines:
        query_name = "q{}".format(counter)
        query_dict[query_name] = lnf.tokenize_input(line.strip())
        counter += 1
    return query_dict


def perform_queries_on_inverted_index(tokenized_queries, inverted_index):
    # now we'll perform the queries and updated our query dictionary with the results
    for key, value in tokenized_queries.items():
        word1 = value[0].lower()
        word2 = value[2].lower()
        compare_operator = value[1].lower()
        print("Word1: {} Word2: {} Comparison operator: {}".format(
            word1, word2, compare_operator))
        try:
            docs_for_word1 = inverted_index[word1]
        except KeyError as ke:
            docs_for_word1 = -1
            print(
                "Word: [{}] is not a key. Query should return -1".format(word1))
        try:
            docs_for_word2 = inverted_index[word2]
        except KeyError as ke:
            docs_for_word2 = -1
            print(
                "Word: [{}] is not a key. Query should return -1".format(word2))
        print("Docs for {}".format(word1))
        print(docs_for_word1)
        print("Docs for word {}".format(word2))
        print(docs_for_word2)

        tokenized_queries[key] = perform_comparison(docs_for_word1, docs_for_word2,
                                                    compare_operator)
    return tokenized_queries


def perform_comparison(docs_for_word1, docs_for_word_2, comparison_operator):

    if comparison_operator == 'and':
        # if either of the lists is -1 then there is no way for the word to be
        # in both lists. We'll return a -1 here.
        if (docs_for_word1 == -1) or (docs_for_word_2 == -1):
            return -1
        else:
            docs_with_both = []
            # We'll iterate through the list of the first word
            # if a doc is in both lists, it is appended to a new list
            # that contain only the docs that have both words
            for doc in docs_for_word1:
                if doc in docs_for_word_2:
                    docs_with_both.append(doc)
            if not docs_with_both:
                docs_with_both = -1
            return sorted(docs_with_both)
    if comparison_operator == 'or':
        # If both docs are -1 then we can return -1
        if (docs_for_word1 == -1) and (docs_for_word_2 == -1):
            return -1
        # If the first keyword is -1 then only return the list of the other word
        elif docs_for_word1 == -1:
            return sorted(docs_for_word_2)
        # If the second keyword is -1 then return the list of the first word
        elif docs_for_word_2 == -1:
            return sorted(docs_for_word1)
        else:
            # Else combind both lists and convert to set so that only unique values are returned
            docs_for_word1.extend(docs_for_word_2)
            return sorted(set(docs_for_word1))
