import random
import string

filed = string.digits + string.ascii_uppercase

def get_random():
    return ''.join(random.sample(filed,4))
def concatenate(n):
    return '-'.join([get_random() for i in range(n)])
def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__ == '__main__':
    print(generate(2))
