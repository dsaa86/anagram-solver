import os, sys, json, requests, time, hashlib

from matplotlib.pylab import permutation

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")

import tkinter as tk
from tkinter import *
from tkinter import ttk

from PermutationsManagerThread import PermutationsManagerThread
from HashmapLookupThread import HashmapLookupThread
from APIRequestThread import APIRequestThread

from PermutationsManager import PermutationsManager
from RetrieveFromLocalDict  import RetrieveFromLocalDict

class InterfacePermutationManager:
    def __init__(self):
        # match_pattern_selection_monitor = tk.BooleanVar()
        # factorial_decomposition_selection_monitor = tk.BooleanVar()
        # heap_non_recursive_selection_monitor = tk.BooleanVar()
        # heap_recursive_selection_monitor = tk.BooleanVar()
        # standard_selection_monitor = tk.BooleanVar()
        # threaded_factorial_decomposition_selection_monitor = tk.BooleanVar()
        # threaded_heap_non_recursive_selection_monitor = tk.BooleanVar()
        # threaded_heap_recursive_selection_monitor = tk.BooleanVar()
        # threaded_standard_selection_monitor = tk.BooleanVar()
        # character_hash_map_selection_monitor = tk.BooleanVar()
        # api_selection_monitor = tk.BooleanVar()


            # [match_pattern_selection_monitor, "Match Pattern"],

        # checkbox_collection_manager = [ 
        #     [factorial_decomposition_selection_monitor, "Factorial Decomposition"],
        #     [heap_non_recursive_selection_monitor, "Heap Non-Recursive"],
        #     [heap_recursive_selection_monitor, "Heap Recursive"],
        #     [standard_selection_monitor, "Standard"],
        #     [threaded_factorial_decomposition_selection_monitor, "Threaded Factorial Decomposition"],
        #     [threaded_heap_non_recursive_selection_monitor, "Threaded Heap Non-Recursive"],
        #     [threaded_heap_recursive_selection_monitor, "Threaded Heap Recursive"],
        #     [threaded_standard_selection_monitor, "Threaded Standard"],
        #     [character_hash_map_selection_monitor, "Character Hash Map"],
        #     [api_selection_monitor, "Words API Lookup"]
        # ]


        self.checkbox_collection_manager = [ 
            [tk.BooleanVar(), "Factorial Decomposition"],
            [tk.BooleanVar(), "Heap Non-Recursive"],
            [tk.BooleanVar(), "Heap Recursive"],
            [tk.BooleanVar(), "Standard"],
            [tk.BooleanVar(), "Threaded Factorial Decomposition"],
            [tk.BooleanVar(), "Threaded Heap Non-Recursive"],
            [tk.BooleanVar(), "Threaded Heap Recursive"],
            [tk.BooleanVar(), "Threaded Standard"],
            [tk.BooleanVar(), "Character Hash Map"],
            [tk.BooleanVar(), "Words API Lookup"]
        ]

        self.permutation_response_output__valid_permutations = StringVar()
        self.permutation_response_output__valid_permutations_matches = StringVar()
        self.permutation_response_output__valid_hashes = StringVar()
        self.permutation_response_output__valid_api_responses = StringVar()

        self.setDefaultPermutationResponseOutput()

    def joinListOfStrings(self, list_of_strings):
        return ", ".join(list_of_strings)

    def checkIfAllPermutationOptionsInCheckboxManagerAreIdentical(self):
        selection_monitor = [ checkbox[0].get for checkbox in self.checkbox_collection_manager ]
        
        selected_checker = True
        unselected_checker = True
        for value in selection_monitor:
            selected_checker = False if value == False else selected_checker
            unselected_checker = False if value == True else unselected_checker

        # It should be impossible for both to be True
        if selected_checker and unselected_checker:
            raise ValueError("Both checkers are True")
        # The following conditions are possible
        elif selected_checker:
            return [True, True]
        elif unselected_checker:
            return [True, False]
        else:
            return [False]


    def resetCheckboxes(self):
        for checkbox in self.checkbox_collection_manager:
            checkbox[0].set(False)

    def setDefaultPermutationResponseOutput(self):
        self.setPermutationResponseOutput("valid_permutations", "No permutations generated")
        self.setPermutationResponseOutput("valid_permutations_matches", "No matches found")
        self.setPermutationResponseOutput("valid_hashes", "No hashes generated")
        self.setPermutationResponseOutput("valid_api_responses", "No API responses generated")

    def setPermutationResponseOutput(self, response_type, response):

        # Two possible ValueErrors are raised, so len() == 0 is a generic exception to make differentiating easier
        if response_type not in ["valid_permutations", "valid_permutations_matches", "valid_hashes", "valid_api_responses"]:
            raise ValueError(f"Invalid response type: {response_type}")
        
        if len(response) == 0:
            raise Exception("Response is empty")

        if response_type == "valid_permutations":
            self.permutation_response_output__valid_permutations.set(response)
        elif response_type == "valid_permutations_matches":
            self.permutation_response_output__valid_permutations_matches.set(response)
        elif response_type == "valid_hashes":
            self.permutation_response_output__valid_hashes.set(response)
        elif response_type == "valid_api_responses":
            self.permutation_response_output__valid_api_responses.set(response)


    def extractSelectedPermutationsFromCheckboxManager(self):
        return [ index for index, checkbox in enumerate(self.checkbox_collection_manager) if checkbox[0].get() ]


    def generateThreadsForPermutationGeneration(self, selected_permutation_types, anagram) -> list:
        """
            selected_permutation_types is a list of ints.
            The ints correspond to the following permutation types:

            0: Factorial Decomposition
            1: Heap Non-Recursive
            2: Heap Recursive
            3: Standard
            4: Threaded Factorial Decomposition
            5: Threaded Heap Non-Recursive
            6: Threaded Heap Recursive
            7: Threaded Standard
            8: Character Hash Map
            9: Words API Lookup

            These ints are based on the order of the checkboxes in the checkbox manager variable.
        """
        threads = []
        for element in selected_permutation_types:
            thread = None
            if element in [0,1,2,3,4,5,6,7]:
                thread = PermutationsManagerThread(anagram, element)
            if element == 8:
                thread = HashmapLookupThread(anagram)
            if element == 9:
                thread = APIRequestThread(anagram)
            threads.append(thread)

        return threads


    def startThreadsForPermutationGeneration(self, threads) -> list:
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        return threads


    def extractResultsFromOutput(self, output, perm_type) -> bool:
        permutation_output_destination = {
            "permutations": "valid_permutations",
            "permutations_matches": "valid_permutations_matches",
            "hashmap": "valid_hashes",
            "api": "valid_api_responses"
        }

        for result in output:
            # We are searching for a specific type of permutation; move to the next result if this is not a matching type
            if result["type"] != perm_type:
                continue
            try:
                permutation_output = self.getOutputFromPermutationResults(result, perm_type)

                self.setPermutationResponseOutput(permutation_output_destination[perm_type], permutation_output)
            except Exception:
                self.setPermutationResponseOutput(permutation_output_destination[perm_type], "No valid permutations generated")

            if perm_type == "permutations":
                local_dict_result_string = self.searchLocalDictForMatchingPermutationsAndReturnAsString(result)

                self.setPermutationResponseOutput(permutation_output_destination["permutations_matches"], local_dict_result_string)
            return True
        return False
    
    
    def getOutputFromPermutationResults(self, result, perm_type):
            if perm_type == "hashmap":
                return result["results"]["results"]
            elif perm_type == "api":
                return result["results"]
            elif perm_type == "permutations":
                return self.stringifyPermutationsOutput(result)
    

    def searchLocalDictForMatchingPermutationsAndReturnAsString(self, result) -> str:
        local_dict_results = self.searchLocalDictForMatchingPermutations(result)
        if len(local_dict_results) == 0:
            return "No matches found"
        return self.joinListOfStrings(local_dict_results)
    

    def stringifyPermutationsOutput(self, result) -> str:
        # Lists are passed by reference, so we need to copy the list to avoid modifying the original
        raw_result = result["results"]["permutations"].copy()
        
        # The GUI can't display more than 50 perms without becomming cluttered
        if len(raw_result) > 50:
            raw_result = raw_result[:50]

        return self.joinListOfStrings(raw_result)
    

    def searchLocalDictForMatchingPermutations(self, result) -> list:
        local_dict = RetrieveFromLocalDict(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")
        return [ permutation for permutation in result["results"]["permutations"] if local_dict.retrieveFromLocalDict(permutation) ]
    

    def gatherDataForUploadToServer(self, output):
        keys = []
        data_set = []
        for result in output:
            if result["type"] in ["permutations", "hashmap"]:
                hashed_key = self.generateHashKeyForDynamoUpload(result)
                keys.append(hashed_key)
                data = self.generateUploadDataSet(result, hashed_key)
                data_set.append(data)
        
            raise ValueError("Number of keys provided does not match number of values.") if len(keys) != len(data_set) else None
        
        # The AWS lambda function iterates over the data by enumerating the "keys" list in the request_data dict
        request_data = {
            "keys" : keys,
        }
        # We also use the enumeration locally to add the data to the dict in the correct order
        for index, key in enumerate(keys):
            request_data[key] = data_set[index]

        return self.uploadOutputToServer(request_data)


    def uploadOutputToServer(self, request_data):
        headers = {"Content-Type": "application/json"}
        data = json.dumps(request_data)
        url = "https://wxu8uvavv0.execute-api.us-west-2.amazonaws.com/anagram_solver-dev/permutations/add"

        return requests.post(url, headers=headers, data=data)


    def generateHashKeyForDynamoUpload(self, result):
        hashed_key_string = f"Time:{time.time()}Type:{result['type']}"
        return hashlib.sha256(hashed_key_string.encode()).hexdigest()
    

    def generateUploadDataSet(self, result, hashed_key):
        return {
                    "ID" : hashed_key,
                    "Sort": result["algorithm"],
                    "type" : result["results"]["type"],
                    "input" :result["results"]["input"],
                    "input_length":len(result["results"]["input"]),
                    "permutations" :result["results"]["permutations"],
                    "permutation_count" : len(result["results"]["permutations"]),
                    "run_time": str(result["results"]["run_time"])
                }



    # WARN: THIS ALL NEEDS TO BE DIRECTLY IN THE UI


    # def startGeneration(self):

    #     # All checkboxes are unchecked - display error to user
    #     if self.checkIfAllPermutationOptionsInCheckboxManagerAreIdentical() == [True, False]:
    #         raise ValueError("No permutation types selected")

    #     # Lock all checkboxes and input

    #     # Perform generation

    #     # Output

    #     # Reset

    #     # Unlock all checkboxes and input



    #     resetResponseOutput()

    #     anagram = anagram_input.get()

    #     selected_permutation_types = extractSelectedPermutationTypes()
        
    #     threads = generateThreads(selected_permutation_types, anagram)
    #     startThreads(threads)
    #     output = [thread.results for thread in threads]
    #     threads = []
    #     # for thread in threads:
    #     #     # thread.join()
    #     #     output.append(thread.results)

    #     successful_permutation_extraction = extractPermutationsResultsFromOutput(output)
    #     successful_hash_extraction = extractHashResultsFromOutput(output)
    #     successful_api_extraction = extractApiResultsFromOutput(output)

    #     uploadOutputToServer(output)

    #     resetCheckboxes()

response = ["valid_permutations", "valid_permutations_matches", "valid_hashes", "valid_api_responses"]
empty_response = []

print("".join(empty_response))