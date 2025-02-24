The queries and counts are:

1.  `PP`: 1,087
2.  `FRAG`: 18
3.  `NP < DT`: 1,128
4.  `NP < POS`: 177
5.  `NP < (DT < (a | an))`: 324
6.  `NP < (NP $ CC $ NP)`: 128
7.  `VP << NP`: 1,535
8.  `VP < NP`: 548
9.  `VP < (NP $ NP)`: 7
10. `VP < (NP < PP)`: 139

See [`query.py`](query.py) for the code. Sample output:

    $ ./query.py
    1:  1,087
    2:     18
    3:  1,128
    4:    177
    5:    324
    6:    128
    7.  1,535
    8.    548
    9.      7
    10.   139
