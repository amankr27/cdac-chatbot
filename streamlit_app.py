import streamlit as st
from autocorrect import Speller
from chat import chatbot  # Assuming you have a chatbot function in chat.py
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
# Initialize the Speller from autocorrect
spell = Speller()

def main():
    st.title("CDAC-Assistant")

    # Sidebar for user input
    user_input = st.text_input("Enter your message:")
    corrected_user_input = spell(user_input)

    # Button to trigger the chatbot response
    if st.button("Ask"):
        bot_response = chatbot(corrected_user_input)
        st.success(f"Bot's Response: {bot_response}")

    # Sidebar for search functionality
    #search_query = st.text_input("Enter your search query:")
    #corrected_query = spell(search_query)

    # Button to trigger the search correction
    #if st.button("Search"):
        #st.success(f"Corrected Query: {corrected_query}")

if __name__ == "__main__":
    main()
