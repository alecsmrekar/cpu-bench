import time
import hashlib
import random
import string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

if __name__ == '__main__':
    repeat = int(1e5) *3
    start = time.time()
    for i in range(repeat):
        input = randomword(30)
        hashlib.sha256(str.encode(input)).hexdigest()
    print('time={:.2f}s'.format(time.time() - start))
