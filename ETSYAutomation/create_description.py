from ETSYAutomation.image_processing import ImageProcess

from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class CreateDescription:
    def __init__(self) -> None:
        self.model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
        image_process = ImageProcess()
        self.image_description = image_process.image_process()
        self.prompt = self.template()

    def template(self) -> str:
        prompt_tempate = """
        This is a small description of a product that is supposed to be listed on Etsy platform. I need you to create a longer description of the following. DON'T create any facts out of thin air, just use the information provided in the description.

        You should return a json format in the following way:

        {{
            "description": "description",
            "product_name": "product name",
            "product_size": "product size or dimensions, if given",
            "product_material": "product material, if given",
            "product_color": "product color, if given",
            "product_use": "product use, if given"
        }}


        Just return the json object and nothing else.

        Refer the following description provided for the product:
        description: {description}
        """

        prompt = PromptTemplate(
            template=prompt_tempate, input_variables=["description"]
        )

        return prompt

    def create_desctipion(self):
        llm_chain = self.prompt | self.model

        # llm_chain.input_schema.schema()

        for s in llm_chain.stream({"description": self.image_description}):
            print(s.content, end="", flush=True)
