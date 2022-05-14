# ChemSay
Spells words using elements on the periodic table.

## Contributors
Reilley Pfrimmer (@b1nwal)

## How I Built It
I was inspired by https://www.chemspeller.com, so I decided to build my own, local version. Here's how it works:

The program uses regex to search through the word for element symbols, and compiles all into a dictionary, the key for each being the starting index for that element in the word. For example, `her` -> `0:['h','he'], 1:['e','er'], 2:['r']}`. Now, finding the best arrangement is the hard part. You cannot use a once-over-pick-longest-symbol, or else `her` -> `[He] + r`, while the ideal arrangement would include the most letters being part of element symbols as possible, meaning `her` -> `[H] + [Er]`. Obviously, you also cannot choose the smallest first either. The solution? Compile all possible arrangements and choose the best.
To do this, I used the following strategy:
```
 for every element in current l
  get current index as c
  for all elements in d[c]
    copy current list
    place d[c] on end of said list
    append this list to placeholder variable n
 l = n
```
where l is our list of combinations. So on step 1, it will look like this: `[['ba'],['b']]` (our example word is bacon)
for every element (i.e. every combination), get the total length of all characters (for `['ba']`, that length would be 2, for `['ba','co']` it would be 4), save this value as `c`.
`d` is our dictionary containing elements organized under starting indexes in the word (a dictionary is the python equiv. of a HashMap.) For the word bacon, `d` will look like `{0: ['ba','b'], 1: ['ac','a'], 2: ['c','co'], 3: ['o'], 4: ['n']}`
so, on step one, with `['ba']` selected, `c` would equal 2, thus `d[c] = ['c','co']`.
for every element in `d[c]`, the program will copy the selected list, place the current selected element of `d[c]` (for step one of this loop for example, that would be `'c'`) at the end of the list, then append it to placeholder variable `n`. by the end of the first step, `n` will look like: `[['ba','c'],['ba','co'],['b','a'],['b','ac']]`
Rinse and repeat until no more changes are being made.
Next evaluate all combinations with the following system:
```
+1 PT PER ELEMENT
+2 PT PER NON-ELEMENT
```
Then, choose the combo with lowest score, meaning it will be the shortest and include the most elements (as opposed to non-elements) as possible.
The rest is all up to displaying it.

## Resources used:
python: (language)
tkinter: (for window)
pyinstaller: (for compiling to executable)
atom: (text editor)
git (github, git bash): (version control)
