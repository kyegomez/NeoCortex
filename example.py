import torch
from neox.model import NeoCortex

#usage
img = torch.randn(1, 3, 256, 256)
caption = torch.randint(0, 20000, (1, 1024))

model = NeoCortex()
output = model(img, caption)
print(output.shape) # (1, 1024, 20000)


