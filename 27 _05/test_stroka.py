from Stroka.my_app.sttroka import dlina, eqvali,  chislo, ruplee, dictionary,  mnoge
import pytest

# длина строки
@pytest.mark.parametrize("z", [('', 0), ('vv', 2)])
def test_dlina(z):
    assert dlina(z[0]) == z[1]

# перевод чсла в строчку
@pytest.mark.parametrize("t", [(5, '5'), (2,'2')])
def test_chislo(t):
    assert chislo(t[0]) == t[1]

# рвыенство длин двух списков
@pytest.mark.parametrize("t", [[[1,2,3], [5,7,9], True],[[1,3], [5,10], True]])
def test_eqvali(t):
    assert eqvali(t[0], t[1]) == t[2]

 # последний элемент в кортеже
@pytest.mark.parametrize("t", [((1,2,3), 3), ((1,2,30), 30)])
def test_ruplee(t):
    assert ruplee(t[0]) == t[1]

 # # объединеие двух множеств
@pytest.mark.parametrize("t", [((1,2), (3,4), (1,2,3,4))])
def test_mnoge(t):
    assert mnoge(set(t[0]),set(t[1])) == set(t[2])