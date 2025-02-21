def is_valid_nin(nin: int) -> None:
    """This function takes an 11-digit long integer as input."""
    # Check if the input is an integer.
    if not isinstance(nin, int):
        print("Invalid input; please enter a numeric value.") 

    # Check if input is an 11-digit integer.
    if nin < 10000000000:
        print(f"Invalid National Identity Number. {nin} is less than 11 digits.")
    elif nin > 99999999999:
        print(f"Invalid National Identity Number. {nin} is more than 11 digits.")
    else:
        print(f"Congratulations! {nin} is a valid National Identity Number.")

is_valid_nin(24651325643)