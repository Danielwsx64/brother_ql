from brother_ql.reader import interpret_response

first = b'\x80 B490\x04\x00\x00\x00>\n\x00\x00#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81\x00\x00\x00\x00\x00\x00'
secod = b'\x80 B490\x04\x00\x00\x00>\n\x00\x00#\x00\x00\x00\x06\x01\x00\x00\x00\x00\x00\x81\x00\x00\x00\x00\x00\x00'
third = b'\x80 B490\x04\x00\x00\x00>\n\x00\x00#\x00\x00\x00\x02\x01\x00\x00\x00\x00\x00\x81\x00\x00\x00\x00\x00$'


data1 = bytes(first)
data2 = bytes(secod)
data3 = bytes(third)

print(data1[8])
print(data1[9])

print(data2[8])
print(data2[9])

print(data3[8])
print(data3[9])


qlr.add_switch_mode()
qlr.add_invalidate()
qlr.add_status_information()

# print(interpret_response(first))
# print(interpret_response(secod))
# print(interpret_response(third))
