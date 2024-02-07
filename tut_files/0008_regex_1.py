'''
Credits: Dr. Chuck Py4e
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
'''

import re
import string

print("\nWithout using re:")
file_handle = open("mbox-short.txt")
count = 0
numbers = string.digits


print("\nstr.FIND() 'From:':")  # prints full lines containing 'From:'
for line_x in file_handle:
    line_x = line_x.rstrip()

    if line_x.find("From:") > -1:
        count += 1
        print(line_x, count)


print("\nUsing re:")
file_handle = open("mbox-short.txt")
count = 0
re_search_results = ""
re_findall_results = []
re_findall_numbers = []
re_greedy_matching = []
re_non_greedy_matching = []
re_fine_tune_str_extraction = []
re_fine_tune_str_extraction_non_greedy = []
re_fine_tune_using_parantheses = []

print("\nre.SEARCH() 'From:':")  # prints full lines containing 'From:'
for line_x in file_handle:
    line_x = line_x.rstrip()

    if re.search("From:", line_x):
        count += 1
        print(line_x, count)

    re_search_fn = re.search("^X-\S+:", line_x)
    re_greedy_matching += re.findall("^F.+:", line_x)
    re_non_greedy_matching += re.findall("^F.+?:", line_x)
    re_fine_tune_str_extraction += re.findall("\S+@\S+", line_x)
    re_fine_tune_str_extraction_non_greedy += re.findall("\S@\S+?", line_x)
    re_fine_tune_using_parantheses += re.findall("^From (\S+@\S+)", line_x)
    re_findall_results += re.findall("^X-\S+:", line_x)
    re_findall_numbers += re.findall("[0123456789]+", line_x)
    # re_findall_numbers += re.findall("[numbers]+", line_x) # doesn't work, searches for chars in 'numbers'

    if re_search_fn is None:
        continue
    else:
        # print(re_search_fn)  # prints out re.Match object
        re_search_results += re_search_fn.string


print("\nre.SEARCH() results:")  # prints full lines containing regexpr
print(re_search_results)

print("\nre.FINDALL() results:")  # prints only phrases matching regexpr
print(re_findall_results)

print("\nre.FINDALL() number results:")  # prints all digit matches
print(re_findall_numbers)

print("\nre.FINDALL() Greedy matching results:")  # greedy matching
print(re_greedy_matching)

# non-greedy matching uses "?" character
print("\nre.FINDALL() Non-greedy matching results:")
print(re_non_greedy_matching)

# fine tuning string extraction
print("\nre.FINDALL() Fine-tuning string extraction:")
print(re_fine_tune_str_extraction)

# non-greedy fine tuning string extraction
print("\nre.FINDALL() NON-GREEDY Fine-tuning string extraction:")
print(re_fine_tune_str_extraction_non_greedy)

# Only parantheses part is extracted
print("\nre.FINDALL() Fine-tuning string extraction with parantheses:")
print(re_fine_tune_using_parantheses)


s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst1 = re.findall('\S+@\S+', s)
print("\nre.FINDALL() example:")
print(lst1)

lst2 = re.findall('\\S+@\\S+', s)
print("\nre.FINDALL() example:")
print(lst2)

if lst1 == lst2:
    print("yes")
    print(id(lst1))
    print(id(lst2))
else:
    print("no")
    print(id(lst1))
    print(id(lst2))

data = "From zqian@umich.edu Fri Jan  4 16:10:39 2008"

# [^ ] --> Not a blank character
re_findall_at_sign = re.findall('@([^ ]*)', data)
print("\nre.FINDALL() @ sign one way:")
print(re_findall_at_sign)

re_findall_at_sign = re.findall('^From .*@([^ ]*)', data)
print("\nre.FINDALL() @ sign second way:")
print(re_findall_at_sign)
