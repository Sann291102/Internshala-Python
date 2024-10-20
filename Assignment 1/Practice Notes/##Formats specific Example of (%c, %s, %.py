##Formats specific Example of (%c, %s, %i, %d, %u, %o, %x)
## Eg for %c(Character)

(print("The letter that comes after d is",('e')))

## Eg for %s(string conversion via str() prior to formatting)
balltype = 'Basketball'
result = 'hit'
print('I wondered why the %s was getting bigger. Then it %s me.' %(balltype, result))

##Eg 2

print("%20s"%('internshala',))
print("%-20s"%('Internshala',))
print("%.5s"%('Internshala',))

## Eg for %i(Signed decimal integer (%i is identical to %d))

##Eg for %d(Signed Decimal integer)

match=12553
site='ebay'
print("%s is so useless. I tried to look up lighters and all they had was %d matches." % (site, match))

