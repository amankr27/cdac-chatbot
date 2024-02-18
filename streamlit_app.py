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

    # Initialize session_state variables
    if "user_inputs" not in st.session_state:
        st.session_state.user_inputs = []
    if "bot_responses" not in st.session_state:
        st.session_state.bot_responses = []

    # Sidebar for user input
    user_input = st.text_input("Enter your query:")
    corrected_user_input = spell(user_input)

    # Button to trigger the chatbot response
    if st.button("Ask"):
        bot_response = chatbot(corrected_user_input)
        st.success(f"Bot: {bot_response}")

        # Add the current conversation to the list of previous conversations within the session
        st.session_state.user_inputs.append(corrected_user_input)
        st.session_state.bot_responses.append(bot_response)

    # Display previous conversations within the session
    st.write("**Previous Conversations in this Session:**")
    for i, (user_input, bot_response) in enumerate(zip(st.session_state.user_inputs, st.session_state.bot_responses), 1):
        st.write(f"{i}. **You:** {user_input}")
        st.write(f"   **Bot:** {bot_response}")

if __name__ == "__main__":
    main()
