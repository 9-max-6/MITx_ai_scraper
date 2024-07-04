#!/usr/bin/env python
from typing import List

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

# 1. Create prompt template
system_template = """
Extract information from HTML content:

The following information needs to be extracted from the provided HTML content (extracted from a website) and formatted as a JSON object:

 summary (100 words max): A concise description of the opportunity, allowing comprehension without additional details.
 main (500 words max): A detailed description of the opportunity, excluding procedures and conclusions.
 procedure (optional): Any relevant application procedures.
 size (optional): The opportunity's size in dollars (if available). make sure to include the currency and seperate the value and currency symbol with a space
 deadline (optional - YYYY-MM-DD format): The application deadline (if available).
 org: The organization offering the opportunity.
 country (optional): The country where the opportunity is posted (or "None" if not provided).
 date_published (optional - YYYY-MM-DD format): The date the opportunity was published (if available).
 relevant_links (optional): Any links you within the document. these must be represented as a JSON object with the link name as the key and the link as the value.
ref_number: The reference number of the opportunity.
Output format:

 Include only the extracted information in JSON format.
 Set any unavailable fields to "None".
 The keys of the json response must be exactly the same as the ones specified in the example JSON response.

Example JSON response: {json_response}

"""

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{html_content}')
])

# 2. Create model
model = ChatOpenAI(model="gpt-3.5-turbo")

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=5000)