import sys

commands = {
    'reverse' : 4,
    'copy' : 4,
    'duplicate-contents' : 4,
    'replace-string' : 5
}

input_command = sys.argv

command_name = input_command[1]
command_length = len(input_command)
path_name = input_command[2]

def read_contents(pathname):
    with open(pathname) as f:
        contents = f.read()
    return contents


if command_name in commands and command_length == commands[command_name]:

    if command_name == 'reverse':
        reversed_contents = read_contents(path_name)[::-1]
        with open(input_command[3], 'w') as f:
            f.write(reversed_contents)

    elif command_name == 'copy':
        copied_contents = read_contents(path_name)
        with open(input_command[3], 'w') as f:
            f.write(copied_contents)

    elif command_name == 'duplicate-contents':
        duplicated_contents = read_contents(path_name)
        with open(path_name, 'a') as f:
            for i in range(int(input_command[3])):
                f.write(duplicated_contents)
            
    elif command_name == 'replace-string':
        contents = read_contents(path_name)
        with open(path_name, 'w') as f:
            f.write(contents.replace(input_command[3], input_command[4]))

else:
    print('Error: Please input the correct command and argument as specified in the README.md', file=sys.stderr)
    sys.exit(1)
