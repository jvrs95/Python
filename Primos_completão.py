def éPrimo(k):
    if k <= 1:
        if k < 0:
            return ("número inválido")
        else:
            if k == 0:
                return ("não existe")
            else:
                if k == 1:
                    return (1)
    else:
        a = 2
        while k % a != 0:
            a = a + 1
        if a < k and a > 1:
            return ("não primo")
        else:
            return ("primo")
                    
def test_éPrimonegativ():
    assert éPrimo(-1) == "número inválido"

def test_éPrimo0():
    assert éPrimo(0) == "não existe"

def test_éPrimo1():
    assert éPrimo(1) == 1

def test_éPrimo2():
    assert éPrimo(2) == "primo"

def test_éPrimo3():
    assert éPrimo(3) == "primo"

def test_éPrimo4():
    assert éPrimo(4) == "não primo"

def test_éPrimo100():
    assert éPrimo(100) == "não primo"

