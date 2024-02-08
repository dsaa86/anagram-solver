import os
import sys

import pytest

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")

import ThreadedStandardPermutations
import ThreadedPermutationsClass

def test_empty_input():
    with pytest.raises(Exception) as e_info:
        ThreadedStandardPermutations.generateStandardPermutationsThreaded([])


def test_too_large_input():
    with pytest.raises(Exception) as e_info:
        ThreadedStandardPermutations.generateStandardPermutationsThreaded(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"])
        ThreadedStandardPermutations.generateStandardPermutationsThreaded([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


def test_mixed_str_int_input():
    with pytest.raises(ValueError) as e_info:
        ThreadedStandardPermutations.generateStandardPermutationsThreaded(['A', 'B', 'C', 1, 2, 3])


def test_mixed_with_spec_char():
    with pytest.raises(ValueError) as e_info:
        ThreadedStandardPermutations.generateStandardPermutationsThreaded(['A', 'B', 'C', 1, 2, 3, '!'])


def test_with_spec_char():
    with pytest.raises(ValueError) as e_info:
        ThreadedStandardPermutations.generateStandardPermutationsThreaded(['!', '}', '^', '!'])


def test_input_size_three_str():
    result_str = ThreadedStandardPermutations.generateStandardPermutationsThreaded(["a", "b", "c"])
    assert result_str == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert len(result_str) == 6


def test_input_size_three_int():
    result_int = ThreadedStandardPermutations.generateStandardPermutationsThreaded([1, 2, 3])
    assert result_int == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert len(result_int) == 6


def test_input_size_five_str():
    result_str = ThreadedStandardPermutations.generateStandardPermutationsThreaded(["a", "b", "c", "d", "e"])
    assert result_str == ['abcde', 'abced', 'abdce', 'abdec', 'abecd', 'abedc', 'acbde', 'acbed', 'acdbe', 'acdeb', 'acebd', 'acedb', 'adbce', 'adbec', 'adcbe', 'adceb', 'adebc', 'adecb', 'aebcd', 'aebdc', 'aecbd', 'aecdb', 'aedbc', 'aedcb', 'bacde', 'baced', 'badce', 'badec', 'baecd', 'baedc', 'bcade', 'bcaed', 'bcdae', 'bcdea', 'bcead', 'bceda', 'bdace', 'bdaec', 'bdcae', 'bdcea', 'bdeac', 'bdeca', 'beacd', 'beadc', 'becad', 'becda', 'bedac', 'bedca', 'cabde', 'cabed', 'cadbe', 'cadeb', 'caebd', 'caedb', 'cbade', 'cbaed', 'cbdae', 'cbdea', 'cbead', 'cbeda', 'cdabe', 'cdaeb', 'cdbae', 'cdbea', 'cdeab', 'cdeba', 'ceabd', 'ceadb', 'cebad', 'cebda', 'cedab', 'cedba', 'dabce', 'dabec', 'dacbe', 'daceb', 'daebc', 'daecb', 'dbace', 'dbaec', 'dbcae', 'dbcea', 'dbeac', 'dbeca', 'dcabe', 'dcaeb', 'dcbae', 'dcbea', 'dceab', 'dceba', 'deabc', 'deacb', 'debac', 'debca', 'decab', 'decba', 'eabcd', 'eabdc', 'eacbd', 'eacdb', 'eadbc', 'eadcb', 'ebacd', 'ebadc', 'ebcad', 'ebcda', 'ebdac', 'ebdca', 'ecabd', 'ecadb', 'ecbad', 'ecbda', 'ecdab', 'ecdba', 'edabc', 'edacb', 'edbac', 'edbca', 'edcab', 'edcba']
    assert len(result_str) == 120


def test_input_size_five_int():
    result_int = ThreadedStandardPermutations.generateStandardPermutationsThreaded([1, 2, 3, 4, 5])
    assert result_int == [[1, 2, 3, 4, 5], [1, 2, 3, 5, 4], [1, 2, 4, 3, 5], [1, 2, 4, 5, 3], [1, 2, 5, 3, 4], [1, 2, 5, 4, 3], [1, 3, 2, 4, 5], [1, 3, 2, 5, 4], [1, 3, 4, 2, 5], [1, 3, 4, 5, 2], [1, 3, 5, 2, 4], [1, 3, 5, 4, 2], [1, 4, 2, 3, 5], [1, 4, 2, 5, 3], [1, 4, 3, 2, 5], [1, 4, 3, 5, 2], [1, 4, 5, 2, 3], [1, 4, 5, 3, 2], [1, 5, 2, 3, 4], [1, 5, 2, 4, 3], [1, 5, 3, 2, 4], [1, 5, 3, 4, 2], [1, 5, 4, 2, 3], [1, 5, 4, 3, 2], [2, 1, 3, 4, 5], [2, 1, 3, 5, 4], [2, 1, 4, 3, 5], [2, 1, 4, 5, 3], [2, 1, 5, 3, 4], [2, 1, 5, 4, 3], [2, 3, 1, 4, 5], [2, 3, 1, 5, 4], [2, 3, 4, 1, 5], [2, 3, 4, 5, 1], [2, 3, 5, 1, 4], [2, 3, 5, 4, 1], [2, 4, 1, 3, 5], [2, 4, 1, 5, 3], [2, 4, 3, 1, 5], [2, 4, 3, 5, 1], [2, 4, 5, 1, 3], [2, 4, 5, 3, 1], [2, 5, 1, 3, 4], [2, 5, 1, 4, 3], [2, 5, 3, 1, 4], [2, 5, 3, 4, 1], [2, 5, 4, 1, 3], [2, 5, 4, 3, 1], [3, 1, 2, 4, 5], [3, 1, 2, 5, 4], [3, 1, 4, 2, 5], [3, 1, 4, 5, 2], [3, 1, 5, 2, 4], [3, 1, 5, 4, 2], [3, 2, 1, 4, 5], [3, 2, 1, 5, 4], [3, 2, 4, 1, 5], [3, 2, 4, 5, 1], [3, 2, 5, 1, 4], [3, 2, 5, 4, 1], [3, 4, 1, 2, 5], [3, 4, 1, 5, 2], [3, 4, 2, 1, 5], [3, 4, 2, 5, 1], [3, 4, 5, 1, 2], [3, 4, 5, 2, 1], [3, 5, 1, 2, 4], [3, 5, 1, 4, 2], [3, 5, 2, 1, 4], [3, 5, 2, 4, 1], [3, 5, 4, 1, 2], [3, 5, 4, 2, 1], [4, 1, 2, 3, 5], [4, 1, 2, 5, 3], [4, 1, 3, 2, 5], [4, 1, 3, 5, 2], [4, 1, 5, 2, 3], [4, 1, 5, 3, 2], [4, 2, 1, 3, 5], [4, 2, 1, 5, 3], [4, 2, 3, 1, 5], [4, 2, 3, 5, 1], [4, 2, 5, 1, 3], [4, 2, 5, 3, 1], [4, 3, 1, 2, 5], [4, 3, 1, 5, 2], [4, 3, 2, 1, 5], [4, 3, 2, 5, 1], [4, 3, 5, 1, 2], [4, 3, 5, 2, 1], [4, 5, 1, 2, 3], [4, 5, 1, 3, 2], [4, 5, 2, 1, 3], [4, 5, 2, 3, 1], [4, 5, 3, 1, 2], [4, 5, 3, 2, 1], [5, 1, 2, 3, 4], [5, 1, 2, 4, 3], [5, 1, 3, 2, 4], [5, 1, 3, 4, 2], [5, 1, 4, 2, 3], [5, 1, 4, 3, 2], [5, 2, 1, 3, 4], [5, 2, 1, 4, 3], [5, 2, 3, 1, 4], [5, 2, 3, 4, 1], [5, 2, 4, 1, 3], [5, 2, 4, 3, 1], [5, 3, 1, 2, 4], [5, 3, 1, 4, 2], [5, 3, 2, 1, 4], [5, 3, 2, 4, 1], [5, 3, 4, 1, 2], [5, 3, 4, 2, 1], [5, 4, 1, 2, 3], [5, 4, 1, 3, 2], [5, 4, 2, 1, 3], [5, 4, 2, 3, 1], [5, 4, 3, 1, 2], [5, 4, 3, 2, 1]]
    assert len(result_int) == 120


def test_input_size_eleven_str():
    result_str = ThreadedStandardPermutations.generateStandardPermutationsThreaded(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
    assert len(result_str) == 39916800
    assert "abcdefghijk" in result_str
    assert "bacdefghijk" in result_str
    assert "cabdefghijk" in result_str
    assert "dabcefghijk" in result_str
    assert "eabcdfghijk" in result_str
    assert "fabcdeghijk" in result_str
    assert "gabcdefhijk" in result_str
    assert "habcdefgijk" in result_str
    assert "iabcdefghjk" in result_str
    assert "jabcdefghik" in result_str
    assert "kabcdefghij" in result_str

def test_input_size_eleven_int():
    result_int = ThreadedStandardPermutations.generateStandardPermutationsThreaded([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    assert len(result_int) == 39916800
    assert [1,2,3,4,5,6,7,8,9,10,11] in result_int
    assert [2,1,3,4,5,6,7,8,9,10,11] in result_int
    assert [3,1,2,4,5,6,7,8,9,10,11] in result_int
    assert [4,1,2,3,5,6,7,8,9,10,11] in result_int
    assert [5,1,2,3,4,6,7,8,9,10,11] in result_int
    assert [6,1,2,3,4,5,7,8,9,10,11] in result_int
    assert [7,1,2,3,4,5,6,8,9,10,11] in result_int
    assert [8,1,2,3,4,5,6,7,9,10,11] in result_int
    assert [9,1,2,3,4,5,6,7,8,10,11] in result_int
    assert [10,1,2,3,4,5,6,7,8,9,11] in result_int
    assert [11,1,2,3,4,5,6,7,8,9,10] in result_int