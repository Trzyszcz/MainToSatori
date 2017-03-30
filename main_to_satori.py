import requests
import zipfile
import os

def test_name_tuple(name):
    answer0 = ''
    for char in name:
        if char == '.':
            return (answer0, name[len(answer0):])
        else:
            answer0 += char

address = input()

if not address[0:7] == 'http://':
    address = 'http://' + address

tests = requests.get(address)

tests.raise_for_status()

playFile = open('tests.zip', 'wb')
for chunk in tests.iter_content(100000):
    playFile.write(chunk)
playFile.close()

cwd = os.getcwd()

path_main = os.path.join(cwd, 'Problem')

os.makedirs(path_main)

Tests_file = zipfile.ZipFile('tests.zip', 'r')
Tests_file.extractall(path_main)
Tests_file.close()

tests_names = []

os.chdir(path_main)

list_of_tests = os.listdir()
list_of_tests = sorted(list_of_tests)

for test in list_of_tests:
    tnt = test_name_tuple(test)
    if tnt[0] in tests_names:
        os.rename(test, (str(tests_names.index(tnt[0]) + 1) + tnt[1]))
    else:
        tests_names.append(tnt[0])
        os.rename(test, (str(len(tests_names)) + tnt[1]))

io_archive = zipfile.ZipFile(os.path.join(path_main, 'io.zip'), 'w')
for number in range(len(tests_names)):
    io_archive.write(str(number + 1) + '.in')
    io_archive.write(str(number + 1) + '.out')
io_archive.close()

tests_yaml_file = open('tests-multi.yaml', 'w')
tests_yaml_file.write('1-' + str(len(tests_names)) + ':\n')
tests_yaml_file.write('  judge   : !file ../common/multijudge.py\n')
tests_yaml_file.write('  io      : !file io.zip\n')
tests_yaml_file.write('  memory  : 128MB\n')
tests_yaml_file.write('  time    : 5s')
tests_yaml_file.close()



