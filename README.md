[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)


# NeoCortex: Multi-Modality Foundation Model for Humanoid Robots

NeoCortex is a cutting-edge, multi-modality foundation model engineered for humanoid robots. With the capability to process an array of modalities including images, text, videos, depth, heatmaps, LIDAR, 3D scenes, point clouds, and more, NeoCortex represents the zenith of robotic perception and cognition.

## Appreciation
* All the creators in Agora, [Join Agora](https://discord.gg/qUtxnK2NMf) the community of AI engineers changing the world with their creations.
* LucidRains for inspiring me to devote myself to open source AI


## Installation
To integrate NeoCortex into your development environment:

```bash
pip install neox
```

## Usage
```python
import torch
from neox.model import NeoCortex

#usage
img = torch.randn(1, 3, 256, 256)
caption_tokens = torch.randint(0, 4)

model = NeoCortex()
output = model(img, caption_tokens)
```

## Model Architecture
Building on the paradigms established by models like NeVA, NeoCortex expands its horizons to embrace a multi-faceted input system:

- **Images**: Processed through a frozen variant of the Hugging Face CLIP model, producing image embeddings.
- **Text**: Integrated seamlessly with an NVIDIA-trained GPT variant.
- **LIDAR**: Point clouds processed through PointNet or KPConv, extracting essential spatial features. These features, once captured, are projected to text embedding dimensions.
- **Videos**: Processed using 3D-CNNs to capture temporal information, then integrated with the main architecture.
- **Heatmaps, 3D Scenes, and Depth**: These are funneled through specialized modules tailored for each modality before being integrated.

Training comprises three stages:
1. **Pretraining**: Specific modules (like PointNet for LIDAR) are pretrained, with the main model frozen.
2. **Inter-modality Training**: The embeddings from different modalities are concatenated, projected, and trained to ensure inter-modality coherence.
3. **Finetuning**: Utilizing synthetic data generated with advanced GPT versions to ensure the model understands the intricate relationship between various modalities.

## Specifications

- **Architecture Type**: Multi-Modality Transformer
- **Sub-Architectures**: GPT, CLIP, PointNet, 3D-CNN
- **Model versions**: 10B, 30B, 50B

## Input & Output

- **Input Formats**: 
  - Images: RGB
  - Text: Tokens
  - LIDAR: Point Clouds
  - Videos: Frames
  - And more...
- **Output Format**: Text or Action Tokens

## Integration and Compatibility

- **Supported Hardware Platforms**: Hopper, Ampere/Turing, specialized robotic chipsets
- **Supported Operating Systems**: Linux, RoboOS

## Training & Fine-tuning Data

- **Image Dataset**: [Link to Dataset]
- **LIDAR Dataset**: [Link to Dataset]
- **Textual Data**: Synthetically produced by GPT versions
- **Licenses**: Various, mainly MIT and CC-BY-NC 4.0

## Inference

- **Engine**: Triton and specialized robotic inference engines
- **Test Hardware**: Humanoid robotic platforms

## References and More

- [Visual Instruction Tuning paper](#)
- [Blog](#)
- [Codebase](https://github.com/kyegomez/NeoCortex)
- [Demo](#)

## Licensing
This project is licensed under the MIT License.

For more details, contributions, and support, please refer to the [official repository](https://github.com/kyegomez/NeoCortex).


# Todo

[] - 