
import copy
import random
input = [[5, 4, 0], [6,1,8], [7,3,2]]

def expand(initial_state):
    unchanged_list = copy.deepcopy(initial_state)
    new_list = []
    a = """
                        Starting Input:
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                            """.format(initial_state[0][0], initial_state[0][1], initial_state[0][2], initial_state[1][0], initial_state[1][1], initial_state[1][2],
                                       initial_state[2][0], initial_state[2][1], initial_state[2][2])
    print(a)


    while True:
        for i in initial_state[0]:
            if i == 0:
                index_value = initial_state[0].index(0)  # Finding the which index include zero
                if index_value == 0:#  checking if 0 inside the list
                    temp = initial_state[0][0]
                    initial_state[0][0] = initial_state[0][1]  #creating the paths
                    initial_state[0][1] = temp
                    new_list.append(initial_state)
                    temp2 = unchanged_list[0][1]
                    unchanged_list[0][1] = unchanged_list[1][1]
                    unchanged_list[1][1] = temp2
                    new_list.append(unchanged_list)
                    return new_list
                elif index_value == 1: # checking if 0 inside the list
                    return initial_state #creating the paths
                elif index_value == 2: # checking if 0 inside the list
                    temp1 = initial_state[0][1]
                    initial_state[0][1] = initial_state[0][2] #creating the paths
                    initial_state[0][2] = temp1
                    new_list.append(initial_state)
                    temp = unchanged_list[0][2]
                    unchanged_list[0][2] = unchanged_list[1][2]
                    unchanged_list[1][2]= temp
                    new_list.append(unchanged_list)
                    print("Path or Paths:")
                    return  new_list

        for j in initial_state[1]:
            if j == 0:
                second_index_value = initial_state[1].index(0) # Finding the which index include zero
                if second_index_value == 0: # checking if 0 inside the list
                    return initial_state #creating the paths
                elif second_index_value == 1: # checking if 0 inside the list
                    return True #creating the paths

                elif second_index_value == 2: # checking if 0 inside the list
                    return initial_state #creating the paths

        for k in initial_state[2]:
            if k == 0:
                third_index_value = initial_state[2].index(0)# Finding the which index include zero
                if third_index_value == 0: # checking if 0 inside the list
                    temp = initial_state[2][0]
                    initial_state[2][0] = initial_state[2][1]
                    initial_state[2][1] = temp   #creating the paths
                    new_list.append(initial_state)

                    temp2 = unchanged_list[1][0]
                    unchanged_list[1][0] = unchanged_list[2][0]
                    unchanged_list[2][0] = temp2
                    new_list.append(unchanged_list)
                    return new_list
                elif third_index_value == 1: # checking if 0 inside the list
                    return initial_state #creating the paths
                elif third_index_value == 2: # checking if 0 inside the list
                    temp = initial_state[1][2]
                    initial_state[1][2] = initial_state[2][2]
                    initial_state[2][2] = temp
                    new_list.append(initial_state)
                    temp2 = unchanged_list[2][1] #creating the paths
                    unchanged_list[2][1] = unchanged_list[2][2]
                    unchanged_list[2][2] = temp2
                    new_list.append(unchanged_list)
                    return new_list
                else:
                    print("Couldn't Find The '0'")
