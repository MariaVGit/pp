def fetch_and_validate_int(standard_msg, error_msg = "To nie jest liczba całkowita"):
    while True:
        try:
            return int(input(standard_msg))
        except:
