import subprocess

yandex = ['ping', 'yandex.ru']
youtube = ['ping', 'youtube.com']

ping = subprocess.Popen(yandex, stdout=subprocess.PIPE)
for line in ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

ping = subprocess.Popen(youtube, stdout=subprocess.PIPE)
for line in ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))