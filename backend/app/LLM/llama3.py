import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN", "")


class LLM:
    def __init__(self):
        self.llm = HuggingFaceEndpoint(
            endpoint_url="meta-llama/Meta-Llama-3-8B-Instruct", streaming=True
        )
        self.system = """
                        You are a healthcare chatbot. Answer the patient's question in a doctor's perspective.
                        Limit your response to 100 words.
                        """
        self.prompt = PromptTemplate(
            input_variables=["system", "text"],
            template="""
                        <|begin_of_text|>
                        <|start_header_id|>system<|end_header_id|>
                        {system}
                        <|eot_id|>
                        <|start_header_id|>user<|end_header_id|>
                        {text}
                        <|eot_id|>
                        <|start_header_id|>assistant<|end_header_id|>
                    """,
        )

    def ask(self, text: str):
        chain = self.prompt | self.llm
        response = chain.stream({"system": self.system, "text": text})
        return response
