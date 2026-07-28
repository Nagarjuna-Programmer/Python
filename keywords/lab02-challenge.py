# Name: Tammineni Nagarjuna
# Lab 02 - Challenge

import keyword

print("Soft Keywords:")

if hasattr(keyword, "softkwlist"):
    for word in keyword.softkwlist:
        print(word)

print("\nHard Keywords:")

for word in keyword.kwlist:
    if not hasattr(keyword, "softkwlist") or word not in keyword.softkwlist:
        print(word)
        """
        Output:
        Soft Keywords:
_
case
match
type

Hard Keywords:
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