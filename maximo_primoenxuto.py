def maior_primo(x):
    if x < 2:
        return x
    else:
        k = 3
        while k < x:
            a = 2
            while a>= 2 and a < k:
                if k % a != 0:
                    a = a + 1

                else:
                    break
            primo = k
            k = k + 1
        return k
