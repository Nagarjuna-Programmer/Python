# Name: Tammineni Nagarjuna
# Lab 02 - Task 1

import keyword

print("Total number of Python keywords:", len(keyword.kwlist))
print("\nPython Keywords:")

for word in keyword.kwlist:
    print(word)
    """
    Output:
    Total number of Python keywords: 35

Python Keywords:
False
None
True
and
as
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield
    """