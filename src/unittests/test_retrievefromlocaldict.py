import os
import sys

import pytest

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")

import RetrieveFromLocalDict


@pytest.fixture
def setup_retrieve_from_local_dict():
    retrieve_from_local_dict = RetrieveFromLocalDict.RetrieveFromLocalDict(path=f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")
    
    yield retrieve_from_local_dict

    retrieve_from_local_dict = None


def test_retrieve_known_true_value_from_local_dict(setup_retrieve_from_local_dict):
    
    retrieve_from_local_dict = setup_retrieve_from_local_dict

    assert retrieve_from_local_dict.retrieveFromLocalDict("a") == True
    assert retrieve_from_local_dict.retrieveFromLocalDict("cricket") == True
    assert retrieve_from_local_dict.retrieveFromLocalDict("aardvark") == True
    assert retrieve_from_local_dict.retrieveFromLocalDict("abelmoschus") == True
    assert retrieve_from_local_dict.retrieveFromLocalDict("punitiveness") == True
    assert retrieve_from_local_dict.retrieveFromLocalDict("investitures") == True
    assert retrieve_from_local_dict.retrieveFromLocalDict("unbuckramed") == True
    assert retrieve_from_local_dict.retrieveFromLocalDict("zwitterionic") == True

def test_retrieve_known_false_value_from_local_dict(setup_retrieve_from_local_dict):

    retrieve_from_local_dict = setup_retrieve_from_local_dict

    assert retrieve_from_local_dict.retrieveFromLocalDict("deaccesseion") == False
    assert retrieve_from_local_dict.retrieveFromLocalDict("crickdets") == False
    assert retrieve_from_local_dict.retrieveFromLocalDict("aardvardks") == False
    assert retrieve_from_local_dict.retrieveFromLocalDict("abelfmoschuses") == False
    assert retrieve_from_local_dict.retrieveFromLocalDict("punitivednesses") == False
    assert retrieve_from_local_dict.retrieveFromLocalDict("invedstiture") == False
    assert retrieve_from_local_dict.retrieveFromLocalDict("udnbuckram") == False
    assert retrieve_from_local_dict.retrieveFromLocalDict("zwitteriond") == False