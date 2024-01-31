import os
import sys

import pytest

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")

import HeapRecursive

def test_empty_input():
    with pytest.raises(Exception) as e_info:
        HeapRecursive.heapRecursive([])

def test_input_size_three():
    result = HeapRecursive.heapRecursive(["A", "B", "C"])
    assert result == ['ABC', 'BAC', 'CAB', 'ACB', 'BCA', 'CBA']
    assert len(result) == 6

def test_input_size_five():
    result = HeapRecursive.heapRecursive(["A", "B", "C", "D", "E"])
    assert result == ['ABCDE', 'BACDE', 'CABDE', 'ACBDE', 'BCADE', 'CBADE', 'DBACE', 'BDACE', 'ADBCE', 'DABCE', 'BADCE', 'ABDCE', 'ACDBE', 'CADBE', 'DACBE', 'ADCBE', 'CDABE', 'DCABE', 'DCBAE', 'CDBAE', 'BDCAE', 'DBCAE', 'CBDAE', 'BCDAE', 'ECDAB', 'CEDAB', 'DECAB', 'EDCAB', 'CDEAB', 'DCEAB', 'ACEDB', 'CAEDB', 'EACDB', 'AECDB', 'CEADB', 'ECADB', 'EDACB', 'DEACB', 'AEDCB', 'EADCB', 'DAECB', 'ADECB', 'ADCEB', 'DACEB', 'CADEB', 'ACDEB', 'DCAEB', 'CDAEB', 'BDAEC', 'DBAEC', 'ABDEC', 'BADEC', 'DABEC', 'ADBEC', 'EDBAC', 'DEBAC', 'BEDAC', 'EBDAC', 'DBEAC', 'BDEAC', 'BAEDC', 'ABEDC', 'EBADC', 'BEADC', 'AEBDC', 'EABDC', 'EADBC', 'AEDBC', 'DEABC', 'EDABC', 'ADEBC', 'DAEBC', 'CAEBD', 'ACEBD', 'ECABD', 'CEABD', 'AECBD', 'EACBD', 'BACED', 'ABCED', 'CBAED', 'BCAED', 'ACBED', 'CABED', 'CEBAD', 'ECBAD', 'BCEAD', 'CBEAD', 'EBCAD', 'BECAD', 'BEACD', 'EBACD', 'ABECD', 'BAECD', 'EABCD', 'AEBCD', 'DEBCA', 'EDBCA', 'BDECA', 'DBECA', 'EBDCA', 'BEDCA', 'CEDBA', 'ECDBA', 'DCEBA', 'CDEBA', 'EDCBA', 'DECBA', 'DBCEA', 'BDCEA', 'CDBEA', 'DCBEA', 'BCDEA', 'CBDEA', 'CBEDA', 'BCEDA', 'ECBDA', 'CEBDA', 'BECDA', 'EBCDA']
    assert len(result) == 120

def test_for_specific_string_in_response():
    result = HeapRecursive.heapRecursive(["A", "T", "H", "W", "M", "E", "T"])
    in_result = "MATTHEW" in result
    assert in_result

    not_in_result = "JATTHEW" not in result
    assert not_in_result

