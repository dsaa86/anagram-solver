import os
import sys

import pytest

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")

from ThreadedHeapRecursivePermutations import PermutationsThreadedHeapRecursiveClass
import ThreadedPermutationsClass

@pytest.mark.raise_exception
@pytest.mark.rapid_test
def test_empty_input():
    with pytest.raises(Exception) as e_info:
        heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass([])
        heap_recursive_permutations.performPermutationGeneration()


@pytest.mark.raise_exception
@pytest.mark.rapid_test
def test_too_large_input_str():
    with pytest.raises(Exception) as e_info:
        heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"])
        heap_recursive_permutations.performPermutationGeneration()


@pytest.mark.raise_exception
@pytest.mark.rapid_test
def test_too_large_input_int():
    with pytest.raises(Exception) as e_info:
        heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        heap_recursive_permutations.performPermutationGeneration()


@pytest.mark.raise_exception
@pytest.mark.rapid_test
def test_mixed_str_int_input():
    with pytest.raises(ValueError) as e_info:
        heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass(['A', 'B', 'C', 1, 2, 3])
        heap_recursive_permutations.performPermutationGeneration()


@pytest.mark.rapid_test
def test_mixed_with_spec_char():
    with pytest.raises(ValueError) as e_info:
        heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass(['A', 'B', 'C', 1, 2, 3, '!'])
        heap_recursive_permutations.performPermutationGeneration()


@pytest.mark.raise_exception
@pytest.mark.rapid_test
def test_with_spec_char():
    with pytest.raises(ValueError) as e_info:
        heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass(['!', '}', '^', '!'])
        heap_recursive_permutations.performPermutationGeneration()


@pytest.mark.input_str_test
@pytest.mark.input_test
@pytest.mark.rapid_test
def test_input_size_one_str():
    heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass(["a"])
    result_str = heap_recursive_permutations.performPermutationGeneration()
    assert result_str == ["a"]
    assert len(result_str) == 1

@pytest.mark.input_int_test
@pytest.mark.input_test
@pytest.mark.rapid_test
def test_input_size_one_int():
    heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass([1])
    result_int = heap_recursive_permutations.performPermutationGeneration()
    assert result_int == [[1]]
    assert len(result_int) == 1


@pytest.mark.input_str_test
@pytest.mark.input_test
@pytest.mark.rapid_test
def test_input_size_three_str():
    heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass(["a", "b", "c"])
    result_str = heap_recursive_permutations.performPermutationGeneration()
    assert result_str == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert len(result_str) == 6


@pytest.mark.input_int_test
@pytest.mark.input_test
@pytest.mark.rapid_test
def test_input_size_three_int():
    heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass([1, 2, 3])
    result_int = heap_recursive_permutations.performPermutationGeneration()
    assert result_int == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert len(result_int) == 6


@pytest.mark.input_str_test
@pytest.mark.input_test
@pytest.mark.rapid_test
def test_input_size_five_str():
    heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass(["a", "b", "c", "d", "e"])
    result_str = heap_recursive_permutations.performPermutationGeneration()
    assert result_str == ['abcde', 'acbde', 'adbce', 'abdce', 'acdbe', 'adcbe', 'aecbd', 'acebd', 'abecd', 'aebcd', 'acbed', 'abced', 'abdec', 'adbec', 'aebdc', 'abedc', 'adebc', 'aedbc', 'aedcb', 'adecb', 'acedb', 'aecdb', 'adceb', 'acdeb', 'bacde', 'bcade', 'bdace', 'badce', 'bcdae', 'bdcae', 'becad', 'bcead', 'baecd', 'beacd', 'bcaed', 'baced', 'badec', 'bdaec', 'beadc', 'baedc', 'bdeac', 'bedac', 'bedca', 'bdeca', 'bceda', 'becda', 'bdcea', 'bcdea', 'cabde', 'cbade', 'cdabe', 'cadbe', 'cbdae', 'cdbae', 'cebad', 'cbead', 'caebd', 'ceabd', 'cbaed', 'cabed', 'cadeb', 'cdaeb', 'ceadb', 'caedb', 'cdeab', 'cedab', 'cedba', 'cdeba', 'cbeda', 'cebda', 'cdbea', 'cbdea', 'dabce', 'dbace', 'dcabe', 'dacbe', 'dbcae', 'dcbae', 'debac', 'dbeac', 'daebc', 'deabc', 'dbaec', 'dabec', 'daceb', 'dcaeb', 'deacb', 'daecb', 'dceab', 'decab', 'decba', 'dceba', 'dbeca', 'debca', 'dcbea', 'dbcea', 'eabcd', 'ebacd', 'ecabd', 'eacbd', 'ebcad', 'ecbad', 'edbac', 'ebdac', 'eadbc', 'edabc', 'ebadc', 'eabdc', 'eacdb', 'ecadb', 'edacb', 'eadcb', 'ecdab', 'edcab', 'edcba', 'ecdba', 'ebdca', 'edbca', 'ecbda', 'ebcda']
    assert len(result_str) == 120


