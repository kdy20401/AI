import os
from bfs import bfs
from hc import hc
from csp import csp


def print_output_file(n, method, solution):
    cwd = os.path.dirname(os.path.realpath(__file__))
    f = open(cwd + '\{}_{}_output.txt'.format(n, method), 'w')

    if solution == []:
        f.write('no solution')
    else:
        output = ''
        for i in solution:  
            output += '{} '.format(str(i))
        output = output[:-1]
        f.write(output)
    f.close()

def main():
    cwd = os.path.dirname(os.path.realpath(__file__))
    f = open(cwd + '\input.txt', 'r')
    lines = f.readlines()
    
    for line in lines:
        arr = line.split(' ')
        n = int(arr[0])
        method = arr[1].strip()
        
        if method == 'bfs':
            solution = bfs(n)
        elif method == 'hc':
            solution = hc(n)
        elif method == 'csp':
            solution = csp(n)
        
        print_output_file(n, method, solution)

if __name__ == '__main__':
    main()