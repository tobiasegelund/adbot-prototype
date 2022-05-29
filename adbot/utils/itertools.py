from typing import List, Any
import itertools


def flatten_lists(list_of_lists: List[List[Any]]) -> List[Any]:
    return list(itertools.chain(*list_of_lists))
