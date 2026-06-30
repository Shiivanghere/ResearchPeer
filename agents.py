from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from rag_pipeline import process_pdf, answer_question
from dotenv import load_dotenv

load_dotenv()


llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)


# Search Agent


def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )


# Reader Agent




def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research writer. Write clear, structured and insightful reports."
    ),
    (
        "human",
        """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""
    ),
])

writer_chain = writer_prompt | llm | StrOutputParser()


critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a sharp and constructive research critic. Be honest and specific."
    ),
    (
        "human",
        """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""
    ),
])

critic_chain = critic_prompt | llm | StrOutputParser()


class RAGAgent:
    """
    Specialized agent responsible for answering
    questions from user-uploaded PDF documents.
    """

    def ingest_document(self, uploaded_file):
        """
        Creates the vector database from the uploaded PDF.
        """
        return process_pdf(uploaded_file)

    def invoke(self, question):
        """
        Answers questions using Retrieval-Augmented Generation.
        """
        return answer_question(question)


def build_rag_agent():
    return RAGAgent()