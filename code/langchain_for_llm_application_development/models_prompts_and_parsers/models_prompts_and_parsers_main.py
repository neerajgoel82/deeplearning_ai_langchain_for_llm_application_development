
from models_prompts_and_parsers.mpp_sample import MPPSample
import os
import openai
from dotenv import load_dotenv, find_dotenv

def main():
    _ = load_dotenv(find_dotenv())  # read local .env file
    openai.api_key = os.environ['OPENAI_API_KEY']
    openai.api_base = os.environ['OPENAI_API_BASE']
    openai.api_version = os.environ['OPENAI_API_VERSION']
    openai.api_type = os.environ['OPENAI_API_TYPE']
    openai.deployment_name = os.environ['OPENAI_DEPLOYMENT_NAME_GPT35']

    mpp_sample = MPPSample()
    mpp_sample.run()

if __name__ == "__main__":
    main()