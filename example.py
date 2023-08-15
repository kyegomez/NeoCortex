import torch
from neox.model import NeoCortex

#usage
img = torch.randn(1, 3, 256, 256)
caption_tokens = torch.randint(0, 4)

model = NeoCortex()
output = model(img, caption_tokens)