# Helmet Detection V8 🚧👷‍♂️

![Helmet Detection](https://github.com/NightPrinceY/Helmet-V8/blob/main/OIG4.jpeg)

### Live Demo: [Helmet Detection on Hugging Face](https://huggingface.co/spaces/NightPrince/Helmet-Detect-model)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Gradio Demo](#gradio-demo)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

Helmet Detection V8 is a cutting-edge solution designed to enhance safety compliance through real-time helmet detection. Built using the powerful YOLOv8 architecture, this system efficiently detects the presence of helmets in various environments such as construction sites, factories, and even outdoor settings. With high accuracy and performance, it helps ensure that safety protocols are being followed, potentially preventing accidents and promoting a safer workspace.

This project also features a live demo on Hugging Face Spaces, where you can interact with the model through a web-based interface built with Gradio.

## Features 🌟

- **🚀 High Accuracy:** YOLOv8’s advanced architecture ensures precise and reliable helmet detection.
- **⚡ Real-Time Performance:** Efficient enough for live video streams, enabling surveillance and monitoring applications.
- **🎮 Gradio Interface:** User-friendly interface hosted on Hugging Face for easy interaction and demonstration.
- **🔄 Customizable:** Flexibility to modify and fine-tune the model for your own dataset or additional features.
- **📈 Scalable:** Suitable for scaling to larger datasets and environments.

## Dataset 📚

The dataset for this project is sourced from **Roboflow**, which contains annotated images specifically curated for helmet detection in diverse scenarios. These images include various angles, lighting conditions, and helmet types, making the model robust across different real-world conditions.

Access the dataset here:
- [Roboflow Helmet Detection Dataset](https://universe.roboflow.com/yahya-muhammad-alnwsany/helmet-xhkfl)

### Dataset Structure


The dataset is structured for easy integration with YOLOv8 and other object detection pipelines, ensuring smooth workflow from data preparation to model training.

## Installation 🛠️

To get started with this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/NightPrinceY/Helmet-V8.git
    cd Helmet-V8
    ```

2. **Install dependencies**:
    You can install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the dataset**:
    Make sure to download and place the dataset in the correct directory as per the structure described above.

4. **Install YOLOv8**:
    You can install YOLOv8 via the official repository:
    ```bash
    pip install ultralytics
    ```

## Usage 🚴‍♂️

Once you've installed the dependencies and downloaded the dataset, you can run the helmet detection model on both images and videos:

- **Detect helmets in an image**:
    ```bash
    python detect.py --source path/to/image.jpg
    ```

- **Detect helmets in a video**:
    ```bash
    python detect.py --source path/to/video.mp4
    ```

### Gradio Demo 🌐

You can try the live demo hosted on Hugging Face Spaces to interact with the model directly:

**[Helmet Detection Model - Gradio Demo](https://huggingface.co/spaces/NightPrince/Helmet-Detect-model)**

This demo allows you to upload images and get real-time helmet detection results using a simple web interface. No installation required!

## Visualizations 📊

Here are some sample detections made using the YOLOv8 helmet detection model:

![Helmet Detection Example](https://github.com/NightPrinceY/Helmet-V8/blob/main/detection_sample.jpg)

## Contributing 🤝

We welcome contributions! If you'd like to contribute to this project, feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add a feature"`)
4. Push the branch (`git push origin feature-branch`)
5. Open a pull request

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments 🙌

Special thanks to the **YOLO** and **Roboflow** communities for their incredible tools and resources, and to **Gradio** and **Hugging Face** for making AI model interaction seamless.

---
