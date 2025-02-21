def national_identity_number(n: int) -> None:
    """ This function takes an 11-digit long integer as input. """
    # Check if the input is an integer
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    # Check if input is an 11-digit long integer
    if not 10000000000 <= n <= 99999999999:
        print(f"{n} is not a valid National Identity Number.")

    else: 
        print(f"Congratulations! {n} is a valid National Identity Number.")

national_identity_number(4388192426)