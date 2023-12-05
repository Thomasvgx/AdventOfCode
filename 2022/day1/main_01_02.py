# Advent of Code template by @MathisHammel

import requests

from aoc_secrets import AOC_COOKIE # Put your session cookie in this variable
YEAR = '2022'

def get_input(day):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}/input', headers={'cookie':'session='+AOC_COOKIE})
    return req.text

def get_example(day,offset=0):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}', headers={'cookie':'session='+AOC_COOKIE})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0]

def submit(day, level, answer):
    input(f'You are about to submit the follwing answer:\n>>>>>>>>>>>>>>>>> {answer}\nPress enter to continue or Ctrl+C to abort.')
    data = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{YEAR}/day/{day}/answer', headers={'cookie':'session='+AOC_COOKIE}, data=data)
    if 'You gave an answer too recently' in response.text:
        print('VERDICT : TOO MANY REQUESTS')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('VERDICT : WRONG (TOO LOW)')
        elif 'too high' in response.text:
            print('VERDICT : WRONG (TOO HIGH)')
        else:
            print('VERDICT : WRONG (UNKNOWN)')
    elif 'seem to be solving the right level.' in response.text:
        print('VERDICT : INVALID LEVEL')
    else:
        print('VERDICT : OK !')

def ints(s):
    return list(map(int, s.split()))

DAY = 1
PART = 2
s = get_input(DAY).strip()

import collections
import math
#import networkx as nx

# print(s.split('\n'))
somme = [0]
i = 0
for element in s.split('\n'):
    if element != '':
        somme[i] = somme[i] + int(element)
    else:
        somme.append(0)
        i += 1
print(sum(sorted(somme)[-3:]))

ans = sum(sorted(somme)[-3:])

submit(DAY, PART, ans)
