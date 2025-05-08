import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#Load Resourse
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
model = joblib.load ('nb_model.pkl')

#page configuration
st.set_page_config(page_title="News Categorization", page_icon='', layout='centered')
                   
st.title ("NEWS CATEGORIZATION!")
st.markdown("Enter a news headline or article below.")
st.markdown ('---')
input_text =st.text_area("Enter News Text", height=200)

#Text preprocessing function
def preprocess_text(text):
    #lowercasing
    text = text.lower()
    #remove special character and puunctuation
    text =re.sub(r'[^a-zA-Z\s]','',text)
    #tokenization
    words = word_tokenize(text)
    #Remove stopwords and leamatize
    words =(lemmatizer.lemmatize(word) for word in words if word not in stop_words)
    #join back into a string
    return " ".join(words)

#prdiction function
def predict_category(text):
    processed_text = preprocess_text(text)
    prediction = model.predict([processed_text])
    return prediction[0]

#prediction Display
if st.button("Predict Category"):
    if input_text.strip():
        category = predict_category(input_text)
        st.success(f'**Predicted Category:** {category}')
    else:
        st.warning("Please enter some text first")


#footer
st.markdown("---")
st.markdown('<p style="text-align:center:">Built by Rakshya Rajbanshi</p', unsafe_allow_html=True)


                   