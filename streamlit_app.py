import streamlit as st
from chat import chatbot  # chatbot function in chat.py
from textblob import TextBlob  # Import TextBlob
import nltk

st.set_page_config(
    page_title="CDAC-Assistant",
    page_icon="🤖",  # Bot icon
    layout="wide",
)

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

def main():
    st.title("CDAC-Assistant")

    # Initialize session_state variables if they don't exist
    if "user_inputs" not in st.session_state:
        st.session_state.user_inputs = []
    if "bot_responses" not in st.session_state:
        st.session_state.bot_responses = []

    # Sidebar for user input
    user_input = st.text_input("Enter your query:")

    # Button to trigger the chatbot response
    if st.button("Ask"):
        sentiment_score = analyze_sentiment(user_input)
        bot_response = chatbot(user_input)

        st.success(f"🤖: {bot_response}")
        #st.write(f"**Sentiment Score:** {sentiment_score:.2f}")

        # Add the current conversation to the list of previous conversations within the session
        st.session_state.user_inputs.append(user_input)
        st.session_state.bot_responses.append(bot_response)

    # Display previous conversations within the session
    st.write("**Previous Conversations in this Session:**")
    if "user_inputs" in st.session_state and "bot_responses" in st.session_state:
        for user_input, bot_response in zip(st.session_state.user_inputs, st.session_state.bot_responses):
            st.write(f"**👤:** {user_input}")
            st.write(f"**🤖:** {bot_response}")

if __name__ == "__main__":
    main()
