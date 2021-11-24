# CS4364_assignment_3

## Project purpose

We have used inverted index to answer Boolean queries. We will use it in this assignment. For a set of given input files, write a program to create an inverted index and respond to user queries.
You will be given:

1. Documents to be indexed in a data directory. Each document in that directory will be a represented using a txt file.
2. User queries in a query.txt file. Each query will be composed of two query terms joined by either an AND or OR.

## Tasks

1. Write a program that generates an inverted index from data files and writes the index in a file named index_lastname.txt (lastname should be replaced by your last name)

   1. The file should have the following format
      t1 d1, d2, d3 t2 d2, d4 t3 d1, d5, d6
      … ……
      tn d1, d8, di where t1 is term1 and d1 is document1.

   2. It is up to you to decide how you want to implement the dictionary and postings. Efficiency is not the major concern for this assignment. 3. Using the queries found in the query.txt file, the program should return the document IDs for the successful queries. Write the results in a file named answer.txt. Use and update the intersection algorithm introduced in the class. The query file should have the following format q1 d1, d3 q2 d1
      q3 -1 where q1 is the first query.
   3. Return -1 for unsuccessful queries.

2. You may use the porter stemmer from the NLTK package.
3. Do not use any stopword list. That is, do NOT remove the stop words.

## Example Usage

- you can run this file, by simply running python 3 and the filename

```
        python3 ./delgado_john.py
```

## Output

It will output 2 files to the output directory in the root directory with
the naming convention of `index_lastname.txt.` and `answer.txt`

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## References/Tools

- https://regex101.com/

## License

Distributed under the Apache License. See `LICENSE` for more information.
