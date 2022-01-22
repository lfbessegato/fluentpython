from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
#print(d_proxy[2]) # Apresenta erro por não existir

# Qualquer mudança em d, é refletido em d_proxy
d[2] = 'B'
print(d_proxy)
print(d_proxy[2])