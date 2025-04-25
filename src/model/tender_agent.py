from langchain_groq import ChatGroq
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.tools import TavilySearchResults
from langchain.memory import ConversationBufferMemory
from ..data.tender_dataset import TENDER_DATASET

class TenderAgent:
    def __init__(self, groq_api_key: str, tavily_api_key: str):
        self.llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name="meta-llama/llama-4-scout-17b-16e-instruct",
            temperature=0.1
        )
        
        self.search_tool = TavilySearchResults(
            tavily_api_key=tavily_api_key,
            max_results=5
        )
        
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        self.agent = self._setup_agent()
    
    def _get_relevant_websites(self, keyword: str) -> list:
        relevant_sites = []
        for category, keywords in TENDER_DATASET["keywords_mapping"].items():
            if keyword.lower() in keywords:
                for website in TENDER_DATASET["websites"]:
                    if category in website["specializations"]:
                        relevant_sites.append(website)
        return relevant_sites
    
    def _setup_agent(self):
        tools = [
            Tool(
                name="Tender Search",
                func=self.search_tool.run,
                description="Searches for tender information"
            )
        ]
        
        return initialize_agent(
            tools=tools,
            llm=self.llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True
        )
    
    def search_tenders(self, query: str) -> str:
        prompt = f"""
        Search for tender information related to: {query}
        
        Please provide:
        - Available tender opportunities
        - Key dates and deadlines
        - Brief descriptions
        """
        
        return self.agent.run(prompt)
