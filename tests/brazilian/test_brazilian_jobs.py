# from src.pre_built.brazilian_jobs import read_brazilian_file
from src.pre_built.brazilian_jobs import read_brazilian_file

def test_brazilian_jobs():
    result = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert result[0].get('title') == 'Maquinista'
    assert result[0].get('salary') == '2000'
    assert result[0].get('type') == 'trainee'
