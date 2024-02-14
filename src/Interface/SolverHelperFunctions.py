def resetCheckboxes():
    for checkbox in checkbox_collection_manager:
        checkbox[0].set(False)

def resetResponseOutput():
    valid_permutations.set("No permutations generated")
    valid_permutations_matches.set("No matches found")
    valid_hashes.set("No hashes generated")
    valid_api_responses.set("No API responses generated")

def extractSelectedPermutationTypes():
    selected_permutation_types = []
    for index, checkbox in enumerate(checkbox_collection_manager):
        if checkbox[0].get():
            selected_permutation_types.append(index)

    return selected_permutation_types


def generateThreads(selected_permutation_types, anagram) -> list:
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


def startThreads(threads) -> list:
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return threads


def extractPermutationsResultsFromOutput(output) -> bool:
    success = False
    for result in output:
        if result["type"] == "permutations":
            permutation_results = result["results"]["permutations"]
            trimmed_permutation_results = permutation_results.copy()
            if len(trimmed_permutation_results) > 50:
                trimmed_permutation_results = trimmed_permutation_results[:50]
            permutations_str = ", ".join(trimmed_permutation_results)
            valid_permutations.set(permutations_str)

            local_dict = RetrieveFromLocalDict(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")

            local_dict_results = []

            for permutation in permutation_results:
                if local_dict.retrieveFromLocalDict(permutation):
                    local_dict_results.append(permutation)
            if len(local_dict_results) > 0:
                processed_local_dict_results = ", ".join(local_dict_results)
                valid_permutations_matches.set(processed_local_dict_results)
            else:
                valid_permutations_matches.set("No matches found")
            success = True
            break

    return success

def extractHashResultsFromOutput(output) -> bool:
    success = False
    for result in output:
        if result["type"] == "hashmap":
            hashmap_results = result["results"]["results"]
            valid_hashes.set(hashmap_results)
            success = True
            break
    return success


def extractApiResultsFromOutput(output) -> bool:
    success = False
    for result in output:
        if result["type"] == "api":
            api_results = result["results"]
            valid_api_responses.set(api_results)
            success = True
            break

    return success


def uploadOutputToServer(output):
    keys = []
    data_set = []
    for result in output:
        if result["type"] in ["permutations", "hashmap"]:
            hashed_key = ""
            if result["type"] == "permutations":
                str_input = "".join(result['results']['input'])
                hashed_key_string = (f"Time:{time.time()}Input:{str_input}Type:{result['algorithm']}")
                hashed_key = hashlib.sha256(hashed_key_string.encode()).hexdigest()
            else:
                hashed_key_string = (f"Time:{time.time()}Type:{result['type']}")
                hashed_key = hashlib.sha256(hashed_key_string.encode()).hexdigest()

            keys.append(hashed_key)

            data = {
                "ID" : hashed_key,
                "Sort": result["algorithm"],
                "type" : result["results"]["type"],
                "input" :result["results"]["input"],
                "input_length":len(result["results"]["input"]),
                "permutations" :result["results"]["permutations"],
                "permutation_count" : len(result["results"]["permutations"]),
                "run_time": str(result["results"]["run_time"])
            }

            data_set.append(data)
    
    if len(keys) != len(data_set):
        return{
            'statusCode': 400,
            'body': json.dumps('Number of keys provided does not match number of values.')
        }
    
    request_data = {
        "keys" : keys,
    }

    for index, key in enumerate(keys):
        request_data[key] = data_set[index]

    headers = {"Content-Type": "application/json"}
    data = json.dumps(request_data)
    url = "https://wxu8uvavv0.execute-api.us-west-2.amazonaws.com/anagram_solver-dev/permutations/add"

    response = requests.post(url, headers=headers, data=data)

    print(response.json())



def startGeneration():

    resetResponseOutput()

    anagram = anagram_input.get()

    selected_permutation_types = extractSelectedPermutationTypes()
    
    threads = generateThreads(selected_permutation_types, anagram)
    startThreads(threads)
    output = [thread.results for thread in threads]
    threads = []
    # for thread in threads:
    #     # thread.join()
    #     output.append(thread.results)

    successful_permutation_extraction = extractPermutationsResultsFromOutput(output)
    successful_hash_extraction = extractHashResultsFromOutput(output)
    successful_api_extraction = extractApiResultsFromOutput(output)

    uploadOutputToServer(output)

    resetCheckboxes()