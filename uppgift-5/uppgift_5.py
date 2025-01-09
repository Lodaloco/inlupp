# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.


def filter_odd(numbers: list[int]) -> list[int]:
    """
    Skriv beskrivning här.
    """
    return [num for num in numbers if num % 2 == 0]
