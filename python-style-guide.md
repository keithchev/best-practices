
# Python style guide overview

### Naming conventions
- Variable names should be descriptive and generally should not include the type of the variable
- Variable names and function names are all lower case with underscores separating words
- Do not name variables l, O, or I because they are hard to distinguish from ones and zeros
- Class names are in PascalCase


```python

```

### Comments
- Avoid in-line comments; put the comment directly above the code
- Avoid excessive comments that state the obvious

### Spaces
- Generally, put single spaces around binary operators, unless omitting space improves readability. 
For example, `x**2 + y**2`. Low precedence operators should have space.

- Assignment operators should always have single spaces around them except when in keyword arguments. E.g., no space in `f(x, y=4)`. 

- Put spaces after commas in function definitions and calls. This also applies for lists, tuples, NumPy arrays, etc. 


```python
# use spaces after commas in lists
gene_names = ['MTOR', 'CLTA']

# dictionaries should have spaces after the colons and the commas
gene_name_ids = {'MTOR': 1, 'CLTA': 2}

# use spaces around the assignment operator...
filepath = '/Users/keith.cheveralls/temp.csv'

# ...except in the context of specifying a keyword argument
some_method(filepath='/Users/keith.cheveralls/')
```


```python
# use spaces around low-precedence operators like plus and minus,
# but not higher-precedence operators like * and **
# (there is some wiggle room on this; use whatever is more readable)

# this is hard to read (too little space)
c = a**2+b**2

# this is also hard to read (too much space)
c = a ** 2 + b ** 2

# this is 'just right'
c = a**2 + b**2
```

### Blank lines
- Use a single blank line to separate logical sections of your code.
- Put two blank lines between functions in a .py file.

### Example
This example has cryptic variable names, inline comments, and inconsistent and missing spaces. 


```python
seq='AUCUGUACUAAUGCUCAGCACGACGUACG'
c='AUG'  # This is the start codon
i =0  # Initialize sequence index
while seq[ i : i + 3 ]!=c:
    i+=1

print('The start codon starts at index', i)
```

#### The same example, well-formatted


```python
start_codon = 'AUG'

# initialize the sequence index
ind = 0

# scan the sequence until we hit the start codon
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

### Breaking up long lines


```python
# this is hard to read
months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
          'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
          'November': 11, 'December': 12}
```


```python
# this is easy to read
months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}
```


```python
load_files(
    filepath='/Users/keith.cheveralls/image-data/', 
    file_type='Micromanager', 
    output_format='JPG')
```
