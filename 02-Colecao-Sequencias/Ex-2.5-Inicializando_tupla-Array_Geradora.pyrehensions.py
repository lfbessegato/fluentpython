symbols = '$óÑ¼ñ'
t = tuple(ord(symbol) for symbol in symbols)
print(t)

##### Array
import array
a = array.array('I',(ord(symbol) for symbol in symbols))
print(a)