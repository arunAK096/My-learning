import torch

# Make two 2-by-2 tensors.
x = torch.tensor([[1.0, 2.0],
                  [3.0, 4.0]])

y = torch.ones(2, 2)

# Add matching values.
z = x + y
print("Sum:")
print(z)

# Select the first row.
print("First row:")
print(z[0, :])

# Show the shape.
print("Shape:", z.shape)

# Change the shape to one row with four values.
flat = z.reshape(1, 4)
print("New shape:", flat.shape)

# Choose a device and move the tensor there.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
z_device = z.to(device)
print("Device:", z_device.device)

# Convert to a NumPy array on the CPU.
z_numpy = z_device.cpu().numpy()
print(z_numpy)