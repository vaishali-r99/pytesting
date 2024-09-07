from hello import hello_world, hello_bye


def test_hello_world():
    assert "Hello" == hello_world()


def test_hello_world2():
    assert "Bye" == hello_bye()
