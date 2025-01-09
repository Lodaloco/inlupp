# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng 
# är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(string):
    """
    Kontrollerar om en given sträng är ett palindrom.
    """
    string = string.replace(" ", "").lower() 
    return string == string[::-1]  

