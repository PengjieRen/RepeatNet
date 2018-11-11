import codecs
import os
import pickle
import ast

def load_item(file):
    item2id = {}
    id2item = {}
    with codecs.open(file, encoding='utf-8') as f:
        id = 0
        for line in f:
            name = line.strip('\n').strip('\r')
            item2id[name] = id
            id2item[id] = name
            id += 1

    print 'item size: ', len(item2id), len(id2item)
    return item2id,id2item

class SessionCorpus:
    def __init__(self, file_path,item2id):
        self.dataset = []
        self.file_path=file_path
        self.item2id=item2id

    def load(self):
        count=0
        with codecs.open(self.file_path, encoding='utf-8') as f:
            for line in f:
                lines = line.strip('\n').strip('\r').split('\t')
                input=ast.literal_eval(lines[0])
                input=[self.item2id[str(name)] for name in input]
                output=[self.item2id[lines[1]]]
                self.dataset.append([input,output])
                count+=1
        print 'data size: ',len(self.dataset)
        # self.dataset=sorted(self.dataset, key=lambda s: len(s[0]))
        return self.dataset