# CompareStrings

CompareStrings accepts either two strings or two Pandas Series' containing 
strings, as inputs, and provides a simple way to tell how similar or dissimilar 
two strings are.\ 
\
By default, the compare_strings function returns the Levenshtein Distance 
between the strings, divided by the length of the first string, with a min and 
max value of 0 and 1 respectively, where 0 represents absolute similiarity, 
and 1 represents maximum dissimilarity.\
\
Optional argument 'method' allows selection of alternative methods of 
calculation, such as the true Levenshtein distance, or the cosine distance. \
\
The email argument takes 1 or 2 as values, and indicates to the function that 
either string (or series) 1 or 2 contain an email address. When this argument
is used, the string that contains an email address is split on the '@' and the
email domain is discarded before the calculation is performed.\
\
Precision argument is used to determine the precision of the resulting float.\
\
## Coming soon: 
- Support for additional alternative measures of similarity
- Support for lists of strings
- check_for_name argument - this is intended for use with the email argument,
and checks that string (or series) for any names that are contained within the 
email username before performing the calculation. This allows the user to 
ignore email user names that don't contain human names.
  

## Installation
```python
pip install CompareStrings
```

## Usage
```python
from CompareStrings import compare_strings

# Levenshtein Distance

compare_strings('string one','string', methond='lev_abs')

# Levenshtein Distance as a proportion of the length of the first string (0 - 1)

compare_strings('string one','string', methond='lev_props')
```

## Contribution
This is my very first python package so contributions are very much welcome. 
Suggestions include: 
- Documentation incl. tidying up docstrings and comments
- Additions to the big_names_list
- Support for names in other languages
- New similarity measures 
- Support or suggestions for other use cases