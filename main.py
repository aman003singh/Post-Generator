import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

def main():
    st.title("Social Media Post Generator")
    col1 , col2, col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        selected_tag = st.selectbox("Topic" , options =fs.get_tags())

    with col2:
        selected_length = st.selectbox("Length", options = ["Short", "Medium", "Long"])

    with col3:
        selected_language = st.selectbox("Language", options = ["English", "Hinglish"])
        

   
    
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language,selected_tag)
        st.write("Hey, See this!")
        st.write(post)

    if st.button("Celebrate"):
        st.balloons()
    

    

if __name__ == "__main__":
    main()


# page styling
st.markdown("""
   <style>
            
      .stButton>button {
            color:  #d34b72;
            padding: 10px 24px;
            font-size: 16px;
            border-radius: 5px;
            width: 225px;
            box-sizing: border-box;
            border: 1px solid #d34b72;
        }

        .stButton>button:hover {
            background-color: #DE3163;
            color: white;
            border: none;
        }

    </style>
""", unsafe_allow_html=True)



# run the command streamlit run main.py