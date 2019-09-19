#%% [markdown]
## Introduction
# This *.ipynb* file was generated by VSCode from *script.py*. See VSCode documentation for more infos.
#
#
# The aim of this project is to identify common English words in the human proteome. 
# For this I have an English dictionnary with 3,000 words and a *human-proteom.fasta* file containing the human proteome.
#
# First, let's load some modules!
#%%
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib as plt
import seaborn as sn
from Bio import SeqIO # Allow me to read human-proteome.fasta file
