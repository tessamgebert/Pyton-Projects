import random

dict = {
    '0000' : '0',
    '0001' : '1',
    '0010' : '2',
    '0011' : '3',
    '0100' : '4',
    '0101' : '5',
    '0110' : '6',
    '0111' : '7',
    '1000' : '8',
    '1001' : '9',
    '1010' : '+',
    '1011' : '-',
    '1100' : '/',
    '1101' : '*',
    '1110' : '',
    '1111' : '',
}

# works!
def initialize_population(pop_size, genome_size):
    """Create an initial population of 20 individuals with genomes of 36 bits"""
    initial_pop = []
    for x in range(pop_size):
        individual = ''
        for i in range(genome_size):
            x = random.randint(0, 1)
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


def group_multi_samples_by_4(initial_pop):
    pop_splices = []
    for sample in initial_pop:
        species_splice = group_one_sample_by_4(sample)
        pop_splices.append(species_splice)
    return pop_splices

def convert_bin_to_operators_operands(group_list):
    """Take out each item (key) from list, then map to corresponding value from dictionary"""
    converted_pop = []
    converted_pop_spliced = []
    for i in group_list:
        for j in i:
            k = dict[j]
            converted_pop.append(k)
    for n in range(0, len(converted_pop), 9):
        x = converted_pop[n:n+9]
        converted_pop_spliced.append(x)
    del converted_pop[:]
    for i in converted_pop_spliced:
        i = ''.join(i)
        converted_pop.append(i)
    return converted_pop

def is_operand(i):
    return (
    i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9')


def is_operator(i):
    return (i == '+' or i == '-' or i == '/' or i == '*')

# IT WORKS
def create_expression(a):
    expression = ''
    need_operand = True  # if true, need operand, if false, need operator
    for i in range(0, len(a)):
        if need_operand == True:
            if is_operand(a[i]):
                expression += a[i]
                need_operand = False
        else:
            if is_operator(a[i]):
                expression += a[i]
                need_operand = True
    if is_operator(a[-1]):
        expression = expression[0:-1]
    return expression

def evaluate_expression(organized_expression):
    answer = 0
    if len(organized_expression) == 0:
        return answer
    else:
        answer = float(organized_expression[0:1])
        organized_expression = organized_expression[1:len(organized_expression)]
    while len(organized_expression) != 0:
        next_2_vals = organized_expression[0:2]
        if next_2_vals == '/0':
            return 0
        organized_expression = organized_expression[2:len(organized_expression)]
        answer = eval(str(answer)+(next_2_vals))
    return answer

#test fitness
def test_fitness(convert_indi):
    x = convert_indi
    if x == 23:
        return 1
    fitness = 1 / abs(23 - x)
    return fitness

def normal_fit(individual, total_fit):
    normalized_fitness = individual / total_fit
    return normalized_fitness

def select_person(accumulate_weight,rand_num):
    selected_individual = accumulate_weight[0]
    for weight in accumulate_weight:
        if weight < rand_num:
            selected_individual = weight
    return selected_individual


generation = 0
while True:
    pop = initialize_population(20,36)
    grouped = group_multi_samples_by_4(pop)
    conversion = convert_bin_to_operators_operands(grouped)
    print conversion

    entire_conversion = ()
    all_conversions = []
    for each_genome in range(len(conversion)):
        my_expression = create_expression(conversion[each_genome])
        print my_expression
        solution = evaluate_expression(my_expression)
        all_conversions.append(solution)
        print 'raw function:\n' , conversion[each_genome]
        print 'clean function:\n' , my_expression
        print 'solved:\n' , solution,'\n'
    fit_list = []
    for individual in all_conversions:
        fit_list.append(test_fitness(individual))
    total_fitness = 0
    for individual in fit_list:
      total_fitness += individual

    weight = []
    for individual in fit_list:
        weight.append(normal_fit(individual, total_fitness))

    sort_fit_list = sorted(fit_list, key = float, reverse = True)
    total_weight = 0
    accumulated_weight = []
    for individual in sort_fit_list:
        total_weight += normal_fit(individual, total_fitness)
        accumulated_weight.append(total_weight)
    mom_list = []
    for i in range(0,20):
        random_number = random.random()
        accumulated_index = accumulated_weight.index(select_person(accumulated_weight, random_number))
        picked_indiv = sort_fit_list[accumulated_index]
        fit_list_index = fit_list.index(picked_indiv)
        mom = pop[fit_list_index]
        mom_list.append(mom)
    dad_list = []
    for i in range(0,20):
        random_number = random.random()
        accumulated_index = accumulated_weight.index(select_person(accumulated_weight, random_number))
        picked_indiv = sort_fit_list[accumulated_index]
        fit_list_index = fit_list.index(picked_indiv)
        dad = pop[fit_list_index]
        dad_list.append(dad)
    child = []
    children = []
    i = 0
    solved_children = []
    for j in range(0,20):
        child = []
        for bit in range(0,36):
            rand_number = random.randint(0,1)
            if rand_number == 1:
                child.append(dad_list[j][bit])
            elif rand_number == 0:
                child.append(mom_list[j][bit])
        children.append("".join(child))
    for kid in children:
        for index in range(0, len(kid)):
            num = random.random
            if num < (0.0278):
                if kid[index] == '1':
                    kid[index] = '0'
                if kid[index] == '0':
                    kid[index] = '1'    


    grouped_children = group_multi_samples_by_4(children)
    converted_children = convert_bin_to_operators_operands(grouped_children)
    expressed_children = []
    for i in converted_children:
        expressed_children.append(create_expression(i))
    eval_children = []
    for i in expressed_children:
        eval_children.append(evaluate_expression(i))
    if 23 in eval_children:
        index_of_23 = eval_children.index(23.0)
        print ("yay! done!")
        print 'raw function:\n' , converted_children[index_of_23]
        print 'clean function:\n' , expressed_children[index_of_23]
        print 'solved:\n' , 23,'\n'
        print 'found on generation:\n' , generation
        exit()
    print eval_children
    generation += 1


