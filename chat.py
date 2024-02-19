import csv
from call import QASystem
import pandas as pd

def chatbot(input_text):
    # First try to get a response from the QASystem
    # Initialize the QASystem
    qa = QASystem('test2.csv')

    try:
        qa_response = qa.get_response(input_text)
        print("Try")
    except Exception as e:
        qa_response = "I can't answer this question."
        print("Except:", str(e))

        # Save the question and the AI's response to the CSV file
        data = {'Questions': [input_text], 'Answers': ['']}
        df = pd.DataFrame(data)
        df.to_csv('test.csv', mode='a', header=False, index=False, quoting=csv.QUOTE_NONNUMERIC)

    return qa_response
