# Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106 (i.e. 9+99+999+9999)

# Write a test for this function.

def addition(a):
    try:
        a = int(a)
    except ValueError:
        return("Nah that's wrong.")
    a = str(a)
    aa = a + a
    aaa = aa + a
    aaaa = aaa + a
    a = int(a)
    aa = int(aa)
    aaa = int(aaa)
    aaaa = int(aaaa)
    return a + aa + aaa + aaaa