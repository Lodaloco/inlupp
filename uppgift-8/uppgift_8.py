# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

from collections import Counter

def count_letters(string):
    """
    Returnerar en dictionary med antalet förekomster av varje bokstav i strängen.
    """
    return Counter(char.lower() for char in string if char.isalpha())

