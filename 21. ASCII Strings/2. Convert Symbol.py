"""
replace symbol to '-'
"""

string = "dhgdewgfbwefhu  ewfi23^482661y8y@@$!$T"
result = ""
for ch in string:
    ascii_code = ord(ch)
    if (
        (ascii_code >= 32 and ascii_code <= 47)
        or (ascii_code >= 58 and ascii_code <= 64)
        or (ascii_code >= 91 and ascii_code <= 96)
        or (ascii_code >= 123 and ascii_code <= 126)
    ):
        result += "-"
    else:
        result += ch
print(result)
