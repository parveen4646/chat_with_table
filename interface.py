import gradio as gr
import os
from app import table_parser
iface = gr.Interface(
    fn=table_parser,
    title='chat with tables',
    inputs=[gr.File(type="filepath", label="Upload PDF File"),gr.Textbox(type="text", label="Enter Query")],
    outputs=[
        gr.Textbox(label="DataFrame", type="text"),
        gr.JSON(label="JSON"),
       
    ],live=True)

# Launch the Gradio interface
iface.launch()
