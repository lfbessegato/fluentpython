# BEGIN STRKEYDICT0
class StrKeyDict0(dict):  # <1>

    def __missing__(self, key):
        if isinstance(key, str):  # <2>
            raise KeyError(key)
        return self[str(key)]  # <3>

    def get(self, key, default=None):
        try:
            return self[key]  # <4>
        except KeyError:
            return default  # <5>

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()  # <6>

# END STRKEYDICT0

# Tests for item retrieval using `d[key] notation`

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d['4'])
# print(d[1])

# Tests for item retrieval using 'd.get(key)' notation
print(d.get('2'))
print(d.get('4'))
print(d.get(1, 'N/A'))

# Tests for the 'in' operator
print(2 in d)
print(1 in d)

