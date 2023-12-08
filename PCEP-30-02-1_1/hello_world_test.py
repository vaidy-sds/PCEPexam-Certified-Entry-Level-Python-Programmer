# function to print hello world
def hello_world():
    print("Hello World")


# pytest to check if the function is working
def test_hello_world(capfd):
    hello_world()  # call the function
    out, err = capfd.readouterr()  # capture the output
    assert out == "Hello World\n"  # check the output
