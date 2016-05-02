# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # read csv
    with open(frequency_file) as myfile:
        content = myfile.readlines()
    data = []
    for line in content:
        data.append(line.strip().split(';'))

    # TODO calculate frequencies for each letter
    with open(textfile) as myfile:
        content = myfile.readlines()

    # TODO calculate mean squared error
    scores = {}
    for language in languages:
        pass
        ...

    # TODO print scores
    for language in languages:
        print language, scores[language]