def graph_search(initial_state):
    print(initial_state) # creating paths in 2D
    first_path = """
                        First Path:
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                            """.format(initial_state[0][0][0], initial_state[0][0][1], initial_state[0][0][2], initial_state[0][1][0], initial_state[0][1][1], initial_state[0][1][2],
                                       initial_state[0][2][0], initial_state[0][2][1], initial_state[0][2][2])
    second_path =  """
                        Second Path:
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                            """.format(initial_state[1][0][0], initial_state[1][0][1], initial_state[1][0][2], initial_state[1][1][0], initial_state[1][1][1], initial_state[1][1][2],
                                       initial_state[1][2][0], initial_state[1][2][1], initial_state[1][2][2])  # creating paths in 2D
    random_value = random.randint(0,1)
    if random_value == 0:
        if initial_state[0][0][1] == 0:
            temp = initial_state[0][1][1]
            initial_state[0][1][1] = initial_state[0][0][1] # reacing the goal state
            initial_state[0][0][1]= temp
            print(first_path)
            first_path = """
                        Goal State:
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                                        """.format(initial_state[0][0][0], initial_state[0][0][1], initial_state[0][0][2],
                                                   initial_state[0][1][0], initial_state[0][1][1], initial_state[0][1][2],
                                                   initial_state[0][2][0], initial_state[0][2][1], initial_state[0][2][2]) # return the goal state in 2d
            return first_path
        elif initial_state[0][1][0] == 0:
            temp = initial_state[0][1][1]
            initial_state[0][1][1] = initial_state[0][1][0] # reacing the goal state
            initial_state[0][1][0] = temp
            print(first_path)
            first_path = """
                                    Goal State:
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                                """.format(initial_state[0][0][0], initial_state[0][0][1],
                                                           initial_state[0][0][2],
                                                           initial_state[0][1][0], initial_state[0][1][1],
                                                           initial_state[0][1][2],
                                                           initial_state[0][2][0], initial_state[0][2][1],
                                                           initial_state[0][2][2]) # return the goal state in 2d
            return first_path
        elif initial_state[0][1][2] == 0:
            temp = initial_state[0][1][1]
            initial_state[0][1][1] = initial_state[0][1][2] # reacing the goal state
            initial_state[0][1][2] = temp
            print(first_path)
            first_path = """
                                    Goal State:
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                                """.format(initial_state[0][0][0], initial_state[0][0][1],
                                                           initial_state[0][0][2],
                                                           initial_state[0][1][0], initial_state[0][1][1],
                                                           initial_state[0][1][2],
                                                           initial_state[0][2][0], initial_state[0][2][1],
                                                           initial_state[0][2][2]) # return the goal state in 2d
            return first_path
        elif initial_state[0][2][1] == 0:
            temp = initial_state[0][1][1]
            initial_state[0][1][1] = initial_state[0][2][1] # reacing the goal state
            initial_state[0][2][1] = temp
            print(first_path)
            first_path = """
                                    Goal State:
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                                """.format(initial_state[0][0][0], initial_state[0][0][1],
                                                           initial_state[0][0][2],
                                                           initial_state[0][1][0], initial_state[0][1][1],
                                                           initial_state[0][1][2],
                                                           initial_state[0][2][0], initial_state[0][2][1],
                                                           initial_state[0][2][2]) # return the goal state in 2d
            return first_path

    elif random_value == 1:
        if initial_state[1][0][1] == 0:
            temp = initial_state[1][1][1]
            initial_state[1][1][1] = initial_state[1][0][1] # reacing the goal state
            initial_state[1][0][1]= temp
            print(second_path)
            second_path = """
                                    Goal State:
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                        """.format(initial_state[1][0][0], initial_state[1][0][1],
                                                   initial_state[1][0][2], initial_state[1][1][0],
                                                   initial_state[1][1][1], initial_state[1][1][2],
                                                   initial_state[1][2][0], initial_state[1][2][1],
                                                   initial_state[1][2][2]) # return the goal state in 2d
            return second_path
        elif initial_state[1][1][0] == 0:
            temp = initial_state[1][1][1]
            initial_state[1][1][1] = initial_state[1][1][0] # reacing the goal state
            initial_state[1][1][0] = temp
            print(second_path)
            second_path = """
                                    Goal State:
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                        """.format(initial_state[1][0][0], initial_state[1][0][1],
                                                   initial_state[1][0][2], initial_state[1][1][0],
                                                   initial_state[1][1][1], initial_state[1][1][2],
                                                   initial_state[1][2][0], initial_state[1][2][1],
                                                   initial_state[1][2][2]) # return the goal state in 2d
            return second_path
        elif initial_state[1][1][2] == 0:
            temp = initial_state[1][1][1]
            initial_state[1][1][1] = initial_state[1][1][2] # reacing the goal state
            initial_state[1][1][2] = temp
            print(second_path)
            second_path = """
                        Goal State:
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                        +++++++++++++++++++
                        +  {}  +  {}  +  {}  +
                        +++++++++++++++++++
                                        """.format(initial_state[1][0][0], initial_state[1][0][1],
                                                   initial_state[1][0][2], initial_state[1][1][0],
                                                   initial_state[1][1][1], initial_state[1][1][2],
                                                   initial_state[1][2][0], initial_state[1][2][1],
                                                   initial_state[1][2][2]) # return the goal state in 2d
            return second_path
        elif initial_state[1][2][1] == 0:
            temp = initial_state[0][1][1]
            initial_state[1][1][1] = initial_state[1][2][1] # reacing the goal state
            initial_state[1][2][1] = temp
            print(second_path)
            second_path = """
                                    Goal State:
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                    +++++++++++++++++++
                                    +  {}  +  {}  +  {}  +
                                    +++++++++++++++++++
                                        """.format(initial_state[1][0][0], initial_state[1][0][1],
                                                   initial_state[1][0][2], initial_state[1][1][0],
                                                   initial_state[1][1][1], initial_state[1][1][2],
                                                   initial_state[1][2][0], initial_state[1][2][1],
                                                   initial_state[1][2][2]) # return the goal state in 2d
            return second_path
print(graph_search(expand(input)))













