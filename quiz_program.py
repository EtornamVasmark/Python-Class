#import random
import random
from questions import quiz_questions

# Git Quiz modified 
# Define the quiz questions as a list of dictionaries
# quiz_questions = [
#     {
#         'question': 'What is the output of 3 + 4?',
#         'options': ['7', '8', '12', 'None of the above'],
#         'answer': '7'
#     },
#     {
#         'question': 'Python is an interpreted language. (True/False)',
#         'options': ['True', 'False'],
#         'answer': 'True'
#     },
#     {
#         'question': 'Which data type is mutable in Python?',
#         'options': ['int', 'str', 'list', 'tuple'],
#         'answer': 'list'
#     },
#     {
#         'question': 'What is the maximum length of a Python identifier?',
#         'options': ['32','16','128','None of the above'],
#         'answer': 'None of the above'
#     },
#     {
#         'question': 'How is a code block indicated in Python?',
#         'options': ['Bracket','Indentation','Key','None of above'],
#         'answer': 'Indentation'
#     }
# ]

# Shuffle the quiz questions to randomize the order
quiz = random.sample(quiz_questions,4)

#function
def Quiz(question):
    #Score 
    # Initialize the user's score and total possible score
    score = 0
    total_possible_score = len(quiz)
    
    
    for i, question in enumerate(quiz):
        #Print the questions
        print("Question " + str(i + 1) + ": " + question['question'])
        
        #shuffle options
        random.shuffle(question['options'])
        
        # Print answer options
        for j, option in enumerate(question['options'], start=1):
            print(str(j) + ". " + option)
    
        
        #take user answer as an integer
        user_answer = int(input("Option number: "))
    
        #Equate correct answer to the answers in the question key
        correct_answer = question['answer']
        correct_answers_position = question['options'].index(correct_answer) + 1
    
        #compare answer to user
        if  user_answer == correct_answers_position:
            print("Your answer is correct!")
            score += 1  # Increment the score for each correct answer
        else:
            print("Your answer is incorrect. The correct answer is " + correct_answer)# tell user the correct answer
    
        print()  # Add a line break for better readability
    
    return score, total_possible_score

#Call Function
user_score, total_possible_score = Quiz(quiz) 

# Calculate the user's score as a percentage
percentage_score = (user_score / total_possible_score) * 100

# Display the final score as a percentage without using an f-string
print("Your score:", user_score, "/", total_possible_score, "(", "{:.2f}".format(percentage_score), "%)")


