# from src.pre_built.counter import count_ocurrences
from src.pre_built.counter import count_ocurrences


def test_counter():
    result = count_ocurrences('data/jobs.csv', 'python')
    assert result == 1639
