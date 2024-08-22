# Install necessary packages
# Uncomment and run these lines if you need to install the packages
# !pip install g4f
# !pip install gradio
# !pip install curl_cffi

# Import necessary libraries
from g4f.client import Client
import gradio as gr

# Initialize the G4F client
client = Client()

# Define the function for generating creative writing prompts
def generate_writing_prompt(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

# Define the custom CSS for the Gradio interface
custom_css = """
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}
.gradio-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
}
"""

# Define the Gradio user interface
interface = gr.Interface(
    fn=generate_writing_prompt,
    inputs=gr.Textbox(lines=3, placeholder="Enter a genre, tone, or starting idea...", label="Input Text"),
    outputs="text",
    title="✨ MuseMind: Your Creative Writing Companion ✨",
    description="Spark your imagination! Get fresh and unique ideas for stories, poems, and more.",
    theme="huggingface",
    examples=[
        ["Write a story about a hidden city finding a mysterious object."],
        ["Create a poem about how the seasons change."],
        ["Write a thrilling story set in a spooky, empty house."],
    ],
    css=custom_css  # Apply custom CSS
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()
