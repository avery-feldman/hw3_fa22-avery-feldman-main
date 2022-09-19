# Your name: Avery Feldman
# Your student id: 83844944
# Your email: averylf@umich.edu
# List who you have worked with on this homework:


# import the random module for use in this program
import random 

# Create the class Fortune_Teller
class Fortune_Teller:
    # create the constructor (__init__) method
    # it takes as input: a list of possible answers
    def __init__(self, fortunes_list):
    # it sets this object's fortunes_list (instance variable) to the passed list of possible answers
        self.fortunes_list = fortunes_list
    # it sets this object's questions_list (instance variable) to an empty list
        self.questions_list = []
    # it sets this object's fortunes_history_list (instance variable) to an empty list
        self.fortunes_history_list = []

    # create the __str__ method
    # It should return a string with all the fortunes
    # in fortunes_list separated by commas
    # For example : "Yes, No, Not clear"
    def __str__(self):
        answer_str = ", ".join(self.fortunes_list)
        return answer_str


    # create the get_fortune method
    def get_fortune(self):   
    # it randomly picks an index from 0 to the number of items in the fortunes_list minus one
        index = random.randint(0, len(self.fortunes_list)-1)
    # it adds that index to the end of the fortunes_history_list
        self.fortunes_history_list.append(index)
    # it returns the answer at the picked index
        return self.fortunes_list[index]

    # create the question_check method that takes a question
    def question_check(self, question):
    # it checks if the question is in the questions_list and if so returns
    # "I've already answered that question”
        if question in self.questions_list:
            return "I've already answered that question"
    # Otherwise it adds the question to the questions_list and
        else:
            self.questions_list.append(question)
    # returns the fortune from get_fortune
            return self.get_fortune()

    # create the print_questions_history method
    def print_questions_history(self):
    # prints "[answer index] question - answer" for each of the indices in the fortunes_history_list
    # from the first to the last with each on a separate line.  If there are no items in the
    # fortunes_history_list it prints "None yet"
        if len(self.fortunes_history_list) == 0:
            print("None yet")
        else:
            for index in range(len(self.questions_list)):
                print("[" + str(self.fortunes_history_list[index]) + "] " + self.questions_list[index] + " - " + self.fortunes_list[self.fortunes_history_list[index]])
    # it does not return anything!

    # EXTRA POINTS
    # create the most_frequent method
    # it takes as input:
    #   a number, n. Ex: 200
    def most_common(self, number):
        # it generates a random response n times by calling get_fortune
        questions_count = [[self.fortunes_list[0], 0], [self.fortunes_list[1], 0], [self.fortunes_list[2], 0], [self.fortunes_list[3], 0], [self.fortunes_list[4], 0]]
        self.fortunes_history_list = []
        for x in range(number):
            self.get_fortune() 
        
        for answer in self.fortunes_history_list:
                questions_count[answer][1] += 1

        for lst in questions_count:
            print(lst[0] + ": " + str(lst[1]))
        sorted_lst = sorted(questions_count, key = lambda x : x[1], reverse = True)
        print("The most frequent answer after " + str(number) + " was " + sorted_lst[0][0])


    
    
    # It prints the counts for each answer and
    # prints the most frequently occurring answer (Do not use a dictionary in this solution):
    #   Yes: 36
    #   No: 36
    #   Ask again: 48
    #   Maybe: 38
    #   Not clear: 47
    #   The most frequent answer after 200 was Not clear

def main():

    # You are welcome to replace the answer_list with your desired answers
    fortunes_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Fortune_Teller(fortunes_list)

    # get the first question or quit

    # loop while question is not "quit"
    question = input("Ask a question or type quit: ")
    while question != "quit":
        # get an answer from question_check
        # print question - answer
        print(question + " - " + bot.question_check(question))
        # get the next question or quit 
        question = input("Ask question or type quit: ")


def test():

    fortunes_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Fortune Teller:")
    bot2 = Fortune_Teller(fortunes_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_questions_history()
    print()

    print("Asking the Question: Will I pass this semester?")
    print(bot2.question_check("Will I pass this semester?"))
    print()

    print("Asking the Question: Should I study today?")
    print(bot2.question_check("Should I study today?"))
    print()

    print("Asking the Question: Should I study today? (again)")
    print(bot2.question_check("Should I study today?"))
    print()

    print("Asking the Question: Is SI 206 the best class ever?")
    print(bot2.question_check("Is SI 206 the best class ever?"))
    print()

    print("Printing the history")
    bot2.print_questions_history()
    print()

    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
    print("Testing most_common method with 200 responses")
    bot2.most_common(200)


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() #Uncomment when you are ready to test your Fortune_Teller class