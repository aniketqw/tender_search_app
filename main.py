# main.py
from src.ui.gradio_app import TenderSearchUI

def main():
    app = TenderSearchUI()
    interface = app.create_ui()
    interface.launch(share=True)

if __name__ == "__main__":
    main()
