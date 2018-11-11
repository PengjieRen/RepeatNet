import random
import codecs
import os


seed = 123456
random.seed(seed)

train = codecs.open('train.artist.txt', encoding='utf-8', mode='w')
dev = codecs.open('dev.artist.txt', encoding='utf-8', mode='w')
test = codecs.open('test.artist.txt', encoding='utf-8', mode='w')
with codecs.open('all.artist.txt', encoding='utf-8') as f:
    for line in f:
        r=random.random()
        if r<0.1:
            dev.write(line + os.linesep)
        elif 0.2>r>=0.1:
            test.write(line + os.linesep)
        else:
            train.write(line + os.linesep)

train.close()
dev.close()
test.close()

