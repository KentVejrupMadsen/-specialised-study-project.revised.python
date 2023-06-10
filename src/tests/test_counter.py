from Operators.Counter import Counter


def test_counter():
    counter = Counter()
    counter.set_value(4)

    assert counter.get_value() == 4
