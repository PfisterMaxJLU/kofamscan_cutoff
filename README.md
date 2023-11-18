# kofamscan_cutoff
This is a code example modifiable for your own needs.

A script for the formatting and enforcement of KO cut-off thresholds in hmmsearch output files. 

This uses the threshold values from the KEGG "ko_list". 

In one part of the script, we discard the rare (≈1%) secondary (lower score) K assignments. Depending on your use case, this might not be desirable. 

Disregarding the dual assignments, the resulting output is >99.999% identical to Kofamscan [1].

Depending on your data, this may all vary.

[1] Tested on one Buchnera aphidicola (34k genes) and one Xanthomonas (1000k genes) (pan-genomes)
