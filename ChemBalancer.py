import tkinter as tk
from pathlib import Path
import sys

from collections import defaultdict
from fractions import Fraction
import math

def get_numeric_value(formula: str, index: int) -> tuple[Fraction, int]:
    count = ""
    while index < len(formula) and (formula[index].isdecimal() or formula[index] == "."):
        count += formula[index]
        index += 1
    return (Fraction(count) if count != "" else Fraction("1")), index

def parse_formula(formula: str, index: int, positive_coefficient: bool) -> tuple[dict, int, bool]:
    coefficient = 1 if positive_coefficient else -1
        
    element_count = defaultdict(int)
    while index < len(formula):
        char = formula[index]

        if char.isupper():
            element = char
            index += 1

            while index < len(formula) and formula[index].islower():
                element += formula[index]
                index += 1
            count, index = get_numeric_value(formula, index)
            element_count[element] += coefficient * count

        elif char in "({[":
            inside, index, positive_coefficient = parse_formula(formula, index + 1, positive_coefficient)
            multiplier, index = get_numeric_value(formula, index + 1)
            for element, count in inside.items():
                element_count[element] += multiplier * count

        elif char in "]})":
            return element_count, index, positive_coefficient

        elif char == "·":
            mol, index = get_numeric_value(formula, index + 1)
            hydrate, index, positive_coefficient = parse_formula(formula, index, positive_coefficient)
            for element, count in hydrate.items():
                element_count[element] += mol * count

        else:
            index += 1
            
    return element_count, index, positive_coefficient

def gauss_jordan_elimination(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    m = len(matrix)           # Number of row
    n = len(matrix[0])        # Number of column

    pivot_row = 0
    for pivot_column in range(n):
        if pivot_row >= m: break

        find_nonzero = pivot_row
        while find_nonzero < m and matrix[find_nonzero][pivot_column] == 0:
            find_nonzero += 1
        if find_nonzero < m:
            matrix[pivot_row], matrix[find_nonzero] = matrix[find_nonzero], matrix[pivot_row]
        else:
            continue
        pivot = matrix[pivot_row][pivot_column]

        for column in range(n):
            matrix[pivot_row][column] /= pivot     # Normalizing the row
        for row in range(m):
            if row == pivot_row: continue

            multiplier = matrix[row][pivot_column]
            for column in range(n):
                matrix[row][column] -= multiplier * matrix[pivot_row][column]     # Eliminating other row
        
        pivot_row += 1

    return matrix

def find_rank_of_rref(matrix: list[list[Fraction]]) -> int:
    #This rank algorithm is specifically for RREF where the we know that no zeros row is in the middle, only at the bottom
    n = len(matrix[0])        # Number of column

    rank = 0
    zero_row = [Fraction("0")] * n
    for row in matrix:
        if row == zero_row:
            return rank
        else:
            rank += 1
    return rank

def simplify_ratio(ratio: list[Fraction]) -> list[int]:
    denominators = [f.denominator for f in ratio]
    common_muliplier = math.lcm(*denominators)

    return [int(f * common_muliplier) for f in ratio]
    
def rref_to_stoichiometric_coefficient(matrix: list[list[Fraction]]) -> list[int]:
    m = len(matrix)           # Number of row
    n = len(matrix[0])        # Number of column

    rank = find_rank_of_rref(matrix)
    free_columns = n - rank  # From DoF and rank-nullity theorem
    stoichiometric_coefficient = []
    for i in range(rank):
        total_free_coefficient = 0
        for j in range(free_columns):
            total_free_coefficient += matrix[i][-1 - j]

        coefficient = abs(total_free_coefficient)
        stoichiometric_coefficient.append(coefficient)
    stoichiometric_coefficient += [Fraction(1)] * free_columns

    return simplify_ratio(stoichiometric_coefficient)

def balancing_equation(equation: str) -> str:
    equation = equation.split()

    compound_hash_list = []
    positive_stoichiometric_coefficient = True
    for compound in equation:
        if compound == "+":
            continue
        elif compound == "->":
            positive_stoichiometric_coefficient = False
            continue
        else:
            compound_hash_list.append(parse_formula(compound, 0, positive_stoichiometric_coefficient)[0])

    all_keys = set().union(*compound_hash_list)
    standardized_compound_hash_list = [{key: hashTable.get(key, Fraction("0")) for key in all_keys} for hashTable in compound_hash_list]

    transposed_augmented_matrix = [list(hashTable.values()) for hashTable in standardized_compound_hash_list]
    augmented_matrix = [list(row) for row in zip(*transposed_augmented_matrix)]

    rref_matrix = gauss_jordan_elimination(augmented_matrix) #  Warning augmented_matrix share same memory as rref_matrix!
    stoichiometric_coefficient = rref_to_stoichiometric_coefficient(rref_matrix)

    if stoichiometric_coefficient == [0] * len(stoichiometric_coefficient):
        return "Error: Cannot be balanced."

    balanced_equation = ""
    compound_index = 0
    for compound in equation:
        if compound in ("+", "->"):
            balanced_equation += " " + compound
        else:
            last_number_index = 0
            while last_number_index < len(compound) and (compound[last_number_index].isdecimal() or compound[last_number_index] == "."):
                last_number_index += 1
            coefficient = str(stoichiometric_coefficient[compound_index]) if stoichiometric_coefficient[compound_index] != 1 else ""
            balanced_equation += " " + coefficient + compound[last_number_index:]
            compound_index += 1

    return balanced_equation.strip()

# -------------- Tkinter --------------
def display_output():
    equation = entry.get().strip()

    balanced_equation = balancing_equation(equation)

    output_box.config(state="normal")

    output_box.delete("1.0", tk.END)

    output_box.insert(tk.END, f"The balanced equation:\n\n")
    output_box.insert(tk.END, f"{balanced_equation}")
    output_box.config(state = "disabled")

root = tk.Tk()
root.title("Chemical Reaction Balancer")

if getattr(sys, 'frozen', False):
    base_path = Path(sys._MEIPASS)
else:
    base_path = Path(__file__).parent

icon_path = base_path / "images" / "logo.ico"
root.iconbitmap(str(icon_path))

window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False,False)

label = tk.Label(root, text = "Enter The Chemical Reaction", font = ("Courier New", 11))
label.pack(pady = 5)

entry = tk.Entry(root, width = 40, fon = ("Courier New", 11))
entry.pack(pady = 5)

button = tk.Button(root, text = "Confirm", font = ("Courier New", 11), command = display_output)
button.pack(pady = 10)

output_box = tk.Text(root, height = 4, width = 50, font = ("Courier New", 11), state = "disabled")
output_box.pack(pady = 20)

root.mainloop()