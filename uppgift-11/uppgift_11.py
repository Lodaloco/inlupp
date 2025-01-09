# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text: str) -> int:
    """
    Skriv beskrivning här.
    """


    return len(text.split())

# Exempelanvändning
print(word_count("Det här är en testmening."))  # Output: 5
print(word_count("Python är kul!"))            # Output: 3