@pytest.mark.input_int_test
@pytest.mark.input_test
@pytest.mark.rapid_test
def test_input_size_five_int():
    heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass([1, 2, 3, 4, 5])
    result_int = heap_recursive_permutations.performPermutationGeneration()
    assert result_int == [[1, 2, 3, 4, 5], [1, 3, 2, 4, 5], [1, 4, 2, 3, 5], [1, 2, 4, 3, 5], [1, 3, 4, 2, 5], [1, 4, 3, 2, 5], [1, 5, 3, 2, 4], [1, 3, 5, 2, 4], [1, 2, 5, 3, 4], [1, 5, 2, 3, 4], [1, 3, 2, 5, 4], [1, 2, 3, 5, 4], [1, 2, 4, 5, 3], [1, 4, 2, 5, 3], [1, 5, 2, 4, 3], [1, 2, 5, 4, 3], [1, 4, 5, 2, 3], [1, 5, 4, 2, 3], [1, 5, 4, 3, 2], [1, 4, 5, 3, 2], [1, 3, 5, 4, 2], [1, 5, 3, 4, 2], [1, 4, 3, 5, 2], [1, 3, 4, 5, 2], [2, 1, 3, 4, 5], [2, 3, 1, 4, 5], [2, 4, 1, 3, 5], [2, 1, 4, 3, 5], [2, 3, 4, 1, 5], [2, 4, 3, 1, 5], [2, 5, 3, 1, 4], [2, 3, 5, 1, 4], [2, 1, 5, 3, 4], [2, 5, 1, 3, 4], [2, 3, 1, 5, 4], [2, 1, 3, 5, 4], [2, 1, 4, 5, 3], [2, 4, 1, 5, 3], [2, 5, 1, 4, 3], [2, 1, 5, 4, 3], [2, 4, 5, 1, 3], [2, 5, 4, 1, 3], [2, 5, 4, 3, 1], [2, 4, 5, 3, 1], [2, 3, 5, 4, 1], [2, 5, 3, 4, 1], [2, 4, 3, 5, 1], [2, 3, 4, 5, 1], [3, 1, 2, 4, 5], [3, 2, 1, 4, 5], [3, 4, 1, 2, 5], [3, 1, 4, 2, 5], [3, 2, 4, 1, 5], [3, 4, 2, 1, 5], [3, 5, 2, 1, 4], [3, 2, 5, 1, 4], [3, 1, 5, 2, 4], [3, 5, 1, 2, 4], [3, 2, 1, 5, 4], [3, 1, 2, 5, 4], [3, 1, 4, 5, 2], [3, 4, 1, 5, 2], [3, 5, 1, 4, 2], [3, 1, 5, 4, 2], [3, 4, 5, 1, 2], [3, 5, 4, 1, 2], [3, 5, 4, 2, 1], [3, 4, 5, 2, 1], [3, 2, 5, 4, 1], [3, 5, 2, 4, 1], [3, 4, 2, 5, 1], [3, 2, 4, 5, 1], [4, 1, 2, 3, 5], [4, 2, 1, 3, 5], [4, 3, 1, 2, 5], [4, 1, 3, 2, 5], [4, 2, 3, 1, 5], [4, 3, 2, 1, 5], [4, 5, 2, 1, 3], [4, 2, 5, 1, 3], [4, 1, 5, 2, 3], [4, 5, 1, 2, 3], [4, 2, 1, 5, 3], [4, 1, 2, 5, 3], [4, 1, 3, 5, 2], [4, 3, 1, 5, 2], [4, 5, 1, 3, 2], [4, 1, 5, 3, 2], [4, 3, 5, 1, 2], [4, 5, 3, 1, 2], [4, 5, 3, 2, 1], [4, 3, 5, 2, 1], [4, 2, 5, 3, 1], [4, 5, 2, 3, 1], [4, 3, 2, 5, 1], [4, 2, 3, 5, 1], [5, 1, 2, 3, 4], [5, 2, 1, 3, 4], [5, 3, 1, 2, 4], [5, 1, 3, 2, 4], [5, 2, 3, 1, 4], [5, 3, 2, 1, 4], [5, 4, 2, 1, 3], [5, 2, 4, 1, 3], [5, 1, 4, 2, 3], [5, 4, 1, 2, 3], [5, 2, 1, 4, 3], [5, 1, 2, 4, 3], [5, 1, 3, 4, 2], [5, 3, 1, 4, 2], [5, 4, 1, 3, 2], [5, 1, 4, 3, 2], [5, 3, 4, 1, 2], [5, 4, 3, 1, 2], [5, 4, 3, 2, 1], [5, 3, 4, 2, 1], [5, 2, 4, 3, 1], [5, 4, 2, 3, 1], [5, 3, 2, 4, 1], [5, 2, 3, 4, 1]]
    assert len(result_int) == 120

@pytest.mark.input_str_test
@pytest.mark.input_test
@pytest.mark.complex_test
@pytest.mark.timeout(550)
def test_input_size_eleven_str():
    heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
    result_str = heap_recursive_permutations.performPermutationGeneration()
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

@pytest.mark.input_int_test
@pytest.mark.input_test
@pytest.mark.complex_test
@pytest.mark.timeout(550)
def test_input_size_eleven_int():
    heap_recursive_permutations = PermutationsThreadedHeapRecursiveClass([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    result_int = heap_recursive_permutations.performPermutationGeneration()
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