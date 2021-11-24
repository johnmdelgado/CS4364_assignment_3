'''
FileName: delgado_john.py
Author: John Delgado
Created Date: 11/20/2021
Version: 1.0 Initial Development
'''
from functions import load_and_format_data as lnf
from functions import query_processing as qp
import pprint
import os

if __name__ == '__main__':
    inverted_index = lnf.load_and_format_data()
    print("Outputting Inverse Matrix to file")
    with open(os.path.dirname(__file__) +
              '/output/index_delgado.txt', 'w+') as convert_file:
        pprint.pprint(inverted_index, convert_file, indent=4, width=100)
        convert_file.close()
    query_results = qp.query_processing(inverted_index)
    with open(os.path.dirname(__file__) +
              '/output/answer.txt', 'w+') as answer_file:
        pprint.pprint(query_results, answer_file, indent=4,
                      width=100, sort_dicts=False)
        answer_file.close()
