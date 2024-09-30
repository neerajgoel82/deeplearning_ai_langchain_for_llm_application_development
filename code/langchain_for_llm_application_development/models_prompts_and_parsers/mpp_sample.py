import openai
import datetime
from langchain_openai import ChatOpenAI

class MPPSample:
    """
    A class to represent a sample model prompt and parser (MPP) using OpenAI's language models.

    Attributes
    ----------
    llm_model : str
        The language model to be used.

    Methods
    -------
    choose_llm_model():
        Chooses the appropriate language model based on the current date.
    __init__():
        Initializes the MPPSample class and sets the language model.
    run():
        Prints the currently set language model.
    """
    llm_model = "gpt-3.5-turbo-0301"

    def choose_llm_model(self):
        """
        Chooses the appropriate language model based on the current date.
        If the current date is after June 12, 2024, sets the model to "gpt-3.5-turbo".
        Otherwise, sets the model to "gpt-3.5-turbo-0301".
        """
        # Get the current date
        current_date = datetime.datetime.now().date()

        # Define the date after which the model should be set to "gpt-3.5-turbo"
        target_date = datetime.date(2024, 6, 12)

        # Set the model variable based on the current date
        if current_date > target_date:
            self.llm_model = "gpt-3.5-turbo"
        else:
            self.llm_model = "gpt-3.5-turbo-0301"

    def __init__(self):
        """
        Initializes the MPPSample class.
        Calls the choose_llm_model method to set the language model.
        Initializes the ChatOpenAI instance with the chosen model and a temperature of 0.0.
        """
        self.choose_llm_model()

        # To control the randomness and creativity of the generated
        # text by an LLM, use temperature = 0.0
        self.chat = ChatOpenAI(temperature=0.0, model=self.llm_model)

    def run(self):
        """
        Prints the currently set language model.
        """
        print(self.llm_model)