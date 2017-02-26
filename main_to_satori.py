import requests

address = input()
tests = requests.get(address)
try:
    tests.raise_for_status()
except Exception as exc:
    print(exc)

playFile = open('tests.zip', 'wb')
for chunk in tests.iter_content(100000):
    playFile.write(chunk)
playFile.close()
