import gradio as gr
from ultralytics import YOLO
from PIL import Image

# Load the trained YOLOv8 model
model = YOLO(r"C:\Users\yahya\Downloads\best.pt")

# Define the prediction function
def predict(image):
    results = model(image)  # Run YOLOv8 model on the uploaded image
    results_img = results[0].plot()  # Get image with bounding boxes
    return Image.fromarray(results_img)

# Create Gradio interface
interface = gr.Interface(
    fn=predict, 
    inputs=gr.Image(type="pil"), 
    outputs=gr.Image(type="pil"),
    title="Helmet Detection with YOLOv8",
    description="Upload an image to detect helmets."
)

# Launch Gradio app
interface.launch(share=True)
