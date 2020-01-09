from typing import List
from finders.stops import Stop
import re


def find_stops_matching_name(stops: List[Stop], name: str, regex: bool = False) -> List[Stop]:
    results = list()
    if not regex:
        for element in stops:
            if element.name == name:
                results.append(element)
    else:
        for element in stops:
            match = re.search(name, element.name, re.IGNORECASE)
            if match:
                results.append(element)
    return results

