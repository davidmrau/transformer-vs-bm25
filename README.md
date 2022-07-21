# Plotting differences in ranking 


This script devides the ranked documents of a `run` in rank-buckets [10, 100, 500, 1000] and plots at which bucket (position) the documents are in a `reference` ranking.

Both `run` and `reference` need to contain the exact same ranked queries and documents. Both rankings need to be in the following format:
```
QueryID Q0 DocumentID Rank Score Run_tag
```


Installing the requirements:


```
pip3 install -r requirements.txt

```

Running the script:

```

python3 plot_rank_diff.py --ref reference.trec --run run.trec

```


This script was used to generate plots in:

ECIR'22 -  How Different are Pre-trained Transformers for Text Ranking? D.Rau et al. [arXiv:2204.07233](https://arxiv.org/abs/2204.07233)

Please consider citing our work:
```
@inproceedings{rau2022different,
  title={How Different are Pre-trained Transformers for Text Ranking?},
  author={Rau, David and Kamps, Jaap},
  booktitle={European Conference on Information Retrieval},
  doi={10.1007/978-3-030-99739-7\_24},
  pages={207--214},
  year={2022},
  publisher={Springer}
}
```
