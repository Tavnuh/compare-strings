# CompareStrings

CompareStrings accepts either two strings or two Pandas Series' containing 
strings, as inputs, and provides a simple way to tell how similar or dissimilar 
two strings are.

By default, the compare_strings function returns the Levenshtein Distance 
between the strings, divided by the length of the first string, with a min and 
max value of 0 and 1 respectively, where 0 represents absolute similiarity, 
and 1 represents maximum dissimilarity.

Optional argument 'method' allows selection of alternative methods of 
calculation, such as the true Levenshtein distance, or the cosine distance. 

The email argument takes 1 or 2 as values, and indicates to the function that 
either string (or series) 1 or 2 contain an email address. When this argument
is used, the string that contains an email address is split on the '@' and the
email domain is discarded before the calculation is performed.

Precision argument is used to determine the precision of the resulting float.

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
### Strings: 
`compare_strings` supports indivdual strings as inputs. Examples: 

```python
from CompareStrings import compare_strings
```

```method='lev_abs'```
```python
# Levenshtein Distance

compare_strings('string one','string', method='lev_abs')
```
`Out[1]: 4`

*There were 4 additions, deletions or substitutions required to change the first
string into the second*

```method='lev_props'```
```python
# Levenshtein Distance as a proportion of the length of the first string (0 - 1)

compare_strings('string one','string', method='lev_props')
```
`Out[1]: 0.4`

*There were 4 additions, deletions or substitutions required to change the first
string into the second string, and 10 characters in the first string.*

### Pandas Series:
`compare_strings` also accepts pandas series as inputs. It will return a new
DataFrame containing the inputs and a new column with the output. 

The `email` argument can be used to tell the function if one of the inputs
contains an email address, and performs some preprocessing to remove the 
domain.

Without `email` set:

|      |  email                           | full_name             |   levenshtein_proportions |
|-----:|:---------------------------------|:----------------------|--------------------------:|
| 6203 | magnus_jonsson@hotmail.com       | Magnus  Jonsson       |                      0.46 |
| 8990 | susanne_svensson@hotmail.com     | Susanne  Svensson     |                      0.43 |
| 6769 | marie.eriksson@hotmail.com       | Marie  Eriksson       |                      0.46 |
| 2552 | elisabeth.henriksson@hotmail.com | Elisabeth  Henriksson |                      0.38 |

With `email = 1` set:

|      |  email                           | full_name             |   levenshtein_proportions |
|-----:|:---------------------------------|:----------------------|--------------------------:|
| 6203 | magnus_jonsson@hotmail.com       | Magnus  Jonsson       |                         0 |
| 8990 | susanne_svensson@hotmail.com     | Susanne  Svensson     |                         0 |
| 6769 | marie.eriksson@hotmail.com       | Marie  Eriksson       |                         0 |
| 2552 | elisabeth.henriksson@hotmail.com | Elisabeth  Henriksson |                         0 |

Passing `1` to the `email` argument tells the function to ignore the characters 
after and including the '@' in the first column when performing the calculation.

## Contribution
This is my very first python package so contributions are very much welcome. 
Suggestions include: 
- Documentation incl. tidying up docstrings and comments
- Additions to the big_names_list
- Support for names in other languages
- New similarity measures 
- Support or suggestions for other use cases