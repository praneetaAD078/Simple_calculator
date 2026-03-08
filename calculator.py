#TASK 2 - Simple calculator
!pip install gradio
import gradio as gr

# Function to perform arithmetic operations
def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == "Addition":
            return num1 + num2
        elif operation == "Subtraction":
            return num1 - num2
        elif operation == "Multiplication":
            return num1 * num2
        elif operation == "Division":
            if num2 == 0:
                return "Error: Division by zero!"
            return num1 / num2
    except ValueError:
        return "Invalid input! Please enter numbers."

# Gradio Interface
iface = gr.Interface(
    fn=calculate,
    inputs=[
        gr.Textbox(label="Enter First Number"),
        gr.Textbox(label="Enter Second Number"),
        gr.Radio(["Addition", "Subtraction", "Multiplication", "Division"], label="Choose Operation")
    ],
    outputs=gr.Textbox(label="Result"),
    title="Simple Web Calculator",
    description="Enter two numbers and select an operation to perform basic arithmetic calculations."
)

# Launch the web app
iface.launch()
