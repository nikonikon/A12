import hashlib
import time

m2 = hashlib.md5()
tmpd = {'UID': 'AAA', 'ATime': time.time(), 'AID': 'FSAG'}
m2.update(tmpd.__str__().encode())
print(m2.hexdigest())