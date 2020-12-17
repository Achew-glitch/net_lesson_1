import telnetlib
import time

with telnetlib.Telnet('192.168.0.1') as tn:
    tn.read_until(b'Username:')
    tn.write(b'user\n')

tn.read_until(b'Password:')
tn.write(b'pass\n')

time.sleep(5)

output = tn.read_very_eager().decode('cp866').encode('utf-8')
print(output.decode('utf-8'))


