# main.py
from src.ui.gradio_app import TenderSearchUI

if __name__ == "__main__":
    app = TenderSearchUI()
    app.launch()