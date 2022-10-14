from selectk.quickselect import find_kth_largest_ele


def test_find_kth_largest_ele():
    for i in range(10):
        a = [x for x in range(9 + i)]
        assert find_kth_largest_ele(a, 9) == i
