import gradio as gr
from src.model.tender_agent import TenderAgent
from src.config import GROQ_API_KEY, TAVILY_API_KEY

class TenderSearchUI:
    def __init__(self):
        self.agent = TenderAgent(GROQ_API_KEY, TAVILY_API_KEY)
    
    def search_tenders(self, query: str, category: str) -> str:
        search_query = f"{query} {category}" if category else query
        return self.agent.search_tenders(search_query)
    
    def create_ui(self):
        with gr.Blocks(title="Indian Tender Search Application") as interface:
            gr.Markdown("# Indian Tender Search Application")
            
            with gr.Row():
                query_input = gr.Textbox(
                    label="Search Query",
                    placeholder="Enter your tender search query..."
                )
                category_input = gr.Dropdown(
                    choices=["construction", "IT services", "healthcare", "defense", "education", "agriculture", "oil and gas"],
                    label="Category",
                    value="construction"
                )
            
            search_button = gr.Button("Search Tenders")
            output_text = gr.Textbox(
                label="Search Results",
                lines=10
            )
            
            search_button.click(
                fn=self.search_tenders,
                inputs=[query_input, category_input],
                outputs=output_text
            )
            
            gr.Examples(
                examples=[
                    ["hospital construction", "construction"],
                    ["software development", "IT services"],
                    ["medical equipment", "healthcare"]
                ],
                inputs=[query_input, category_input]
            )
        
        return interface