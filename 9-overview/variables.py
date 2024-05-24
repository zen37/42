# Variables are dynamically typed
n = 0
print('n =', n)

n = 'abc'
print('n =', n)

# Multiple assignments
n, m = 0, 'abc'
print('n =', n)
print('m =', m)

n, m, z = 0.125, "abc", False
print('n =', n)
print('m =', m)
print('z =', z)

#increment
n = n + 1
print('n =', n)

n += 1
print('n =', n)

# n++ does not work

# None is null (absence of value)
n = 4
n = None
print("n =", n)