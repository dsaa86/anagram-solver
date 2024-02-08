import os
import sys

import pytest

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")

from HeapRecursive import GeneratePermutationsHeapRecursive

def test_empty_input():
    with pytest.raises(Exception) as e_info:
        generator = GeneratePermutationsHeapRecursive([], max_perm_size = 7)
        result = generator.performPermutationGeneration()

def test_too_large_input_str():
    with pytest.raises(Exception) as e_info:
        generator = GeneratePermutationsHeapRecursive(["a", "b", "c", "d", "e", "f", "g", "h"], max_perm_size = 7)
        result = generator.performPermutationGeneration()


def test_too_large_input_int():
    with pytest.raises(Exception) as e_info:
        generator = GeneratePermutationsHeapRecursive([1, 2, 3, 4, 5, 6, 7, 8], max_perm_size = 7)
        result = generator.performPermutationGeneration()


def test_mixed_str_int_input():
    with pytest.raises(ValueError) as e_info:
        generator = GeneratePermutationsHeapRecursive(['A', 'B', 'C', 1, 2, 3], max_perm_size = 7)
        result = generator.performPermutationGeneration()


def test_mixed_with_spec_char():
    with pytest.raises(ValueError) as e_info:
        generator = GeneratePermutationsHeapRecursive(['A', 'B', 'C', 1, 2, 3, '!'], max_perm_size = 7)
        result = generator.performPermutationGeneration()


def test_with_spec_char():
    with pytest.raises(ValueError) as e_info:
        generator = GeneratePermutationsHeapRecursive(['!', '}', '^', '!'], max_perm_size = 7)
        result = generator.performPermutationGeneration()


def test_input_size_one_str():
    generator = GeneratePermutationsHeapRecursive(["a"], max_perm_size = 7)
    result = generator.performPermutationGeneration()
    assert result == ["a"]
    assert len(result) == 1


def test_input_size_one_int():
    generator = GeneratePermutationsHeapRecursive([1], max_perm_size = 7)
    result = generator.performPermutationGeneration()
    assert result == [[1]]
    assert len(result) == 1

def test_input_size_three_str():
    generator = GeneratePermutationsHeapRecursive(["a", "b", "c"], max_perm_size = 7)
    result = generator.performPermutationGeneration()
    expected_results = ['abc', 'bac', 'cab', 'acb', 'bca', 'cba']

    for expected_result in expected_results:
        assert expected_result in result
    assert len(result) == 6


def test_input_size_three_int():
    generator = GeneratePermutationsHeapRecursive([1, 2, 3], max_perm_size = 7)
    result = generator.performPermutationGeneration()
    expected_results = [[1, 2, 3], [2, 1, 3], [3, 1, 2], [1, 3, 2], [2, 3, 1], [3, 2, 1]]
    
    for expected_result in expected_results:
        assert expected_result in result
    assert len(result) == 6

def test_input_size_five_str():
    generator = GeneratePermutationsHeapRecursive(["a", "b", "c", "d", "e"], max_perm_size = 7)
    result = generator.performPermutationGeneration()
    expected_results = ['abcde', 'bacde', 'cabde', 'acbde', 'bcade', 'cbade', 'dbace', 'bdace', 'adbce', 'dabce', 'badce', 'abdce', 'acdbe', 'cadbe', 'dacbe', 'adcbe', 'cdabe', 'dcabe', 'dcbae', 'cdbae', 'bdcae', 'dbcae', 'cbdae', 'bcdae', 'ecdab', 'cedab', 'decab', 'edcab', 'cdeab', 'dceab', 'acedb', 'caedb', 'eacdb', 'aecdb', 'ceadb', 'ecadb', 'edacb', 'deacb', 'aedcb', 'eadcb', 'daecb', 'adecb', 'adceb', 'daceb', 'cadeb', 'acdeb', 'dcaeb', 'cdaeb', 'bdaec', 'dbaec', 'abdec', 'badec', 'dabec', 'adbec', 'edbac', 'debac', 'bedac', 'ebdac', 'dbeac', 'bdeac', 'baedc', 'abedc', 'ebadc', 'beadc', 'aebdc', 'eabdc', 'eadbc', 'aedbc', 'deabc', 'edabc', 'adebc', 'daebc', 'caebd', 'acebd', 'ecabd', 'ceabd', 'aecbd', 'eacbd', 'baced', 'abced', 'cbaed', 'bcaed', 'acbed', 'cabed', 'cebad', 'ecbad', 'bcead', 'cbead', 'ebcad', 'becad', 'beacd', 'ebacd', 'abecd', 'baecd', 'eabcd', 'aebcd', 'debca', 'edbca', 'bdeca', 'dbeca', 'ebdca', 'bedca', 'cedba', 'ecdba', 'dceba', 'cdeba', 'edcba', 'decba', 'dbcea', 'bdcea', 'cdbea', 'dcbea', 'bcdea', 'cbdea', 'cbeda', 'bceda', 'ecbda', 'cebda', 'becda', 'ebcda']

    for expected_result in expected_results:
        assert expected_result in result
    assert len(result) == 120


