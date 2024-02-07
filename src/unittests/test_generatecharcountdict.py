import os
import sys
import json

import pytest

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")

import GenerateCharCountDict

def test_generate_char_count_dict():
    with pytest.raises(ValueError) as e_info:
        char_count_dict_obj = GenerateCharCountDict.GenerateCharCountDict()

    try:
        char_count_dict_obj = GenerateCharCountDict.GenerateCharCountDict(read = True)
    except:
        assert False

    try:
        char_count_dict_obj = GenerateCharCountDict.GenerateCharCountDict(generate = True)
    except:
        assert False


def test_retrieve_known_char_count_dict():
    with open(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/char_count_dictionary.json", "r") as file:
        try:
            extracted_dict_from_file = json.load(file)
        except ValueError as e:
            assert False


def test_generate_known_char_count_dict():
    pre_gen_file_modified_time = os.path.getmtime(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/char_count_dictionary.json")

    char_count_dict_obj = GenerateCharCountDict.GenerateCharCountDict(generate = True)

    post_gen_file_modified_time = os.path.getmtime(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/char_count_dictionary.json")

    assert pre_gen_file_modified_time < post_gen_file_modified_time


def test_known_char_dict_structure():
    char_count_dict_obj = GenerateCharCountDict.GenerateCharCountDict(read = True)

    for key, value in char_count_dict_obj.char_count_dict.items():
        assert type(key) == tuple
        assert type(value) == list

        if "a" in value:
            assert True
            if key == ('a1'):
                assert True

        elif "cricket" in value:
            assert True
            if key != ('c2', 'e1', 'i1', 'k1', 'r1', 't1'):
                assert False

        elif "aardvark" in value:
            assert True
            if key != ('a3', 'd1', 'k1', 'r2', 'v1'):
                assert False

        elif "abelmoschus" in value:
            assert True
            if key != ('a1', 'b1', 'c1', 'e1', 'h1', 'l1', 'm1', 'o1', 's2', 'u1'):
                assert False

        elif "punitiveness" in value:
            assert True
            if key != ('e2', 'i2', 'n2', 'p1', 's2', 't1', 'u1', 'v1'):
                assert False

        elif "investitures" in value:
            assert True
            if key != ('e2', 'i2', 'n1', 'r1', 's2', 't2', 'u1', 'v1'):
                assert False

        elif "unbuckramed" in value:
            assert True
            if key != ('a1', 'b1', 'c1', 'd1', 'e1', 'k1', 'm1', 'n1', 'r1', 'u2'):
                assert False
        elif "zwitterionic" in value:
            assert True
            if key != ('c1', 'e1', 'i3', 'n1', 'o1', 'r1', 't2', 'w1', 'z1'):
                assert False
