# tenextra

Extra tools for parsing 10X VDJ annoations 

### Purpose
We consider the frequency of each unique chain (nucleotide-level), and how frequency 
of each alpha chain is paired with each unique beta chain. 
We attempt to use that information to distinguish 'true' pairings from 
likley cell-free DNA artifacts. 

At the end of the day, if a cell has multiple alphas/betas pairings,
and no obvious contaminating receptor is found, the remaining choice 
is to select, per single cell barcode, the A:B chains the highest umi counts. 

### Basic Usage 

```python
from tenextra.parse import select_likely_receptors
clean_clones, all_clones, ct_chains, ct_pairs = \
    select_likely_receptors(f = 'tenextra/data/filtered_contig_annotations.csv', threshold_chains = 10)
```

1. `clean_clones` pd.DataFrame with most likely A:B pairing, only one pairing per barcode
2. 'all_clones` pd.DataFrame with all possible A:B pairings, possibly more than one per barcode
3.  ct_chain - Frequency of each single chain
4.  ct_pairs - Frequency of paired chains 


### TODO: Find Chimeric Sequences 
