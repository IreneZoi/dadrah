import numpy as np
from typing import List

import pofah.jet_sample as jesa

def get_bin_counts_sig_like_bg_like(sample:jesa.JetSample, bin_edges:List) -> List[int]:
    
    tot_count, _ = np.histogram(sample['mJJ'], bins=bin_edges)
    acc_count, _ = np.histogram(sample.accepted('mJJ'), bins=bin_edges)
    rej_count, _ = np.histogram(sample.rejected('mJJ'), bins=bin_edges) 
    return [tot_count, acc_count, rej_count]


def divide_sample_into_orthogonal_quantiles(sample:jesa.JetSample, quantiles:List) -> List[jesa.JetSample]:

    quantiles_inv = [round((1.-q),2) for q in quantiles] # invert quantiles to [0.9, 0.7, 0.5, 0.3, 0.1, 0.01]

    samples_ortho = []

    # process bottom quantile (didn't make first cut, e.g. sel 0.9 == 0)
    q_key = 'sel_q{:02}'.format(int(quantiles_inv[0]*100))
    samples_ortho.append(sample.filter(~sample[q_key]))

    # process all quantiles except for last (tightest)
    for q_i, q_ii in zip(quantiles_inv[:-1], quantiles_inv[1:]):

        q_i_key, q_ii_key = 'sel_q{:02}'.format(int(q_i*100)), 'sel_q{:02}'.format(int(q_ii*100))

        sample_q_next = sample.filter(sample[q_i_key] & ~sample[q_ii_key])
        samples_ortho.append(sample_q_next)

    # process tightest quantile
    q_key = 'sel_q{:02}'.format(int(quantiles_inv[-1]*100))
    samples_ortho.append(sample.filter(sample[q_key]))

    return samples_ortho
