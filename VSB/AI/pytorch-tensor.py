import torch
import numpy as np

#creates Empty tensor
x = torch.empty(3)
print(x)

#creates random value
x1 = torch.rand(2, 2)
print(x1)

#creates zeroes with tensor
x2 = torch.zeros(2, 3)
print(x2)

#creates ones with tensor
x3 = torch.ones(2, 3)
print(x3)

#ceates tensor with our list value
x4 = torch.tensor([2.5, 0.1, 4.0])
print(x4)


#prints our data type of tensor
x = torch.tensor([1, 2, 3], dtype=torch.float32)
print(x)
print(x.dtype)

#prints our data type of tensor
x = torch.ones(3, dtype=torch.int64)
print(x)
print(x.dtype)

#show our size and values
x = torch.zeros(2, 3)

print(x.shape)
print(x.size())
print(x.numel())

#math function performing
r = torch.tensor([[1,2],[4,5]])
m = torch.tensor([[10,20],[40,50]])

z = torch.add(r,m)
print(z)

#In-Place Operations
x = torch.tensor([1, 2, 3])
y = torch.tensor([10, 20, 30])

x.add_(y)
print(x)

#index Slicing
x = torch.tensor([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(x[1, :])

#Getting a Normal Python Number with `.item()`
x = torch.tensor([42], dtype=torch.int64)
value = x.item()

print(value)
print(type(value))

#Reshaping a Tensor with `.view()`
x = torch.arange(16)
print(x)

y = x.view(4,4)
print(y)

y = x.view(2, -1)
print(y)
print(y.shape)

a = torch.tensor([1.0, 2.0, 3.0])
b = a.numpy()

print(b)
print(type(b))

a = np.array([1.0, 2.0, 3.0], dtype=np.float32)
b = torch.tensor(a)

print(b)


#When a CPU tensor and a NumPy array share memory, changing one can change what you see in the other.
a = torch.tensor([1.0, 2.0, 3.0])
b = a.numpy()

a.add_(1)

print(a)  # tensor([2., 3., 4.])
print(b)  # [2. 3. 4.]

print(torch.cuda.is_available())

