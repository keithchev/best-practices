
# Python style guide overview <!-- omit in toc -->

- [Variable and function naming style](#variable-and-function-naming-style)
- [Guidelines for chosing names](#guidelines-for-chosing-names)
- [Comments](#comments)
- [Spaces](#spaces)
- [Blank lines](#blank-lines)
- [Examples](#examples)
- [Another example](#another-example)
- [Maximum line length and breaking up long lines](#maximum-line-length-and-breaking-up-long-lines)
  - [Long lists and dictionaries](#long-lists-and-dictionaries)
  - [Long function calls](#long-function-calls)


### Variable and function naming style
Variable names, function names, and module names are always all lowercase with underscores between words. This is often called camel case and it `looks_like_this`. The only exceptions are global variables (which should be used sparingly; see below), which should be in all-caps with underscores (`LIKE_THIS`). Class names, on the other hand, do not include underscores; instead, every word should be capitalized. 


### Guidelines for chosing names
The names of variables, functions, and classes should be as descriptive as necessary. When in doubt, favor descriptiveness over succinctness. In particular, avoid the temptation to use abbreviations or parts of words. Also, variable names should generally not include the type of the variable in the name. 


### Comments
The frequency and extent of comments should be sufficient to clarify anything non-obvious about your code. Generally, well-chosen variable and function names can go a long way to making your code 'self-documenting'; avoid adding comments that simply repeat variable or function names, or otherwise state the obvious. Finally, always put comments directly above the line or block of code, never after a line. 


### Spaces
Put spaces around binary operators, unless omitting space improves readability. For example, writing `x**2 + y**2` is considered clearer than `x ** 2 + y ** 2`. Generally, lower precedence operators (like `+` and `-`) should have spaces around them. 

Assignment operators should __always__ have single spaces around them __except__ when they are used to specify keyword arguments in a function definition or call. For example, always write `f(x, y=4)` and not `f(x, y = 4)`. 

__Always__ put spaces after commas, regardless of the context. This includes commas in lists, tuples, dictionaries, function definitions and function calls. For example, lists should always be written `[1, 2, 3]` and never `[1,2,3]`. Similarly, functions should always be written `f(x, y)` and never `f(x,y)`. Finally, always use a space after the colon in dictionaries. 


Here are more examples of these rules:

```python
# use spaces after commas in lists
gene_names = ['MTOR', 'CLTA']

# dictionaries should have spaces after the colons and the commas
gene_name_ids = {'MTOR': 1, 'CLTA': 2}

# use spaces around the assignment operator...
filepath = '/Users/keith.cheveralls/temp.csv'

# ...except in the context of specifying a keyword argument
some_method(filepath='/Users/keith.cheveralls/')

# use spaces around low-precedence operators like plus and minus,
# but not higher-precedence operators like * and **
# (there is some wiggle room on this; use whatever is more readable)

# this is hard to read (too little space)
c = a**2+b**2

# this is also hard to read (too much space)
c = a ** 2 + b ** 2

# this is generally considered 'just right'
c = a**2 + b**2
```

### Blank lines
Use single blank lines to separate logical sections of code within a function. Exactly where, and how many, such blank lines you use is largely a matter of taste and personal preference. However, never use more than one blank line within a function or method. Use two blank lines (and only two!) between class definitions and one or two blank lines (this is a matter of preference) between function definitions. 


### Examples
This example (borrowed from [here](http://justinbois.github.io/bootcamp/2019/lessons/l18_pep8.html)) violates several best practices: it has cryptic variable names, inline comments, and inconsistent and missing spaces. 

```python
seq='AUCUGUACUAAUGCUCAGCACGACGUACG'
c='AUG'  # This is the start codon
i =0  # Initialize sequence index
while seq[ i : i + 3 ]!=c:
    i+=1

print('The start codon starts at index', i)
```

Here is the same example, but properly styled:
```python
start_codon = 'AUG'

# initialize the sequence index
ind = 0

# scan the sequence until the start codon is reached
while seq[ind:ind + 3] != start_codon:
    ind += 1
    
print('The start codon starts at index %d' % ind)
```


### Another example
These are two definitions of the same function. The first is almost impossible to understand, because the variable names are too short to mean anything, everything is condensed into one line, and there are no comments. 

The second definition, on the other hand, is quite clear, even without many comments, because there is a meaningful docstring (the text beteen the triple quotes) and the variable names are descriptive. 

```python
def qf(a, b, c):
    return -(b-np.sqrt(b**2-4*a*c))/2/a, (-b-np.sqrt(b**2-4*a*c))/2/a

def quadratic_roots(a, b, c):
    """Real roots of a second order polynomial."""

    discriminant_sqrt = np.sqrt(b**2 - 4*a*c)
    root_1 = (-b + discriminant_sqrt) / (2*a)
    root_2 = (-b - discriminant_sqrt) / (2*a)

    return root_1, root_2
```


### Maximum line length and breaking up long lines
Excessively long lines make code very hard to read; for this reason, a maximum line length should be chosen and adhered to. This maximum varies between organizations, teams, and codebases, but is usually between 80 and 100 characters. For personal and/or side projects, 100 characters is probably the most flexible choice. Whatever the maximum is, lines over the maximum length must be broken up, and there are various conventions around the best way to do so. 

#### Long lists and dictionaries
Long lists and dictionaries should be broken up so that the brackets are on their own line and there is one item per line. The items should be indented relative to the brackets. This is easier to illustrate than describe:

```python
# here is a long list
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

# here is the same list, formatted correctly
months =  [
    'January', 
    'February', 
    'March', 
    'April', 
    'may', 
    'june', 
    'july', 
    'august', 
    'september', 
    'october', 
    'november', 
    'december',
]

# here is a dictionary that is too long to appear in one line 
months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5,'june': 6, 'july': 7, 'august': 8,}

# here is the same dictionary, correctly formatted using multiple lines
months = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
}
```

#### Long function calls
Sometimes, a function has so many arguments that defining it or calling it yields a line that is too long. In these cases, there are two options. The first is to break the line at the opening parenthesis, like this:

```python
# this line is too long
process_microscopy_image(filepath='/Users/keith.cheveralls/raw-pipeline-microscopy', file_type='Micromanager')

# break up such lines using a line return after the opening parenthesis
process_microscopy_image(
    filepath='/Users/keith.cheveralls/raw-pipeline-microscopy', file_type='Micromanager')

# aside: the closing parenthesis is sometimes also given its own line
# (this is a matter of taste/preference)
process_microscopy_image(
    filepath='/Users/keith.cheveralls/raw-pipeline-microscopy', file_type='Micromanager'
)

```

Sometimes, there are so many arguments that even this doesn't work - the second line, with the list of arguments, is still too long. In these cases, use one line per argument, like this:

```python
# there are so many arguments that the second line below is too long
process_microscopy_image(
    filepath='/Users/keith.cheveralls/raw-pipeline-microscopy', file_type='Micromanager', output_format='jpeg')

# in these cases, use one line per argument
process_microscopy_image(
    filepath='/Users/keith.cheveralls/raw-pipeline-microscopy', 
    file_type='Micromanager', 
    output_format='jpeg'
)
```
