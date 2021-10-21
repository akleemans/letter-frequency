# letter-frequency

This is a python script which tries to identify the language of a text by the frequency of its letter.

See also [**this Blog post**](https://www.kleemans.ch/identifying-language-by-letter-frequency).

This is not in any way an accurate general purpose language identifier, just some hacking around with the table at [Wikipedia: Letter frequencies](https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_other_languages) and only applies to very small subset of languages listed there (list at the end of this readme).

It runs through the text, builds the frequency list for all occurring letters and then calculates [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) (for all letters) for each language.

## Run
Run with `python letter_frequency.py`, here the five top languages for each text snippet.
The script will also generate a graph if matplotlib is installed (optional).

### Scores for nl_columbus_short.txt
>In de prachtige zeestad Genua, de trotsche bijgenaamd, werd
omstreeks het jaar 1435 een knaapje geboren, dat nu in alle landen
als Christophorus Columbus bekend is. (...)

![Pylab-graph](https://github.com/akleemans/letter-frequency/blob/master/columbus.png)

* **Dutch**: MSE 0.0016 | 639.8 points
* German: MSE 0.006 | 166.3 points
* Danish: MSE 0.0076 | 131.6 points
* French: MSE 0.0127 | 78.6 points
* Swedish: MSE 0.0137 | 72.9 points

### Scores for it_boccaccio_short.txt
> Solone, il cui petto un umano tempio di divina sapienzia fu reputato,
e le cui sacratissime leggi sono ancora alli presenti uomini chiara
testimonianza dell'antica giustizia, era, (...)

* **Italian**: MSE 0.0007 | 1503.6 points
* Spanish: MSE 0.0042 | 237.0 points
* French: MSE 0.0057 | 175.9 points
* Esperanto: MSE 0.0068 | 147.4 points
* Portuguese: MSE 0.0072 | 139.4 points

### Scores for fi_kivi_short.txt
> Jukolan talo, eteläisessä Hämeessä, seisoo erään mäen pohjaisella
rinteellä, liki Toukolan kylää. Sen läheisin ympäristö on kivinen
tanner, mutta alempana alkaa pellot, joissa,  (...)

* **Finnish**: MSE 0.002 | 491.5 points
* Esperanto: MSE 0.008 | 124.4 points
* Czech: MSE 0.0144 | 69.6 points
* Swedish: MSE 0.0154 | 65.0 points
* Icelandic: MSE 0.0172 | 58.0 points

The three snippets provided are from [Project Gutenberg](https://www.gutenberg.org/), each one contains only the first 200 lines of the original book.

## Languages
Here's a list of languages in the list, which are checked against an example text:
* French
* German
* Spanish
* Portuguese
* Esperanto
* Italian
* Turkish
* Swedish
* Polish
* Dutch
* Danish
* Icelandic
* Finnish
* Czech
