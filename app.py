import gradio as gr
from ultralytics import RTDETR
from huggingface_hub import hf_hub_download, snapshot_download

model_path = hf_hub_download(
    repo_id="itsyoboieltr/pcb",
    repo_type="model",
    filename="model.pt",
)

examples_path = snapshot_download(
    repo_id="itsyoboieltr/pcb",
    repo_type="dataset",
    allow_patterns=["examples/*"],
    local_dir="./pcb_dataset",
)

model = RTDETR(model=model_path)


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
        image_input = gr.Image(width=486, height=238)
        image_output = gr.Image(width=486, height=238)
        image_input.upload(
            predict_image,
            inputs=[image_input],
            outputs=[image_output],
        )
        image_input.clear(lambda: None, outputs=[image_output], api_name=False)
    gr.Examples(
        "./pcb_dataset/examples",
        [image_input],
        [image_output],
        predict_image,
        cache_examples=True,
    )
    gr.Markdown("[@itsyoboieltr](https://github.com/itsyoboieltr)")

demo.launch()
