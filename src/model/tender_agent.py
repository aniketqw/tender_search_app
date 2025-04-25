import json
from datetime import datetime
from langchain_groq import ChatGroq
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.tools import TavilySearchResults
from langchain.memory import ConversationBufferMemory
from src.data.tender_dataset import TENDER_DATASET

class TenderAgent:
    def __init__(self, groq_api_key: str, tavily_api_key: str):
        self.llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name="meta-llama/llama-4-scout-17b-16e-instruct",
            temperature=0.1
        )
        
        self.search_tool = TavilySearchResults(
            tavily_api_key=tavily_api_key,
            max_results=10
        )
        
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        self.agent = self._setup_agent()
    
    def _get_relevant_sources(self, query: str) -> list:
        relevant_sources = []
        for website in TENDER_DATASET["websites"]:
            for specialization in website["specializations"]:
                if specialization.lower() in query.lower():
                    relevant_sources.append(website)
                    break
        return relevant_sources
    
    def _setup_agent(self):
        tools = [
            Tool(
                name="Tender Search",
                func=self.search_tool.run,
                description="Searches for tender information across multiple sources"
            )
        ]
        
        return initialize_agent(
            tools=tools,
            llm=self.llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True
        )
    
    def search_tenders(self, query: str) -> dict:
        relevant_sources = self._get_relevant_sources(query)
        source_urls = [source["base_url"] for source in relevant_sources]
        
        prompt = f"""
        Search for Indian tender opportunities related to: {query}
        
        Search specifically in these sources: {', '.join(source_urls)}
        
        Format the results as a JSON array with the following structure for each tender:
        {{
            "title": "Tender title",
            "description": "Brief description",
            "deadline": "Deadline date in format 'Month DD, YYYY'",
            "source": "Source website name",
            "source_url": "Source URL",
            "estimated_value": "Estimated value if available",
            "category": "Tender category"
        }}
        
        Only include tenders that:
        1. Are from India or relevant to Indian organizations
        2. Have deadlines in the future
        3. Are directly related to the search query
        """
        
        try:
            raw_response = self.agent.run(prompt)
            results = json.loads(raw_response)
            return {
                "status": "success",
                "data": results,
                "count": len(results),
                "sources_searched": source_urls
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "data": [],
                "sources_searched": source_urls
            }
