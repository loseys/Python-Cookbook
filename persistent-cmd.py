import subprocess 
import pathlib 
import time
import os

path_output = pathlib.Path(__file__).parent.absolute() 
proc = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
while True: 
    continue_while = False 
    command = input('# ')
    command = bytes(command + ' ' + f'> ' + str(path_output) + '/output.txt 2>&1' + '\n', encoding='utf-8') 
    try: 
        proc.stdin.write(command) 
        proc.stdin.flush() 
    except subprocess.CalledProcessError as e: 
        continue 
    time.sleep(0.2) 
    with open(str(path_output) + r'\output.txt', 'r') as get_output_terminal:
        string_output = get_output_terminal.read() 
        get_output_terminal.close() 

    print(string_output)
    os.remove(str(path_output) + r'\output.txt')
