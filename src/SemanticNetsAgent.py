import random
import uuid


class State:
    def __init__(self, left_sheep, left_wolves, right_sheep, right_wolves, direction):
        self.id = uuid.uuid1()
        self.left_sheep = left_sheep
        self.left_wolves = left_wolves
        self.right_sheep = right_sheep
        self.right_wolves = right_wolves
        if direction != "right" and direction != "left":
            raise Exception("prev_trip is not valid value")
        self.direction = direction

    def is_valid(self):
        result = True
        if self.left_sheep < self.left_wolves:
            if self.left_sheep == 0:
                result = True
            else:
                result = False
        if self.right_sheep < self.right_wolves:
            if self.right_sheep == 0:
                result = True
            else:
                result = False
        return result

    def get_signature(self):
        return 'ls:%x,lw:%x,rs:%x,rw:%x,d:%s' % (
            self.left_sheep, self.left_wolves, self.right_sheep, self.right_wolves, self.direction)

# bfs node inspired by this udemy video
# https://www.udemy.com/course/advanced-algorithms-in-java/learn/lecture/2484016#overview
class Node:

    def __init__(self, state: State, parent, chosen_option):
        self.state = state
        self.parent = parent
        self.chosen_option = chosen_option
        self.neighbors = []
        self.visited = False

    def get_state(self):
        return self.state

    def get_state_signature(self):
        return self.state.get_signature()


class SemanticNetsAgent:

    def __init__(self):
        self.queue = []
        self.created_states = {}

    def solve(self, initial_sheep, initial_wolves):
        self.queue = []
        self.created_states = {}
        state = State(initial_sheep, initial_wolves, 0, 0, "left")
        node = Node(state, None, None)
        return self.bfs(node)

    # bfs algorithm inspired by this udemy video
    # https://www.udemy.com/course/advanced-algorithms-in-java/learn/lecture/2484016#overview
    def bfs(self, node):
        node.visited = True
        self.queue.append(node)
        while len(self.queue) != 0:
            node: Node = self.queue.pop()
            node.neighbors = self.get_neighbors_for(node)
            x = None
            for n in node.neighbors:

                # print("signature: " + n.get_state().get_signature() + " valid: " + str(n.get_state().is_valid()))
                if n.get_state().get_signature() not in self.created_states.keys():
                    key = n.get_state().get_signature()
                    self.created_states[key] = n
                    if n.visited != True:
                        n.visited = True
                        self.queue.append(n)
                        if self.solution_is_found(n.get_state()):
                            return self.get_path(n)
        return []

    def get_path(self, node: Node):
        path = []
        curr = node
        while curr.chosen_option != None:
            path.append(curr.chosen_option)
            curr = curr.parent
        return path

    def get_neighbors_for(self, parent):
        options = self.get_options_for_next_state(parent.get_state())
        neighbors = []
        for o in options:
            node = Node(o[1], parent, o[0])
            neighbors.append(node)
        return neighbors

    def get_options_for_next_state(self, state):
        smart_options = []
        default_options = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 1)]
        for o in default_options:
            next_state = self.calculate_new_state(state, o[0], o[1])

            smart_result = self.is_smart_option(next_state, o)
            if smart_result > 0:
                if smart_result == 1:
                    smart_options.insert(0, (o, next_state))
                if smart_result == 2:
                    smart_options.append((o, next_state))
                    # return smart_options
                    # return smart_options
        return smart_options

    def alternate_direction(self, direction):
        if direction == "left":
            return "right"
        else:
            return "left"

    def calculate_new_state(self, state, num_sheep, num_wolves):
        result = None
        next_direction = self.alternate_direction(state.direction)
        if next_direction == "right":
            left_sheep = state.left_sheep - num_sheep
            left_wolves = state.left_wolves - num_wolves
            right_sheep = state.right_sheep + num_sheep
            right_wolves = state.right_wolves + num_wolves
            result = State(left_sheep, left_wolves, right_sheep, right_wolves, next_direction)
        elif next_direction == "left":
            left_sheep = state.left_sheep + num_sheep
            left_wolves = state.left_wolves + num_wolves
            right_sheep = state.right_sheep - num_sheep
            right_wolves = state.right_wolves - num_wolves
            result = State(left_sheep, left_wolves, right_sheep, right_wolves, next_direction)
        else:
            raise Exception("Direction was not valid, you shouldn't see this.")
        return result

    def is_smart_option(self, state, option) -> bool:
        # 0 = not smart, 1 = smart, 2 = super smart
        result = 1
        past_sheep = None
        past_wolves = None
        future_sheep = None
        future_wolves = None
        if state.direction == "right":
            past_sheep = state.left_sheep
            past_wolves = state.left_wolves
            future_sheep = state.right_sheep
            future_wolves = state.right_sheep
        if state.direction == "left":
            future_sheep = state.left_sheep
            future_wolves = state.left_wolves
            past_sheep = state.right_sheep
            past_wolves = state.right_wolves

        if self.past_quantities_are_logical(past_sheep, past_wolves) != True:
            return 0

        if self.sheep_are_safe(state.left_sheep, state.left_wolves) != True:
            return 0

        if self.sheep_are_safe(state.right_sheep, state.right_wolves) != True:
            return 0

        result = self.is_progress(state, option)
        return result

    def is_progress(self, state, option):
        result = 1
        step_sum = option[0] + option[1]
        if state.direction == "left":
            left_side_sum = state.left_sheep + state.left_wolves
            if (left_side_sum == 1) and (step_sum == 1):
                return 0
            if (left_side_sum > 1) and step_sum == 1:
                return 2
        if state.direction == "right":
            if step_sum == 2:
                return 2
            right_side_sum = state.right_sheep + state.right_wolves
            if right_side_sum == 1 and (step_sum == 1):
                return 0
        return 1


    def past_quantities_are_logical(self, past_sheep, past_wolves):
        return past_sheep >= 0 and past_wolves >= 0

    def sheep_are_safe(self, sheep, wolves):
        if sheep > 0:
            return sheep >= wolves
        else:
            return True

    def solution_is_found(self, state):
        return (state.left_sheep == 0) and (state.left_wolves == 0)