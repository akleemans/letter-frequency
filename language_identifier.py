# -*- coding: utf-8 -*-
'''
Tries to identify a language from a small subset of languages, based on the wikipedia table
https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_other_languages
'''
from __future__ import division
__author__ = "Adrianus Kleemans"

def analyze(textfile):
    # read csv
    with open('letter_frequency.csv') as myfile:
        content = myfile.readlines()
    data = []
    for line in content:
        data.append(line.strip().split(';'))

    all_letters = []
    for i in range(1, len(data)):
        all_letters.append(data[i][0])

    languages = []
    for i in range(1, len(data[0])):
        languages.append(data[0][i])

    # calculate
    with open(textfile) as myfile:
        content = myfile.readlines()
    dic = {}
    total = 0
    for line in content:
        for letter in line:
            letter = letter.lower()
            if letter in all_letters:
                total += 1
                if letter in dic: dic[letter] += 1
                else: dic[letter] = 0

    # normalize
    for letter in dic:
        dic[letter] = dic[letter] / total
    #print 'Letter frequency in text:', dic

    # calculate
    scores = {}
    for i in range(len(languages)):
        language = languages[i]
        score = 0.0
        # calculate square error
        for l in range(len(all_letters)):
            letter = all_letters[l]
            expected = float(data[l+1][i+1].split('%')[0])/100.0
            if letter in dic: score += (dic[letter] - expected)**2
            else: score += expected**2
        scores[language] = score

    print 'Scores for', textfile, ':'
    for language in sorted(scores, key=scores.get):
        print language + ': MSE', round(scores[language], 4), '|', round(1 / scores[language], 1), 'points'

if __name__ == "__main__":
    for textfile in ['nl_columbus.txt', 'it_boccaccio.txt', 'fi_kivi.txt']:
        analyze('snippets/' + textfile)
