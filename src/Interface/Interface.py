import tkinter as tk
from tkinter import *
from tkinter import ttk
import os, sys, requests, hashlib, time, json
from urllib import response
from PermutationsManagerThread import PermutationsManagerThread
from HashmapLookupThread import HashmapLookupThread
from APIRequestThread import APIRequestThread
import matplotlib.pyplot as plt
import numpy as np


sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")

from PermutationsManager import PermutationsManager
from RetrieveFromLocalDict  import RetrieveFromLocalDict


# def resetCheckboxes():
#     for checkbox in checkbox_collection_manager:
#         checkbox[0].set(False)

# def resetResponseOutput():
#     valid_permutations.set("No permutations generated")
#     valid_permutations_matches.set("No matches found")
#     valid_hashes.set("No hashes generated")
#     valid_api_responses.set("No API responses generated")

# def extractSelectedPermutationTypes():
#     selected_permutation_types = []
#     for index, checkbox in enumerate(checkbox_collection_manager):
#         if checkbox[0].get():
#             selected_permutation_types.append(index)

#     return selected_permutation_types


# def generateThreads(selected_permutation_types, anagram) -> list:
#     threads = []
#     for element in selected_permutation_types:
#         thread = None
#         if element in [0,1,2,3,4,5,6,7]:
#             thread = PermutationsManagerThread(anagram, element)
#         if element == 8:
#             thread = HashmapLookupThread(anagram)
#         if element == 9:
#             thread = APIRequestThread(anagram)
#         threads.append(thread)

#     return threads


# def startThreads(threads) -> list:
#     for thread in threads:
#         thread.start()

#     for thread in threads:
#         thread.join()

#     return threads


# def extractPermutationsResultsFromOutput(output) -> bool:
#     success = False
#     for result in output:
#         if result["type"] == "permutations":
#             permutation_results = result["results"]["permutations"]
#             trimmed_permutation_results = permutation_results.copy()
#             if len(trimmed_permutation_results) > 50:
#                 trimmed_permutation_results = trimmed_permutation_results[:50]
#             permutations_str = ", ".join(trimmed_permutation_results)
#             valid_permutations.set(permutations_str)

#             local_dict = RetrieveFromLocalDict(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")

#             local_dict_results = []

#             for permutation in permutation_results:
#                 if local_dict.retrieveFromLocalDict(permutation):
#                     local_dict_results.append(permutation)
#             if len(local_dict_results) > 0:
#                 processed_local_dict_results = ", ".join(local_dict_results)
#                 valid_permutations_matches.set(processed_local_dict_results)
#             else:
#                 valid_permutations_matches.set("No matches found")
#             success = True
#             break

#     return success

# def extractHashResultsFromOutput(output) -> bool:
#     success = False
#     for result in output:
#         if result["type"] == "hashmap":
#             hashmap_results = result["results"]["results"]
#             valid_hashes.set(hashmap_results)
#             success = True
#             break
#     return success


# def extractApiResultsFromOutput(output) -> bool:
#     success = False
#     for result in output:
#         if result["type"] == "api":
#             api_results = result["results"]
#             valid_api_responses.set(api_results)
#             success = True
#             break

#     return success


# def uploadOutputToServer(output):
#     keys = []
#     data_set = []
#     for result in output:
#         if result["type"] in ["permutations", "hashmap"]:
#             hashed_key = ""
#             if result["type"] == "permutations":
#                 str_input = "".join(result['results']['input'])
#                 hashed_key_string = (f"Time:{time.time()}Input:{str_input}Type:{result['algorithm']}")
#                 hashed_key = hashlib.sha256(hashed_key_string.encode()).hexdigest()
#             else:
#                 hashed_key_string = (f"Time:{time.time()}Type:{result['type']}")
#                 hashed_key = hashlib.sha256(hashed_key_string.encode()).hexdigest()

#             keys.append(hashed_key)

#             data = {
#                 "ID" : hashed_key,
#                 "Sort": result["algorithm"],
#                 "type" : result["results"]["type"],
#                 "input" :result["results"]["input"],
#                 "input_length":len(result["results"]["input"]),
#                 "permutations" :result["results"]["permutations"],
#                 "permutation_count" : len(result["results"]["permutations"]),
#                 "run_time": str(result["results"]["run_time"])
#             }

#             data_set.append(data)
    
#     if len(keys) != len(data_set):
#         return{
#             'statusCode': 400,
#             'body': json.dumps('Number of keys provided does not match number of values.')
#         }
    
#     request_data = {
#         "keys" : keys,
#     }

#     for index, key in enumerate(keys):
#         request_data[key] = data_set[index]

#     headers = {"Content-Type": "application/json"}
#     data = json.dumps(request_data)
#     url = "https://wxu8uvavv0.execute-api.us-west-2.amazonaws.com/anagram_solver-dev/permutations/add"

#     response = requests.post(url, headers=headers, data=data)



# def startGeneration():

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



permutations_manager = PermutationsManager()

root = Tk()
root.title("Anagram Solver")
root.geometry("800x600")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Solve Anagrams")
tabControl.add(tab2, text="Measure Algorithm Performance")
tabControl.pack(expand=1, fill="both")


"""
    LOGIC AND UI WIDGETS FOR ANAGRAM SOLVER
"""


# Constants and variables used throughout the programme

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


#     # [match_pattern_selection_monitor, "Match Pattern"],

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

