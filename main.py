import torch

x = torch.tensor([[1, 1, 0], [1, 2, 3]])
y = torch.tensor([[0, 1, 2], [3, 4, 5]])
print(torch.mm(x, y))