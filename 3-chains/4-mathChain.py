"""
Genera un code python para luego evaluarlo
"""

import os
from langchain import LLMChain, OpenAI, PromptTemplate

API = os.environ['OPENAI_API_KEY']
llm = OpenAI(openai_api_key=API)

# MathChain
from langchain import LLMMathChain
cadena_mate = LLMMathChain(llm=llm, verbose=True)
cadena_mate.run("Cuanto es 432*12-32+32?")
