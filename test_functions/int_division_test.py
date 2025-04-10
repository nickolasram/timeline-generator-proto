def int_div_test(x):
    expected = []
    match x:
        case _ if 2.25 <= x < 4.5:
            expected = [1]
        case _ if 4.5 <= x < 9:
            expected = [2, 3]
        case _ if 9 <= x < 13.5:
            expected = [4, 5]
        case _ if 13.5 <= x < 18:
            expected = [6, 7]
    assert x // 2.25 in expected, f"{x} // 2.25 = {x // 2.25}"
    print(f"{x} // 2.25 = {x // 2.25}")
