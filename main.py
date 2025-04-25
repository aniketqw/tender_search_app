from src.ui.gradio_app import TenderSearchUI

def main():
    # Create and launch the Gradio interface
    app = TenderSearchUI()
    interface = app.create_ui()
    interface.launch(share=True)

if __name__ == "__main__":
    main()
