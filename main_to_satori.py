import requests

address = input()
tests = requests.get(address)

tests.raise_for_status()

playFile = open('tests.zip', 'wb')
for chunk in tests.iter_content(100000):
    playFile.write(chunk)
playFile.close()
