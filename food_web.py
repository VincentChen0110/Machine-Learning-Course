import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_option('deprecation.showfileUploaderEncoding',False)
st.title("Food Image to Recipe Generator")
st.text("Provide URL of Food Image For Classification")

#@st.cache(allow_output_mutation=True)

path = st.text_input('Enter Image URL to Classify.. ','https://prettysimplesweet.com/wp-content/uploads/2019/07/Chocolate-Donuts.jpg')
if path is not None:
    content = requests.get(path).content
    st.write("Predicted Recipe Ingredients :")
    with st.spinner('Generating....'):
        st.write("")
    st.write("")
    image = Image.open(BytesIO(content))
    st.image(image,caption= 'Input Food Image', use_column_width = True)
