#!/usr/bin/env python
"""Tree queries for HW4."""

from typing import List

from nltk import tgrep, tree


DATA = "data/wsj.parse"


def count_nodes(query: str, forest: List[tree.ParentedTree]) -> int:
    """Computes the number of nodes which match a TGrep query.

    This function runs a TGrep2 query, catches the resulting generator,
    and returns the number of matching nodes.

    Args:
        query: a TGrep2 query string.
        forest: a list of one or more `ParentedTree`s to be queried.

    Returns:
        The number of matching nodes.
    """
    # This a generator whose elements are, for each sentence, a list
    # of the matching nodes.
    gen = tgrep.tgrep_nodes(query, forest)
    return sum(len(nodes) for nodes in gen)


def main() -> None:
    # Loads collection of trees.
    forest = []
    with open(DATA, "r") as source:
        for line in source:
            forest.append(tree.ParentedTree.fromstring(line.rstrip()))
    # Runs queries.
    print(f"1:\t{count_nodes('PP', forest):>5,}")
    print(f"2:\t{count_nodes('FRAG', forest):>5,}")
    print(f"3:\t{count_nodes('NP < DT', forest):>5,}")
    print(f"4:\t{count_nodes('NP < POS', forest):5,}")
    print(f"5:\t{count_nodes('NP < (DT < (a | an))', forest):>5,}")
    print(f"6:\t{count_nodes('NP < (NP $ CC $ NP)', forest):>5,}")
    print(f"7.\t{count_nodes('VP << NP', forest):>5,}")
    print(f"8.\t{count_nodes('VP < NP', forest):>5,}")
    print(f"9.\t{count_nodes('VP < (NP $ NP)', forest):>5,}")
    print(f"10.\t{count_nodes('VP < (NP < PP)', forest):>5,}")


if __name__ == "__main__":
    main()
