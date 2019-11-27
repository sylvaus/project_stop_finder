from typing import List
from finders.stops import Stop
import re


def find_stops_matching_name(stops: List[Stop], name: str, regex: bool = False) -> List[Stop]:
    found = False
    results = list()
    if not regex:
        for element in stops:
            if element.name == name:
                print("Your stop is: ", element)
                found = True
                return element
        if not found:
            print("Sorry, this stop doesn't exist. Try regex=True")
    else:
        for element in stops:
            match = re.search(name, element.name, re.IGNORECASE)
            if match:
                results.append(element)
                print("Your stop is: ", element)
        if not results:
            print("Sorry, can't find anything")
        else:
            return results




