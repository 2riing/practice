import sys
sys.stdin=open('input.txt')
import psutil

def memory_usage():
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    return f"{rss: 10.1f} MB"
T = int(input())
for _ in range(T):
    a, b = 1, 2
    print((a**b)%10)

print(memory_usage())