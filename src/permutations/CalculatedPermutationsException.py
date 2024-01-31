class CalculatedPermutationsException(Exception):
    def __init__(self, calculated_total_permutations: int, output_list: list):
        self.message = f"Expected {calculated_total_permutations} permutations, but got {len(output_list)}"
        super().__init__(self.message)