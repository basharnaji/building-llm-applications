from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv() #A
api_key = os.getenv("API_KEY") #B

def get_llm(): #C
    return ChatAnthropic(api_key=api_key, 
                 model_name="claude-haiku-4-5-20251001")
    
#A Load the environment variables from the .env file
#B Get the OpenAI API key from the environment variables
#C Instantiate and return the ChatOpenAI model
