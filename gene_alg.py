"""Genetic Algorithm
How to get 23
By: Tessa Gebert and Cindy Weng
"""

from random import randint
#pop_size = 20
#genome_size = 36


dict = {
    '0000': '0', 
    '0001': '1', 
    '0010': '2',
    '0011': '3', 
    "0100": "4",
    '0101': '5',
    '0110': '6', 
    '0111': '7',
    '1000': '8', 
    '1001': '9', 
    '1010': '+',
    '1011': '-',
    '1100': '/',
    '1101': '*',
    '1110': '',
    '1111': '',
}


def initialize_population():
    """Create an initial population of 20 individuals with genomes of 36 bits"""
    initial_pop = []
    for x in range(20):
        individual = ''
        for i in range(36):
            x = randint(0, 1)
            individual = individual + str(x)
        initial_pop.append(individual)
    return initial_pop


def group_one_sample_by_4(sample):
    species_splice = []
    n = 0
    for n in range(0, len(sample), 4):
        x = sample[n:n + 4]
        species_splice.append(x)
    return species_splice

init_pop = initialize_population()
def group_multi_samples_by_4(pop):
    #initial_pop = initialize_population()
    pop_splices = []
    for sample in pop:
        species_splice = group_one_sample_by_4(sample)
        pop_splices.append(species_splice)
    return pop_splices
init_pop_gr4 = group_multi_samples_by_4(init_pop)

def convert_bin_to_operators_operands(conversion):
    """Take out each item (key) from list, then map to corresponding value from dictionary"""
    converted_pop = []
    converted_pop_spliced = []
    for i in conversion:
        for j in i:
            k = dict[j]
            converted_pop.append(k)
    for n in range(0, len(converted_pop), 9):
        x = converted_pop[n:n+9]
        converted_pop_spliced.append(x)
    del converted_pop[:]
    for i in converted_pop_spliced:
        i = ''.join(i)
        # print(i)
        converted_pop.append(i)
    return converted_pop

def find_operator(person):
    position = 0
    for i in person:
        if i == '+' or i == '-' or i == '*' or i == '/':
            return position
        position += 1

def find_operand(person):
    position = 0
    for i in person:
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            return position
        position += 1


# converted_pop = convert_bin_to_operators_operands(init_pop_gr4)

# print find_operator(converted_pop[0])



        
# def create_expression(group_list):
#     converted_pop = convert_bin_to_operators_operands(group_list)
#     print converted_pop
#     operands = []
#     operators = []
#     for i in converted_pop:
#         for j in i:
#             t = (j)
#             if t == "+" or  t == "-"  or t == "*" or t == "/":
#                 operators.append(t)
#             else:
#                 operands.append(t)
#     return (operands, operators)
# print create_expression(init_pop_gr4)

'''
# def number_or_operator(operands)
'''