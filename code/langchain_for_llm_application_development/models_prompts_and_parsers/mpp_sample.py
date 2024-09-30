import openai
import datetime
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


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

    def test_prompt_template(self):
        template_string = """Translate the text \
                        that is delimited by triple backticks \
                        into a style that is {style}. \
                        text: ```{text}```
                        """


        prompt_template = ChatPromptTemplate.from_template(template_string)
        print(prompt_template.messages[0].prompt)
        print(prompt_template.messages[0].prompt.input_variables)

        customer_style = """American English \
        in a calm and respectful tone
        """

        customer_email = """
        Arrr, I be fuming that me blender lid \
        flew off and splattered me kitchen walls \
        with smoothie! And to make matters worse, \
        the warranty don't cover the cost of \
        cleaning up me kitchen. I need yer help \
        right now, matey!
        """

        customer_messages = prompt_template.format_messages(
            style=customer_style,
            text=customer_email)

        print(type(customer_messages))
        print(type(customer_messages[0]))
        print(customer_messages[0])

        # Call the LLM to translate to the style of the customer message
        customer_response = self.chat(customer_messages)
        print(customer_response.content)

        service_reply = """Hey there customer, \
        the warranty does not cover \
        cleaning expenses for your kitchen \
        because it's your fault that \
        you misused your blender \
        by forgetting to put the lid on before \
        starting the blender. \
        Tough luck! See ya!
        """

        service_style_pirate = """\
        a polite tone \
        that speaks in English Pirate\
        """

        service_messages = prompt_template.format_messages(
            style=service_style_pirate,
            text=service_reply)

        print(service_messages[0].content)

        service_response = self.chat(service_messages)
        print(service_response.content)

    def get_completion(prompt, model=llm_model):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]

    def test_openai_chat_api(self):
        customer_email = """
        Arrr, I be fuming that me blender lid \
        flew off and splattered me kitchen walls \
        with smoothie! And to make matters worse,\
        the warranty don't cover the cost of \
        cleaning up me kitchen. I need yer help \
        right now, matey!
        """

        style = """American English \
        in a calm and respectful tone
        """

        prompt = f"""Translate the text \
        that is delimited by triple backticks 
        into a style that is {style}.
        text: ```{customer_email}```
        """

        print(prompt)

        response = self.get_completion(prompt)
        print(response)


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
        #self.test_prompt_template()
        self.test_openai_chat_api()