# valid_permutations = StringVar()
# valid_permutations.set("No permutations generated")
# valid_permutations_matches = StringVar()
# valid_permutations_matches.set("No matches found")
# valid_hashes = StringVar()
# valid_hashes.set("No hashes generated")
# valid_api_responses = StringVar()
# valid_api_responses.set("No API responses generated")

main_frame = ttk.Frame(tab1, padding="20 20 30 30")
main_frame.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=5)
root.rowconfigure(0, weight=10)

ttk.Label(main_frame, text="Anagram Input:").grid(column=1, row=1, sticky=(W, E))

anagram_input = StringVar()
anagram_input_entry = ttk.Entry(main_frame, width=50, textvariable=anagram_input)
anagram_input_entry.grid(column=2, columnspan=2, row=1, sticky=(W,E))

row_accumulator = 3

for index, checkbox in enumerate(checkbox_collection_manager):
    interface_checkbox = ttk.Checkbutton(
        main_frame,
        text=checkbox[1],
        variable=checkbox[0],
    ).grid(
        column=1,
        columnspan=2,
        row=row_accumulator,
        sticky=(W,E)
    )
    checkbox.append(interface_checkbox)
    row_accumulator += 1

start_lookup_button = ttk.Button(main_frame, text="Start Generation", command=startGeneration)
start_lookup_button.grid(
    column=1,
    columnspan=3,
    row=row_accumulator,
    sticky=(W,E)
)
row_accumulator += 1

ttk.Label(main_frame, text="Valid Permutations:").grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1
valid_permutations_label = Message(main_frame, textvariable=valid_permutations, width=500, justify=LEFT).grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1

ttk.Label(main_frame, text="Valid Permutation Matches:").grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1
valid_permutations_matches_label = Message(main_frame, textvariable=valid_permutations_matches, width=500, justify=LEFT).grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1

ttk.Label(main_frame, text="Valid Hashes:").grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1
valid_hashes_label = Message(main_frame, textvariable=valid_hashes, width=500, justify=LEFT).grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1

ttk.Label(main_frame, text="Valid API Responses:").grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1
valid_api_responses_label = Message(main_frame, textvariable=valid_api_responses, width=500, justify=LEFT).grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1



"""
    LOGIC AND UI WIDGETS FOR ALGORITHM PERFORMANCE MEASUREMENT
"""

def retrievePerformanceData():

    for index, element in enumerate(complete_performance_data_set):
        type = element["type"]
        headers = {
            "Content-Type": "application/json"
        }
        body = {"type": type}
        url = "https://wxu8uvavv0.execute-api.us-west-2.amazonaws.com/anagram_solver-dev/permutations/get"

        response = requests.get(url, headers=headers, data=json.dumps(body))
        print(response.json())
        response_body = response.json()["body"]
        response_body_json = json.loads(response_body)
        response_data = response_body_json["Items"]

        run_time_data = []
        permutation_count_data = []
        input_length_data = []


        for data_point in response_data:
            run_time_data.append(float(data_point["run_time"]))
            permutation_count_data.append(int(data_point["permutation_count"]))
            input_length_data.append(int(data_point["input_length"]))

        complete_performance_data_set[index]["performance_data"] = {
            "run_time": run_time_data,
            "permutation_count": permutation_count_data,
            "input_length": input_length_data
        }

    print(complete_performance_data_set)

    plotPerformanceData(complete_performance_data_set[0]["performance_data"])


def plotPerformanceData(data_set):
    anagram_length = np.array(data_set["input_length"])
    run_time = np.array(data_set["run_time"])

    fig, ax = plt.subplots()
    ax.scatter(anagram_length, run_time)

    ax.set(xlabel='Anagram Length', ylabel='Run Time (s)',
        title='Run Time vs. Anagram Length')
    ax.grid()
    fig.savefig("test.png")
    plt.show()





factorial_decomposition_performance_data_set = {
    "type" : "Factorial Decomposition",
    "performance_data" : []
}
heap_non_recursive_performance_data_set = {
    "type" : "Heap's Non-Recursive",
    "performance_data" : []
}
heap_recursive_performance_data_set = {
    "type" : "Heap's Recursive",
    "performance_data" : []
}
standard_performance_data_set = {
    "type" : "Standard Permutations",
    "performance_data" : []
}
threaded_factorial_decomposition_performance_data_set = {
    "type" : "Threaded Factorial Decomposition",
    "performance_data" : []
}
threaded_heap_non_recursive_performance_data_set = {
    "type" : "Threaded Heap's Non-Recursive",
    "performance_data" : []
}
threaded_heap_recursive_performance_data_set = {
    "type" : "Threaded Heap's Recursive",
    "performance_data" : []
}
threaded_standard_performance_data_set = {
    "type" : "Threaded Standard Permutations",
    "performance_data" : []
}
character_hash_map_performance_data_set = {
    "type" : "Hashmap Lookup",
    "performance_data" : []
}


complete_performance_data_set = [factorial_decomposition_performance_data_set, heap_non_recursive_performance_data_set, heap_recursive_performance_data_set, standard_performance_data_set, threaded_factorial_decomposition_performance_data_set, threaded_heap_non_recursive_performance_data_set, threaded_heap_recursive_performance_data_set, threaded_standard_performance_data_set, character_hash_map_performance_data_set]

retrieve_performance_data_button = ttk.Button(tab2, text="Retrieve Performance Data", command=retrievePerformanceData).grid(column=1, columnspan=3, row=1, sticky=(W,E))




root.mainloop()
