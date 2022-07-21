import sys
from collections import defaultdict, Counter
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ref', help='Reference ranking in TREC format', required=True)
parser.add_argument('--ref_label', help='Label of reference in plot.', default='Reference')
parser.add_argument('--run', help='Run ranking in TREC format.', required=True)
parser.add_argument('--run_label', help='Label of run in plot.', default='Run')
args = parser.parse_args()


buckets = [10,100,500,1000]
bucket_d, ref_d, run_d, other = {}, {}, {}, {}

# create rank to bucket dict
b = 0
for r in range(buckets[-1]):
    if r < buckets[b]:
        bucket_d[r] = buckets[b]
    else:
        bucket_d[r] = buckets[b]
        b += 1
    print(r)
    print(bucket_d[r])

#read ref and save ranks
for l in open(args.ref):
    q, q0, d, rank, score, tag = l.rstrip().split()
    if q not in ref_d:
        ref_d[q] = {}
    ref_d[q][d] = bucket_d[int(rank)-1]

# read run
movement = defaultdict(list)
for l in open(args.run):
    q, q0, d, rank, score, tag = l.rstrip().split()
    # if q not in dict create entry 
    if q not in run_d:
        run_d[q] = {}
    # if doc in dict get the bucket of doc in ref
    if d in ref_d[q]:
        ref_b = ref_d[q][d]    
    if bucket_d[int(rank)-1] == 10 and ref_b == 1000:
        print(q, d)
    # save the bucket of ref @ rank 
    movement[bucket_d[int(rank)-1]].append(ref_b)



movement_c = {}
# count buckets
for b in movement:
    movement_c[b] = dict(Counter(movement[b]))

df = pd.DataFrame.from_dict(movement_c).T
df = df.sort_index(1)
print(df)
df = df.apply(lambda l: l/l.sum(), 1)
plt.figure()
print(df)


ax = sns.heatmap(df, cmap='YlGnBu', annot=True, linewidths=2, cbar=False, fmt='.2g')
plt.xlabel(f'{args.ref_label} @')
plt.ylabel(f'{args.run_label} @')
plt.tight_layout()
plt.savefig(f'{args.run.split("/")[-1]}_{args.ref.split("/")[-1]}.pdf')
