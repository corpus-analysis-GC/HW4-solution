The queries and counts are:

1.  `FRAG`: 18
2.  `CD`: 647
3.  `NP < DT`: 1,128
4.  `NP < (DT < a)`: 274
5.  `NP < (NP $ CC $ NP)`: 128
6.  `VP << NP`: 1,535
7.  `VP < NP`: 548
8.  `VP !< NP`: 1,288
9.  `VP < (NP $ NP)`: 7
10. `VP < (NP < PP)`: 139

See [`hw4.py`](hw4.py) for the code. Sample output:

    $ ./hw4.py 
    1:     18
    2:    647
    3:  1,128
    4:    274
    5:    128
    6.  1,535
    7.    548
    8.  1,288
    9.      7
    10.   139
