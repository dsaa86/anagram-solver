import os
import sys

import pytest

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")

import ThreadedStandardPermutations

def test_empty_input():
    with pytest.raises(Exception) as e_info:
        ThreadedStandardPermutations.generatePermutationsThreaded([])

def test_too_large_input():
    with pytest.raises(Exception) as e_info:
        ThreadedStandardPermutations.generatePermutationsThreaded(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"])

def test_input_size_three():
    result = ThreadedStandardPermutations.generatePermutationsThreaded(["A", "B", "C"])
    assert result == ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    assert len(result) == 6

def test_input_size_five():
    result = ThreadedStandardPermutations.generatePermutationsThreaded(["A", "B", "C", "D", "E"])
    assert result == ['ABCDE', 'ABCED', 'ABDCE', 'ABDEC', 'ABECD', 'ABEDC', 'ACBDE', 'ACBED', 'ACDBE', 'ACDEB', 'ACEBD', 'ACEDB', 'ADBCE', 'ADBEC', 'ADCBE', 'ADCEB', 'ADEBC', 'ADECB', 'AEBCD', 'AEBDC', 'AECBD', 'AECDB', 'AEDBC', 'AEDCB', 'BACDE', 'BACED', 'BADCE', 'BADEC', 'BAECD', 'BAEDC', 'BCADE', 'BCAED', 'BCDAE', 'BCDEA', 'BCEAD', 'BCEDA', 'BDACE', 'BDAEC', 'BDCAE', 'BDCEA', 'BDEAC', 'BDECA', 'BEACD', 'BEADC', 'BECAD', 'BECDA', 'BEDAC', 'BEDCA', 'CABDE', 'CABED', 'CADBE', 'CADEB', 'CAEBD', 'CAEDB', 'CBADE', 'CBAED', 'CBDAE', 'CBDEA', 'CBEAD', 'CBEDA', 'CDABE', 'CDAEB', 'CDBAE', 'CDBEA', 'CDEAB', 'CDEBA', 'CEABD', 'CEADB', 'CEBAD', 'CEBDA', 'CEDAB', 'CEDBA', 'DABCE', 'DABEC', 'DACBE', 'DACEB', 'DAEBC', 'DAECB', 'DBACE', 'DBAEC', 'DBCAE', 'DBCEA', 'DBEAC', 'DBECA', 'DCABE', 'DCAEB', 'DCBAE', 'DCBEA', 'DCEAB', 'DCEBA', 'DEABC', 'DEACB', 'DEBAC', 'DEBCA', 'DECAB', 'DECBA', 'EABCD', 'EABDC', 'EACBD', 'EACDB', 'EADBC', 'EADCB', 'EBACD', 'EBADC', 'EBCAD', 'EBCDA', 'EBDAC', 'EBDCA', 'ECABD', 'ECADB', 'ECBAD', 'ECBDA', 'ECDAB', 'ECDBA', 'EDABC', 'EDACB', 'EDBAC', 'EDBCA', 'EDCAB', 'EDCBA']
    assert len(result) == 120

def test_input_size_eleven():
    result = ThreadedStandardPermutations.generatePermutationsThreaded(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])
    assert len(result) == 39916800
    assert "ABCDEFGHIJK" in result
    assert "BACDEFGHIJK" in result
    assert "CABDEFGHIJK" in result
    assert "DABCEFGHIJK" in result
    assert "EABCDFGHIJK" in result
    assert "FABCDEGHIJK" in result
    assert "GABCDEFHIJK" in result
    assert "HABCDEFGIJK" in result
    assert "IABCDEFGHJK" in result
    assert "JABCDEFGHIK" in result
    assert "KABCDEFGHIJ" in result