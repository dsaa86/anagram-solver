# import os
# import sys
# from threading import local

# import pytest

# sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/anagramsolver/")

# import AnagramSolver


# @pytest.fixture
# def setup_anagram_solver():
#     hello_solver = AnagramSolver.AnagramSolver("LOEHL", remote=True)
#     aardvark_solver = AnagramSolver.AnagramSolver("VARARAKD", remote=True)
#     uncharacteristically_solver = AnagramSolver.AnagramSolver("RHELYIAISACRTLCCATNU", remote=True)
#     yield uncharacteristically_solver, hello_solver, aardvark_solver

#     hello_solver = None
#     aardvark_solver = None

# def test_regex_raises_exception_for_non_remote_solver(setup_anagram_solver):
#     uncharacteristically_solver, hello_solver, aardvark_solver = setup_anagram_solver

#     false_remote_solver = AnagramSolver.AnagramSolver("LOEHL", remote=False)
#     false_remote_solver_true_local_solver = AnagramSolver.AnagramSolver("LOEHL", remote=False, local=True)

#     with pytest.raises(NotImplementedError) as e_info:
#         false_remote_solver.buildRegexForRemote()
#         false_remote_solver_true_local_solver.buildRegexForRemote()

#     try:
#         hello_solver.buildRegexForRemote()
#         aardvark_solver.buildRegexForRemote()
#         uncharacteristically_solver.buildRegexForRemote()
#     except NotImplementedError as e:
#         assert False


# def test_build_regex_for_remote(setup_anagram_solver):
#     uncharacteristically_solver, hello_solver, aardvark_solver = setup_anagram_solver

#     assert hello_solver.buildRegexForRemote() == "[L|O|E|H]{5}"
#     assert aardvark_solver.buildRegexForRemote() == "[V|A|R|K|D]{8}"
#     assert uncharacteristically_solver.buildRegexForRemote() == "[R|H|E|L|Y|I|A|S|C|T|N|U]{20}"


# def test_repeated_chars_in_anagram(setup_anagram_solver):
#     uncharacteristically_solver, hello_solver, aardvark_solver = setup_anagram_solver

#     assert hello_solver.buildRegexForRemote().count("L") == 1
    
#     assert aardvark_solver.buildRegexForRemote().count("A") == 1
#     assert aardvark_solver.buildRegexForRemote().count("R") == 1
#     assert aardvark_solver.buildRegexForRemote().count("K") == 1
#     assert aardvark_solver.buildRegexForRemote().count("D") == 1

#     assert uncharacteristically_solver.buildRegexForRemote().count("C") == 1
#     assert uncharacteristically_solver.buildRegexForRemote().count("A") == 1
#     assert uncharacteristically_solver.buildRegexForRemote().count("L") == 1
#     assert uncharacteristically_solver.buildRegexForRemote().count("R") == 1
#     assert uncharacteristically_solver.buildRegexForRemote().count("T") == 1
#     assert uncharacteristically_solver.buildRegexForRemote().count("I") == 1