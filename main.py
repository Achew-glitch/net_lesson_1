import subprocess


bytes_s_1 = 'Программа'
print(type(bytes_s_1))
bytes_s_1 = bytes_s_1.encode('utf-8')
print(type(bytes_s_1))
print(f'Bytes of bytes_s_1 = {bytes_s_1}')
bytes_s_2 = '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'
print(f'bytes_s_2 = {bytes_s_2}')
print(f'bytes_s_1 = {bytes_s_1.decode("utf-8")}')

args = ['ping', 'google.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

program = "notepad.exe"
process = subprocess.Popen(program)
code = process.wait()

print(code)

