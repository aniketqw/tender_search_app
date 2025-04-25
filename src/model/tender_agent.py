import json
import re
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
            max_results=5
        )
        
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        self.agent = self._setup_agent()
    
    def _extract_relevant_terms(self, query: str) -> list:
        """
        Extract relevant keywords from the query based on the keywords mapping.
        """
        relevant_terms = []
        query_lower = query.lower()
        
        for category, keywords in TENDER_DATASET["keywords_mapping"].items():
            for keyword in keywords:
                if keyword.lower() in query_lower:
                    if keyword not in relevant_terms:
                        relevant_terms.append(keyword)
        
        return relevant_terms
    
    def _get_relevant_websites(self, query: str) -> list:
        """
        Get relevant websites based on the query keywords.
        """
        query_lower = query.lower()
        relevant_sites = []
        matched_specializations = set()
        
        # First identify all matching specializations
        for category, keywords in TENDER_DATASET["keywords_mapping"].items():
            for keyword in keywords:
                if keyword.lower() in query_lower:
                    matched_specializations.add(category)
                    # Also add the exact keyword
                    matched_specializations.add(keyword.lower())
        
        # Then find websites that match these specializations
        for website in TENDER_DATASET["websites"]:
            for spec in website["specializations"]:
                if spec.lower() in matched_specializations or any(kw.lower() in spec.lower() for kw in matched_specializations):
                    if website not in relevant_sites:
                        relevant_sites.append(website)
        
        # If no specific matches, return all websites
        if not relevant_sites:
            return TENDER_DATASET["websites"]
        
        return relevant_sites
    
    def _search_engine_query(self, base_query: str) -> str:
        """
        Perform a search using the search tool with a well-structured query string.
        """
        # Create a search-friendly query string
        search_query = f"Indian tender {base_query} deadline"
        
        # Directly call the search tool with the string query
        try:
            results = self.search_tool.run(search_query)
            return results
        except Exception as e:
            return f"Search error: {str(e)}"
    
    def _setup_agent(self):
        """
        Set up a simple agent that uses a structured approach
        """
        # Define the search tool
        search_tool = Tool(
            name="Search",
            func=self._search_engine_query,
            description="Searches for Indian tender information using a query string"
        )
        
        # Initialize the agent
        return initialize_agent(
            tools=[search_tool],
            llm=self.llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True
        )
    
    def _parse_json_from_text(self, text: str) -> list:
        """
        Extract JSON from text that might contain additional content.
        """
        # Look for JSON array pattern
        json_pattern = r'\[\s*{.*}\s*\]'
        match = re.search(json_pattern, text, re.DOTALL)
        
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass
        
        # Try to find any JSON-like structures
        try:
            # Look for array with opening and closing brackets
            start_idx = text.find('[')
            end_idx = text.rfind(']')
            
            if start_idx != -1 and end_idx != -1:
                json_str = text[start_idx:end_idx+1]
                return json.loads(json_str)
        except:
            pass
        
        # If all else fails, return empty list
        return []
    
    def search_tenders(self, query: str) -> str:
        """
        Two-stage process:
        1. Research and collect raw data
        2. Format and present the data
        """
        # STAGE 1: Research and collect raw data
        relevant_terms = self._extract_relevant_terms(query)
        relevant_websites = self._get_relevant_websites(query)
        
        # Format website suggestions for research
        website_suggestions = ", ".join([site['name'] for site in relevant_websites[:5]])
        
        # Create an enhanced search query
        search_terms = query + " " + " ".join(relevant_terms[:3])
        
        # Research prompt to gather raw information
        research_prompt = f"""
        I need to find information about Indian tenders related to: {search_terms}
        
        Focus on websites like {website_suggestions}.
        
        Perform a search and collect all relevant tender information, including:
        - Tender titles
        - Deadlines
        - Brief descriptions
        - Source websites
        
        Return the raw information you find without any formatting or structure yet.
        """
        
        # Get raw research results
        raw_research = self.agent.run(research_prompt)
        
        # STAGE 2: Format and structure the data
        formatting_prompt = f"""
        Based on this raw research data about Indian tenders:
        
        {raw_research}
        
        Please organize the information into a clean JSON array where each tender has these fields:
        - title: The tender title
        - deadline: The submission deadline in Month Day, Year format
        - description: Brief description of the tender
        - website: The source website
        
        Only include tenders that are relevant to "{query}" and have clear deadlines that haven't passed yet.
        
        Format as a valid JSON array of objects.
        """
        
        # Get formatted tender data
        formatted_response = self.llm.invoke(formatting_prompt).content
        
        # Extract JSON data
        try:
            tender_data = self._parse_json_from_text(formatted_response)
        except Exception as e:
            # Fall back to using the raw research if JSON parsing fails
            return f"Found the following tender information:\n\n{raw_research}\n\nNote: The data couldn't be structured into a standard format. Please review the information above."
        
        # Format the response for the user
        if not tender_data or len(tender_data) == 0:
            return f"No relevant tenders found for the query: {query}\n\nSuggested websites to check manually:\n" + "\n".join([f"- {site['name']}: {site['base_url']}" for site in relevant_websites[:5]])
        
        response = "# Relevant Tenders Found\n\n"
        for tender in tender_data:
            response += f"## {tender.get('title', 'Unnamed Tender')}\n"
            response += f"**Deadline**: {tender.get('deadline', 'Not specified')}\n"
            response += f"**Description**: {tender.get('description', 'No description available')}\n"
            response += f"**Source**: {tender.get('website', 'Unknown source')}\n\n"
        
        # Add website recommendations
        response += "\n## Recommended Tender Websites\n"
        for site in relevant_websites[:5]:
            response += f"- [{site['name']}]({site['base_url']})\n"
        
        return response