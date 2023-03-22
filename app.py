import gradio as gr  # type: ignore
from ultralytics import YOLO  # type: ignore
from internetarchive import download  # type: ignore

download("pcb_weights", files=["pcb.pt"], verbose=True)  # type: ignore

download(
    "pcb_examples",
    files=["test_1.jpg", "test_2.jpg", "test_3.jpg", "test_4.jpg", "test_5.jpg", "test_6.jpg"],  # type: ignore
    verbose=True,
)


model = YOLO(model="./pcb_weights/pcb.pt", task="detect")


def predict_image(src):
    predictions = model.predict(src)
    return predictions[0].plot()


with gr.Blocks() as demo:
    gr.Markdown(
        '### <h3 align="center">Defect detection for Printed Circuit Boards</h3>'
    )
    gr.Markdown(
        "This AI was trained to detect and recognize six types of defects on printed circuit boards: missing hole, mouse bite, open circuit, short, spur, and spurious copper."
    )
    with gr.Row():
        image_input = gr.Image()
        image_output = gr.Image()
        image_input.upload(
            predict_image,
            inputs=[image_input],
            outputs=[image_output],
        )
    gr.Examples(
        [
            ["./pcb_examples/test_1.jpg"],
            ["./pcb_examples/test_2.jpg"],
            ["./pcb_examples/test_3.jpg"],
            ["./pcb_examples/test_4.jpg"],
            ["./pcb_examples/test_5.jpg"],
            ["./pcb_examples/test_6.jpg"],
        ],
        [image_input],
        [image_output],
        predict_image,
        cache_examples=True,
    )
    gr.Markdown("[@itsyoboieltr](https://github.com/itsyoboieltr)")

demo.launch()
