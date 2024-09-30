import openai
import datetime

class MPPSample:
    llm_model = "gpt-3.5-turbo-0301"

    def choose_llm_model(self):
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
        self.choose_llm_model()

    def run(self):
        print(self.llm_model)
