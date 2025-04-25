import gradio as gr
from src.model.tender_agent import TenderAgent
from src.data.tender_dataset import TENDER_DATASET
from src.config import GROQ_API_KEY, TAVILY_API_KEY

class TenderSearchUI:
    def __init__(self):
        self.agent = TenderAgent(GROQ_API_KEY, TAVILY_API_KEY)
        # Extract categories from the keywords mapping
        self.categories = list(TENDER_DATASET["keywords_mapping"].keys())
    
    def search_tenders(self, query: str, categories: list = None) -> str:
        """
        Search for tenders with selected categories included in the query
        """
        search_query = query
        
        # Append categories if selected
        if categories and len(categories) > 0:
            for category in categories:
                # Add representative keywords from the category
                if category in TENDER_DATASET["keywords_mapping"]:
                    keywords = TENDER_DATASET["keywords_mapping"][category]
                    if keywords and len(keywords) > 0:
                        search_query += f" {keywords[0]}"
                        
        return self.agent.search_tenders(search_query)
    
    def create_ui(self):
        with gr.Blocks(title="Indian Tender Search Application") as interface:
            gr.Markdown("# 🔍 Indian Tender Search Application")
            gr.Markdown("Search for tenders across multiple Indian government and international websites.")
            
            with gr.Row():
                query_input = gr.Textbox(
                    label="Search Query",
                    placeholder="Enter your tender search query...",
                    lines=2
                )
            
            with gr.Row():
                categories_input = gr.CheckboxGroup(
                    choices=self.categories,
                    label="Include Categories",
                    info="Select categories to include in your search"
                )
            
            # Websites display
            with gr.Accordion("Available Tender Websites", open=False):
                website_list = "\n".join([f"- {site['name']}: {site['base_url']}" for site in TENDER_DATASET["websites"]])
                gr.Markdown(website_list)
            
            search_button = gr.Button("🔍 Search Tenders", variant="primary")
            
            output_text = gr.Markdown(
                label="Search Results",
                value="Results will appear here after search"
            )
            
            search_button.click(
                fn=self.search_tenders,
                inputs=[query_input, categories_input],
                outputs=output_text
            )
            
            # Example queries
            gr.Examples(
                examples=[
                    ["Carbon emissions assessment project in Delhi", ["sustainability"]],
                    ["Skill gap analysis for IT sector", ["capacity_building"]],
                    ["Monitoring and evaluation of education programs", ["monitoring_evaluation"]],
                    ["Healthcare services consultancy", ["health"]],
                    ["Project management unit for infrastructure", ["project_management"]]
                ],
                inputs=[query_input, categories_input]
            )
            
        return interface

    def launch(self):
        interface = self.create_ui()
        interface.launch(share=True)  # Create a public link
