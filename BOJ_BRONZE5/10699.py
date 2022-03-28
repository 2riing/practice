import sys
sys.stdin = open('input.txt')
from datetime import date

today = date.today()
print(f'{today}')