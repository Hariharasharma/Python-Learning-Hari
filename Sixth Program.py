firstname = raw_input()
secondname = raw_input()
def stringlength (xyz):
    length = 0
    for i in xyz:
        length = length + 1
    return length
a=stringlength(firstname)
b=stringlength(secondname)
if a > b:
    print firstname
else:
    print secondname




