import pytest

from concertina import concertina


def test_no_pages():
    assert concertina(1, 0) == []

def test_nonsense():
    with pytest.raises(TypeError):
        assert concertina() == []
        assert concertina(None) == []
        assert concertina(None, None) == []
    with pytest.raises(ValueError):
        assert concertina('banana', None) == []
        assert concertina(None, 'grape') == []
        assert concertina('banana', 'grape') == []
        assert concertina(1, 'grape') == []
        assert concertina('banana', 5) == []

def test_out_of_bounds():
    assert concertina(-1, 5) == concertina(1, 5)
    assert concertina(-100, 50) == concertina(1, 50)
    assert concertina(-1000, 500) == concertina(1, 500)
    assert concertina(10, 5) == concertina(5, 5)
    assert concertina(50, 30) == concertina(30, 30)
    assert concertina(100, 55) == concertina(55, 55)
    assert concertina(1000, 505) == concertina(505, 505)

def test_single_page():
    assert concertina(1, 1) == [1]

def test_two_pages():
    assert concertina(1, 2) == [1, 2]
    assert concertina(2, 2) == [1, 2]

def test_three_pages():
    assert concertina(1, 3) == [1, 2, 3]
    assert concertina(3, 3) == [1, 2, 3]

def test_four_pages():
    assert concertina(1, 4) == [1, 2, 3, 4]
    assert concertina(4, 4) == [1, 2, 3, 4]

def test_five_pages():
    assert concertina(1, 5) == [1, 2, 3, 4, 5]
    assert concertina(5, 5) == [1, 2, 3, 4, 5]

def test_six_pages():
    assert concertina(1, 6) == [1, 2, 3, 4, 5, 6]
    assert concertina(6, 6) == [1, 2, 3, 4, 5, 6]

def test_seven_pages():
    assert concertina(1, 7) == [1, 2, 3, 4, 5, 6, 7]
    assert concertina(7, 7) == [1, 2, 3, 4, 5, 6, 7]

def test_eight_pages():
    assert concertina(1, 8) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert concertina(8, 8) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_nine_pages():
    assert concertina(1, 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert concertina(9, 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_ten_pages():
    assert concertina(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert concertina(10, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_eleven_pages():
    assert concertina(1, 11) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    assert concertina(6, 11) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert concertina(11, 11) == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def test_twelve_pages():
    assert concertina(1, 12) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
    assert concertina(6, 12) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert concertina(12, 12) == [1, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def test_thirteen_pages():
    assert concertina(1, 13) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 13]
    assert concertina(7, 13) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert concertina(13, 13) == [1, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def test_fourteen_pages():
    assert concertina(1, 14) == [1, 2, 3, 4, 5, 6, 7, 8, 10, 14]
    assert concertina(7, 14) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]
    assert concertina(8, 14) == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert concertina(14, 14) == [1, 5, 7, 8, 9, 10, 11, 12, 13, 14]

def test_fifteen_pages():
    assert concertina(1, 15) == [1, 2, 3, 4, 5, 6, 7, 9, 11, 15]
    assert concertina(4, 15) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
    assert concertina(8, 15) == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]
    assert concertina(12, 15) == [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert concertina(15, 15) == [1, 5, 7, 9, 10, 11, 12, 13, 14, 15]

def test_rounding_to_five():
    # just before and after when rounding to 5 kicks in
    assert concertina(1, 28) == [1, 2, 3, 5, 6, 8, 12, 15, 20, 28]
    assert concertina(1, 29) == [1, 2, 3, 5, 10, 15, 20, 29]

    assert concertina(16, 31) == [1, 8, 11, 12, 14, 15, 16, 17, 18, 20, 21, 24, 31]
    assert concertina(17, 33) == [1, 10, 15, 16, 17, 18, 19, 20, 25, 33]

    assert concertina(28, 28) == [1, 9, 14, 17, 21, 23, 24, 26, 27, 28]
    assert concertina(29, 29) == [1, 10, 15, 20, 25, 27, 28, 29]

def test_rounding_to_ten():
    # just before and after when rounding to 10 kicks in
    assert concertina(1, 58) == [1, 2, 3, 5, 10, 15, 20, 30, 40, 58]
    assert concertina(1, 59) == [1, 2, 3, 10, 20, 30, 40, 59]

    assert concertina(31, 61) == [1, 15, 20, 25, 29, 30, 31, 32, 33, 35, 40, 45, 61]
    assert concertina(32, 63) == [1, 20, 30, 31, 32, 33, 34, 40, 50, 63]

    assert concertina(58, 58) == [1, 15, 30, 35, 45, 50, 56, 57, 58]
    assert concertina(59, 59) == [1, 20, 30, 40, 50, 57, 58, 59]

def test_rounding_to_fifty():
    # just before and after when rounding to 50 kicks in
    assert concertina(1, 298) == [1, 2, 3, 20, 50, 70, 110, 150, 210, 298]
    assert concertina(1, 299) == [1, 2, 3, 50, 100, 150, 200, 299]

    assert concertina(151, 301) == [1, 80, 110, 130, 149, 150, 151, 152, 153, 170, 190, 230, 301]
    assert concertina(152, 303) == [1, 100, 150, 151, 152, 153, 154, 200, 250, 303]

    assert concertina(298, 298) == [1, 90, 150, 190, 230, 250, 280, 296, 297, 298]
    assert concertina(299, 299) == [1, 100, 150, 200, 250, 297, 298, 299]

def test_ohsomany_pages():
    assert concertina(1, 2547) == [1, 2, 3, 200, 350, 550, 900, 1300, 1800, 2547]
    assert concertina(8, 2547) == [1, 4, 6, 7, 8, 9, 10, 200, 400, 800, 1200, 1750, 2547]
    assert concertina(87, 2547) == [1, 50, 85, 86, 87, 88, 89, 300, 450, 850, 1200, 1800, 2547]
    assert concertina(506, 2547) == [1, 250, 504, 505, 506, 507, 508, 650, 800, 1150, 1450, 1900, 2547]
    assert concertina(1274, 2547) == [1, 650, 950, 1100, 1272, 1273, 1274, 1275, 1276, 1450, 1600, 1900, 2547]
    assert concertina(2100, 2547) == [1, 650, 1150, 1450, 1800, 1950, 2098, 2099, 2100, 2101, 2102, 2300, 2547]
    assert concertina(2540, 2547) == [1, 800, 1350, 1750, 2150, 2350, 2538, 2539, 2540, 2541, 2542, 2544, 2547]
    assert concertina(2547, 2547) == [1, 750, 1250, 1650, 2000, 2200, 2350, 2545, 2546, 2547]
