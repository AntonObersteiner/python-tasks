def check(test_name, what_is, what_should_be):
    if what_is != what_should_be:
        print(f"{test_name}:")
        print(f"    Funktion ergibt: {what_is}")
        print(f"    Sollte sein:     {what_should_be}")
    else:
        print(f"{test_name} passed! :)")


def check_error(test_name, func, args, error_type):
    try:
        result = func(*args)

        print(f"{test_name}:")
        print(f"    Funktion ergibt: {result}")
        print(f"    Sollte Fehler werfen: {error_type}")
    except Exception as e:
        if isinstance(e, error_type):
            print(f"{test_name} passed! :)")
        else:
            print(f"{test_name}")
            print(f"    Funktion wirft: {type(e)} '{e}'")
            print(f"    Sollte werfen: {error_type}")
