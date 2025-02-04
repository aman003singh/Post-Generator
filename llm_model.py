from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os


load_dotenv()
llm = ChatGroq(groq_api_key= os.getenv("GROQ_API_KEY"), model_name="llama-3.2-3b-preview")


if __name__ == "__main__":
    response = llm.invoke("What are the main ingredients in samosa ")
    print(response.content)


# llm models
# llama-3.2-3b-preview
# llama-3.3-70b-versatile
# llama-3.2-90b-vision-preview
# distil-whisper-large-v3-en