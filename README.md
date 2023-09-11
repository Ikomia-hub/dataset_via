<div align="center">
  <img src="https://raw.githubusercontent.com/Ikomia-hub/dataset_via/main/icons/vgg_logo.png" alt="Algorithm icon">
  <h1 align="center">dataset_via</h1>
</div>
<br />
<p align="center">
    <a href="https://github.com/Ikomia-hub/dataset_via">
        <img alt="Stars" src="https://img.shields.io/github/stars/Ikomia-hub/dataset_via">
    </a>
    <a href="https://app.ikomia.ai/hub/">
        <img alt="Website" src="https://img.shields.io/website/http/app.ikomia.ai/en.svg?down_color=red&down_message=offline&up_message=online">
    </a>
    <a href="https://github.com/Ikomia-hub/dataset_via/blob/main/LICENSE.md">
        <img alt="GitHub" src="https://img.shields.io/github/license/Ikomia-hub/dataset_via.svg?color=blue">
    </a>    
    <br>
    <a href="https://discord.com/invite/82Tnw9UGGc">
        <img alt="Discord community" src="https://img.shields.io/badge/Discord-white?style=social&logo=discord">
    </a> 
</p>

Load VGG Image Annotator (VIA) dataset. This plugin converts a given dataset in VIA format to Ikomia format. Then, any training algorithms from the Ikomia marketplace can be connected to this converter.

![VIA](https://www.robots.ox.ac.uk/~vgg/software/via/images/via_logo.png)

## :rocket: Use with Ikomia API

#### 1. Install Ikomia API

We strongly recommend using a virtual environment. If you're not sure where to start, we offer a tutorial [here](https://www.ikomia.ai/blog/a-step-by-step-guide-to-creating-virtual-environments-in-python).

```sh
pip install ikomia
```

#### 2. Create your workflow

[Change the sample image URL to fit algorithm purpose]

```python
from ikomia.dataprocess.workflow import Workflow
from ikomia.utils import ik

# Initialize the workflow
wf = Workflow()

# Add the dataset loader to load your custom data and annotations
dataset = wf.add_task(name="dataset_via")

# Set parameters
dataset.set_parameters({
    "via_json_file":"Path/to/via_json_file.json"
})                     

# Add the YoloV8 training algorithm
yolo = wf.add_task(name="train_yolo_v8")

# Launch your training on your data
wf.run()
```

## :sunny: Use with Ikomia Studio

Ikomia Studio offers a friendly UI with the same features as the API.

- If you haven't started using Ikomia Studio yet, download and install it from [this page](https://www.ikomia.ai/studio).

- For additional guidance on getting started with Ikomia Studio, check out [this blog post](https://www.ikomia.ai/blog/how-to-get-started-with-ikomia-studio).

## :pencil: Set algorithm parameters

- **via_json_via** (str): Annotation file (.json).

```python
from ikomia.dataprocess.workflow import Workflow
from ikomia.utils import ik

# Initialize the workflow
wf = Workflow()

# Add the dataset loader to load your custom data and annotations
dataset = wf.add_task(name="dataset_via")

# Set parameters
dataset.set_parameters({
    "via_json_file":"Path/to/via_json_file.json"
})
```