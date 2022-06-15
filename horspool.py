import string
MY_ALPHABET=list(string.ascii_letters+'!?,. ;:""()/'+"'"+'\n')
def shiftTable(pattern):
    table=dict()
    m=len(pattern)
    for char in MY_ALPHABET:
        table[char]=m
    for i in range(m-1):
        table[pattern[i]]=m-1-i
    return table
def main(text, pattern):
    table=shiftTable(pattern)
    n=len(text)
    m=len(pattern)
    i=m-1
    while i<=n-1:
        k=0        #кількість співпадаючих символів
        while k<=m-1 and pattern[m-1-k]==text[i-k]:
            k+=1
        if k==m:
            return i-m+2
        else:
            i+=int(table[text[i]])
    return -1
f=open('text.txt', 'r')
s=''
for line in f:
    s+=line
f.close()
pattern='honc'
print(main(s, pattern))
