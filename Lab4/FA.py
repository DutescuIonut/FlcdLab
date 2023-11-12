class FiniteAutomata:
    def __init__(self, filePath):
        self.file_path = filePath
        self.states = []
        self.alphabet = []
        self.initial_state = ""
        self.final_states = []
        self.transitions = []
        self.parse_file()

    def separate_by_delimiter(self, line, delimiter):
        return line.strip().split(delimiter)



    def parse_file(self):
        with open(self.file_path, 'r') as file:
            # Parse the 1st line: the finite set of states
            self.states = self.separate_by_delimiter(next(file), ' ')

            # Parse the 2nd line: the alphabet
            self.alphabet = self.separate_by_delimiter(next(file), ' ')

            # Parse the 3rd line: the transitions
            self.transitions = self.separate_by_delimiter(next(file), ' ')



    def print_menu(self):
        print("----------------------------------------")
        print("Please choose what you want to output:")
        print("Type <0> to exit")
        print("Type <1> to output the set of states")
        print("Type <2> to output the alphabet")
        print("Type <3> to output the transitions")
        print("Type <4> to output the initial state")
        print("Type <5> to output the set of final states")
        print("Type <6> to test if a sequence is accepted by the FA")
        print("----------------------------------------")

    def print_states(self):
        print(" ".join(self.states))

    def print_alphabet(self):
        print(" ".join(self.alphabet))

    def print_transitions(self):
        print(" ".join(self.transitions))


    def print_initial_state(self):
        print(self.initial_state)

    def print_final_states(self):
        print(" ".join(self.final_states))

    def is_final_state(self, state):
        return state in self.final_states

    def can_obtain_sequence(self, sequence_so_far, final_sequence, current_state):
        if len(sequence_so_far) == len(final_sequence):
            if sequence_so_far == final_sequence and self.is_final_state(current_state):
                return True
            return False

        answer = False
        for transition in self.transitions:
            if transition[0] == current_state and transition[1] == sequence_so_far[-1]:
                answer = (answer or self.can_obtain_sequence(sequence_so_far + transition[3], final_sequence,
                                                             transition[2]))

        return answer

    def check_sequence(self):
        sequence = input("Enter your sequence to be checked:\n")
        if self.can_obtain_sequence("", sequence, self.initial_state):
            print("Your sequence is accepted")
        else:
            print("Your sequence is NOT accepted")

    def run(self):
        while True:
            self.print_menu()
            try:
                option = int(input())
                if option == 0:
                    return
                elif option == 1:
                    self.print_states()
                elif option == 2:
                    self.print_alphabet()
                elif option == 3:
                    self.print_transitions()
                elif option == 4:
                    self.print_initial_state()
                elif option == 5:
                    self.print_final_states()
                elif option == 6:
                    self.check_sequence()
                else:
                    print("Invalid option! Try again!")
            except ValueError:
                print("Invalid input. Try again!")

#fa = FiniteAutomata("FAIdentifier.in")
fa = FiniteAutomata("FAIntegerConstants.in")
fa.run()
