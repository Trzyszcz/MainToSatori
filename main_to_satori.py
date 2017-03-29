import requests
import zipfile
import os

address = input()
tests = requests.get(address)

tests.raise_for_status()

playFile = open('tests.zip', 'wb')
for chunk in tests.iter_content(100000):
    playFile.write(chunk)
playFile.close()

path0 = os.getcwd() + '/Tests_main'

os.makedirs(path0)

Tests_file = zipfile.ZipFile('tests.zip', 'r')
Tests_file.extractall(path0)
Tests_file.close()


