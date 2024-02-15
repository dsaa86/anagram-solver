import tkinter as tk
from tkinter import *
from tkinter import ttk
import os, sys, requests, json
import matplotlib.pyplot as plt
import numpy as np


sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")

from PermutationsManager import PermutationsManager
from InterfacePermutationManager import InterfacePermutationManager


def startGeneration():
    pass


root = Tk()
root.title("Anagram Solver")
root.geometry("800x600")


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Solve Anagrams")
tabControl.add(tab2, text="Measure Algorithm Performance")
tabControl.pack(expand=1, fill="both")


permutations_manager = PermutationsManager()
interface_permutations_manager = InterfacePermutationManager()


main_frame = ttk.Frame(tab1, padding="20 20 30 30")
main_frame.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=5)
root.rowconfigure(0, weight=10)


ttk.Label(main_frame, text="Anagram Input:").grid(column=1, row=1, sticky=(W, E))

anagram_input = StringVar()
anagram_input_entry = ttk.Entry(main_frame, width=50, textvariable=anagram_input)
anagram_input_entry.grid(column=2, columnspan=2, row=1, sticky=(W,E))


row_accumulator = 3

for index, checkbox in enumerate(interface_permutations_manager.checkbox_collection_manager):
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
    interface_permutations_manager.checkbox_collection_manager[index].append(interface_checkbox)
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
valid_permutations_label = Message(main_frame, textvariable=interface_permutations_manager.permutation_response_output__valid_permutations, width=500, justify=LEFT).grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1


ttk.Label(main_frame, text="Valid Permutation Matches:").grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1
valid_permutations_matches_label = Message(main_frame, textvariable=interface_permutations_manager.permutation_response_output__valid_permutations_matches, width=500, justify=LEFT).grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1


ttk.Label(main_frame, text="Valid Hashes:").grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1
valid_hashes_label = Message(main_frame, textvariable=interface_permutations_manager.permutation_response_output__valid_hashes, width=500, justify=LEFT).grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1


ttk.Label(main_frame, text="Valid API Responses:").grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
row_accumulator +=1
valid_api_responses_label = Message(main_frame, textvariable=interface_permutations_manager.permutation_response_output__valid_api_responses, width=500, justify=LEFT).grid(column=1, columnspan=3, row=row_accumulator, sticky=(W,E))
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
