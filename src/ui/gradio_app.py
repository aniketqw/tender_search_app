import gradio as gr
from src.model.tender_agent import TenderAgent
from src.config import GROQ_API_KEY, TAVILY_API_KEY
from src.data.tender_dataset import TENDER_DATASET

class TenderSearchUI:
    def __init__(self):
        self.agent = TenderAgent(GROQ_API_KEY, TAVILY_API_KEY)
    
    def search_tenders(self, query: str, category: str) -> str:
        search_query = f"{query} {category}" if category else query
        results = self.agent.search_tenders(search_query)
        
        if results["status"] == "error":
            return f"Error: {results['message']}"
        
        if not results["data"]:
            return "No tenders found matching your criteria."
        
        # Format results as HTML
        html_output = "<div style='padding: 20px;'>"
        html_output += f"<h3>Found {results['count']} relevant tenders</h3>"
        
        for tender in results["data"]:
            html_output += f"""
            <div style='margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px;'>
                <h4 style='color: #2c5282;'>{tender['title']}</h4>
                <p><strong>Description:</strong> {tender['description']}</p>
                <p><strong>Deadline:</strong> {tender['deadline']}</p>
                <p><strong>Source:</strong> <a href='{tender['source_url']}' target='_blank'>{tender['source']}</a></p>
                <p><strong>Category:</strong> {tender['category']}</p>
                {f"<p><strong>Estimated Value:</strong> {tender['estimated_value']}</p>" if tender.get('estimated_value') else ''}
            </div>
            """
        
        html_output += "</div>"
        return html_output
    
    def create_ui(self):
        with gr.Blocks(title="Indian Tender Search Application") as interface:
            gr.Markdown("# Indian Tender Search Application")
            
            with gr.Row():
                query_input = gr.Textbox(
                    label="Search Query",
                    placeholder="Enter your tender search query..."
                )
                category_input = gr.Dropdown(
                    choices=list(TENDER_DATASET["keywords_mapping"].keys()),
                    label="Category",
                    value="construction"
                )
            
            search_button = gr.Button("Search Tenders")
            output_html = gr.HTML(label="Search Results")
            
            search_button.click(
                fn=self.search_tenders,
                inputs=[query_input, category_input],
                outputs=output_html
            )
            
            # Add example queries
            gr.Examples(
                examples=[
                    ["hospital construction project", "construction"],
                    ["medical equipment supply", "healthcare"],
                    ["software development services", "IT_services"],
                    ["solar power plant installation", "energy"],
                    ["school infrastructure development", "education"]
                ],
                inputs=[query_input, category_input]
            )
        
        return interface

# Test queries for users
TEST_QUERIES = [
    "Construction of new hospital building in Mumbai",
    "Supply of medical equipment for government hospitals",
    "IT infrastructure upgrade for public sector banks",
    "Solar power plant installation in Gujarat",
    "School building renovation project",
    "Water treatment plant construction",
    "Agricultural equipment procurement",
    "Healthcare facility management system",
    "Road construction and maintenance",
    "Digital transformation consulting services"
]
