name='shalu kumari'
v='aeiou'
r=[char for char in name if char in v]
print(r)
r=[char for char in name if char not in v]
print(r)

print(name[::3])
print(name[::-3])
sep='-'.join(name[::2])
print(sep)


