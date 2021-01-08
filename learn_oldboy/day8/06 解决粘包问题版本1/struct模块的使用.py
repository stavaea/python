import struct


headers=struct.pack('i',132333)
# print(headers,len(headers))

res=struct.unpack('i',headers)
print(res[0])