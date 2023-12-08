def hello_world():
    """Define a function to print 'Hello World' to the standard output."""
    print("Hello World")


def test_hello_world(capfd):
    """
    Test case for verifying the 'hello_world' function's output.

    Args:
    capfd (fixture): Pytest fixture to capture the stdout and stderr.
    """
    hello_world()
    out, err = capfd.readouterr()
    assert out == "Hello World\n"