def test_input_size_five_int():
    generator = GeneratePermutationsHeapRecursive([1, 2, 3, 4, 5], max_perm_size = 7)
    result = generator.performPermutationGeneration()
    expected_results = [[2, 1, 3, 4, 5], [3, 1, 2, 4, 5], [1, 3, 2, 4, 5], [2, 3, 1, 4, 5], [3, 2, 1, 4, 5], [4, 2, 1, 3, 5], [2, 4, 1, 3, 5], [1, 4, 2, 3, 5], [4, 1, 2, 3, 5], [2, 1, 4, 3, 5], [1, 2, 4, 3, 5], [1, 3, 4, 2, 5], [3, 1, 4, 2, 5], [4, 1, 3, 2, 5], [1, 4, 3, 2, 5], [3, 4, 1, 2, 5], [4, 3, 1, 2, 5], [4, 3, 2, 1, 5], [3, 4, 2, 1, 5], [2, 4, 3, 1, 5], [4, 2, 3, 1, 5], [3, 2, 4, 1, 5], [2, 3, 4, 1, 5], [5, 3, 4, 1, 2], [3, 5, 4, 1, 2], [4, 5, 3, 1, 2], [5, 4, 3, 1, 2], [3, 4, 5, 1, 2], [4, 3, 5, 1, 2], [1, 3, 5, 4, 2], [3, 1, 5, 4, 2], [5, 1, 3, 4, 2], [1, 5, 3, 4, 2], [3, 5, 1, 4, 2], [5, 3, 1, 4, 2], [5, 4, 1, 3, 2], [4, 5, 1, 3, 2], [1, 5, 4, 3, 2], [5, 1, 4, 3, 2], [4, 1, 5, 3, 2], [1, 4, 5, 3, 2], [1, 4, 3, 5, 2], [4, 1, 3, 5, 2], [3, 1, 4, 5, 2], [1, 3, 4, 5, 2], [4, 3, 1, 5, 2], [3, 4, 1, 5, 2], [2, 4, 1, 5, 3], [4, 2, 1, 5, 3], [1, 2, 4, 5, 3], [2, 1, 4, 5, 3], [4, 1, 2, 5, 3], [1, 4, 2, 5, 3], [5, 4, 2, 1, 3], [4, 5, 2, 1, 3], [2, 5, 4, 1, 3], [5, 2, 4, 1, 3], [4, 2, 5, 1, 3], [2, 4, 5, 1, 3], [2, 1, 5, 4, 3], [1, 2, 5, 4, 3], [5, 2, 1, 4, 3], [2, 5, 1, 4, 3], [1, 5, 2, 4, 3], [5, 1, 2, 4, 3], [5, 1, 4, 2, 3], [1, 5, 4, 2, 3], [4, 5, 1, 2, 3], [5, 4, 1, 2, 3], [1, 4, 5, 2, 3], [4, 1, 5, 2, 3], [3, 1, 5, 2, 4], [1, 3, 5, 2, 4], [5, 3, 1, 2, 4], [3, 5, 1, 2, 4], [1, 5, 3, 2, 4], [5, 1, 3, 2, 4], [2, 1, 3, 5, 4], [1, 2, 3, 5, 4], [3, 2, 1, 5, 4], [2, 3, 1, 5, 4], [1, 3, 2, 5, 4], [3, 1, 2, 5, 4], [3, 5, 2, 1, 4], [5, 3, 2, 1, 4], [2, 3, 5, 1, 4], [3, 2, 5, 1, 4], [5, 2, 3, 1, 4], [2, 5, 3, 1, 4], [2, 5, 1, 3, 4], [5, 2, 1, 3, 4], [1, 2, 5, 3, 4], [2, 1, 5, 3, 4], [5, 1, 2, 3, 4], [1, 5, 2, 3, 4], [4, 5, 2, 3, 1], [5, 4, 2, 3, 1], [2, 4, 5, 3, 1], [4, 2, 5, 3, 1], [5, 2, 4, 3, 1], [2, 5, 4, 3, 1], [3, 5, 4, 2, 1], [5, 3, 4, 2, 1], [4, 3, 5, 2, 1], [3, 4, 5, 2, 1], [5, 4, 3, 2, 1], [4, 5, 3, 2, 1], [4, 2, 3, 5, 1], [2, 4, 3, 5, 1], [3, 4, 2, 5, 1], [4, 3, 2, 5, 1], [2, 3, 4, 5, 1], [3, 2, 4, 5, 1], [3, 2, 5, 4, 1], [2, 3, 5, 4, 1], [5, 3, 2, 4, 1], [3, 5, 2, 4, 1], [2, 5, 3, 4, 1], [5, 2, 3, 4, 1], [5, 2, 3, 4, 1]]

    for expected_result in expected_results:
        assert expected_result in result
    assert len(result) == 120


def test_input_size_seven_str():
    generator = GeneratePermutationsHeapRecursive(["a", "b", "c", "d", "e", "f", "g"], max_perm_size = 7)
    result = generator.performPermutationGeneration()
    assert len(result) == 5040
    assert 'abcdefg' in result
    assert 'bacdefg' in result
    assert 'cabdefg' in result
    assert 'dabcefg' in result
    assert 'eabcdfg' in result
    assert 'fabcdeg' in result
    assert 'gabcdef' in result


def test_input_size_seven_int():
    generator = GeneratePermutationsHeapRecursive([1, 2, 3, 4, 5, 6, 7], max_perm_size = 7)
    result = generator.performPermutationGeneration()

    assert len(result) == 5040
    # assert [1, 2, 3, 4, 5, 6, 7] in result
    assert [2, 1, 3, 4, 5, 6, 7] in result
    assert [3, 1, 2, 4, 5, 6, 7] in result
    assert [4, 1, 2, 3, 5, 6, 7] in result
    assert [5, 1, 2, 3, 4, 6, 7] in result
    assert [6, 1, 2, 3, 4, 5, 7] in result
    assert [7, 1, 2, 3, 4, 5, 6] in result