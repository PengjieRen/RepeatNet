
import codecs
from datetime import datetime
import os


items_freq=dict()
items_id=dict()
itemcount=0

with codecs.open('userid-timestamp-artid-artname-traid-traname.tsv', encoding='utf-8') as f:
    for line in f:
        lines = line.strip('\n').strip('\r').split('\t')
        if len(lines) < 5:
            continue
        userid = lines[0]
        time = datetime.strptime(lines[1], "%Y-%m-%dT%H:%M:%SZ")
        itemid = lines[2]
        if len(itemid) < 2:
            continue
        if itemid not in items_id:
            items_id[itemid]=str(itemcount)
            items_freq[itemid]=1
            itemcount+=1
        else:
            items_freq[itemid] += 1

if len(items_freq)>40000:
    items_freq=dict(sorted(items_freq.items(), key=lambda d:d[1],reverse=True)[:40000])


fff = codecs.open('items.artist.txt', encoding='utf-8', mode='w')
for k in items_freq:
    fff.write(items_id[k]+os.linesep)
fff.close()

last_time=None
last_user=None
session=list()
ff = codecs.open('all.artist.txt', encoding='utf-8', mode='w')
with codecs.open('userid-timestamp-artid-artname-traid-traname.tsv', encoding='utf-8') as f:
    for line in f:
        lines = line.strip('\n').strip('\r').split('\t')
        if len(lines) < 5:
            continue
        userid = lines[0]
        time = datetime.strptime(lines[1], "%Y-%m-%dT%H:%M:%SZ")
        itemid = lines[2]
        if len(itemid) < 2 or itemid not in items_freq:
            continue

        itemid=items_id[itemid]

        if last_time is None:
            session.append(itemid)
            last_user=userid
            last_time=time
            continue

        if (last_time-time).total_seconds()>28800 or last_user!=userid:
            if 50>len(session)>1 :
                ff.write(', '.join(session) + os.linesep)
                ff.flush()
            session = list()
            last_user = userid
            last_time = time
        else:
            if len(session)==0 or itemid !=session[-1]:
                session.append(itemid)
            last_user = userid
            last_time = time
ff.close()



