
# ============================================================
# PyTorch Learning Project: Autograd and Gradients
# Based on my lesson: Autograd Gradients
#
# Topics:
# 1. Autograd and gradients
# 2. requires_grad=True
# 3. Computational graph
# 4. Forward pass and backward pass
# 5. grad_fn
# 6. backward()
# 7. Scalar and non-scalar outputs
# 8. Chain rule and vector-Jacobian product
# 9. Stopping gradient tracking
# 10. Gradient accumulation and zero_grad()
# 11. SGD optimizer and learning rate
# ============================================================

import torch


# ------------------------------------------------------------
# TOPIC 1: AUTOGRAD AND GRADIENTS
# ------------------------------------------------------------

print("\n========== 1. AUTOGRAD AND GRADIENTS ==========")

x = torch.tensor([2.0], requires_grad=True)

# Forward pass: calculate y = x * x
y = x * x

print("Input x:", x.item())
print("Output y:", y.item())

# Backward pass: calculate the gradient
y.backward()

print("Gradient of y with respect to x:", x.grad.item())

# Explanation:
# y = x^2
# Gradient = 2x
# When x = 2, gradient = 2 * 2 = 4


# ------------------------------------------------------------
# TOPIC 2: requires_grad=True
# ------------------------------------------------------------

print("\n========== 2. REQUIRES_GRAD ==========")

a = torch.randn(3, requires_grad=True)

print("Tensor a:", a)
print("Track gradients:", a.requires_grad)

# requires_grad=True tells PyTorch to record
# operations needed for gradient calculation.


# ------------------------------------------------------------
# TOPIC 3: COMPUTATIONAL GRAPH
# ------------------------------------------------------------

print("\n========== 3. COMPUTATIONAL GRAPH ==========")

x = torch.tensor([2.0], requires_grad=True)

y = x + 2
z = y * y

print("x:", x.item())
print("y = x + 2:", y.item())
print("z = y * y:", z.item())

# Computational graph:
# x -> add 2 -> y -> multiply y by itself -> z

print("Backward function of y:", y.grad_fn)
print("Backward function of z:", z.grad_fn)

# grad_fn describes the backward operation.
# It is not the gradient value itself.


# ------------------------------------------------------------
# TOPIC 4: FORWARD PASS AND BACKWARD PASS
# ------------------------------------------------------------

print("\n========== 4. FORWARD AND BACKWARD PASSES ==========")

x = torch.tensor([3.0], requires_grad=True)

# Forward pass: calculate the output
output = x * x

print("Forward pass output:", output.item())

# Backward pass: calculate the gradient
output.backward()

print("Backward pass gradient:", x.grad.item())

# Forward pass calculates the result.
# Backward pass calculates the gradient.


# ------------------------------------------------------------
# TOPIC 5: CHAIN RULE
# ------------------------------------------------------------

print("\n========== 5. CHAIN RULE ==========")

x = torch.tensor([2.0], requires_grad=True)

y = x + 2
z = y * y

z.backward()

print("x:", x.item())
print("y = x + 2:", y.item())
print("z = y * y:", z.item())
print("Gradient dz/dx:", x.grad.item())

# Mathematics:
# z = (x + 2)^2
# dz/dx = 2(x + 2)
# When x = 2, dz/dx = 8
#
# PyTorch uses the chain rule to calculate this
# through the computational graph.


# ------------------------------------------------------------
# TOPIC 6: SCALAR OUTPUT
# ------------------------------------------------------------

print("\n========== 6. SCALAR OUTPUT ==========")

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Square every element and add the results.
y = (x * x).sum()

print("Scalar output:", y.item())

# sum() produces one value, so backward()
# does not need an extra gradient argument.
y.backward()

print("Gradients:", x.grad)

# Expected gradient: [2, 4, 6]


# ------------------------------------------------------------
# TOPIC 7: NON-SCALAR OUTPUT
# ------------------------------------------------------------

print("\n========== 7. NON-SCALAR OUTPUT ==========")

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

y = x * x

print("Non-scalar output:", y)

# The output has three values.
# Supply one starting gradient for each value.
starting_gradient = torch.tensor([1.0, 1.0, 1.0])

y.backward(starting_gradient)

print("Gradients:", x.grad)

# Expected gradient: [2, 4, 6]
#
# A multi-value output normally needs a suitable
# gradient argument when calling backward().


# ------------------------------------------------------------
# TOPIC 8: VECTOR-JACOBIAN PRODUCT
# ------------------------------------------------------------

print("\n========== 8. VECTOR-JACOBIAN PRODUCT ==========")

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

y = x * x

# Different starting gradient values for the outputs.
starting_gradient = torch.tensor([1.0, 2.0, 3.0])

y.backward(starting_gradient)

print("Output y:", y)
print("Starting gradient:", starting_gradient)
print("Resulting gradient:", x.grad)

# PyTorch combines the supplied output gradients
# with the derivatives of the recorded operations.
# This is called a vector-Jacobian product.


# ------------------------------------------------------------
# TOPIC 9: STOP TRACKING WITH requires_grad_(False)
# ------------------------------------------------------------

print("\n========== 9. requires_grad_(False) ==========")

x = torch.tensor([1.0, 2.0], requires_grad=True)

print("Before:", x.requires_grad)

# Turn off gradient tracking for this leaf tensor.
x.requires_grad_(False)

print("After:", x.requires_grad)


# ------------------------------------------------------------
# TOPIC 10: DETACH
# ------------------------------------------------------------

print("\n========== 10. DETACH ==========")

x = torch.tensor([1.0, 2.0], requires_grad=True)

y = x.detach()

print("Original x tracks gradients:", x.requires_grad)
print("Detached y tracks gradients:", y.requires_grad)
print("Values in detached y:", y)

# detach() disconnects the new tensor from
# the original gradient history.
# The tensor data is shared in memory.


# ------------------------------------------------------------
# TOPIC 11: torch.no_grad()
# ------------------------------------------------------------

print("\n========== 11. TORCH.NO_GRAD ==========")

x = torch.tensor([1.0, 2.0], requires_grad=True)

with torch.no_grad():
    y = x + 2

print("Original x tracks gradients:", x.requires_grad)
print("Result y tracks gradients:", y.requires_grad)

# Operations inside no_grad() are not recorded
# for gradient calculation.


# ------------------------------------------------------------
# TOPIC 12: GRADIENT ACCUMULATION
# ------------------------------------------------------------

print("\n========== 12. GRADIENT ACCUMULATION ==========")

weights = torch.ones(4, requires_grad=True)

# First backward pass
output = (weights * 3).sum()
output.backward()

print("After first backward:", weights.grad)

# Create a fresh forward calculation.
# Gradients will be added to the old gradients.
output = (weights * 3).sum()
output.backward()

print("After second backward:", weights.grad)

# Clear the stored gradients.
weights.grad.zero_()

print("After zero_():", weights.grad)

# First backward:  [3, 3, 3, 3]
# Second backward: [6, 6, 6, 6]
# After zero_():   [0, 0, 0, 0]


# ------------------------------------------------------------
# TOPIC 13: SGD TRAINING STEP
# ------------------------------------------------------------

print("\n========== 13. SIMPLE SGD TRAINING STEP ==========")

# These are the values we want the optimizer to update.
weights = torch.tensor([1.0, 2.0], requires_grad=True)

# SGD means Stochastic Gradient Descent.
# Learning rate controls the size of each update.
optimizer = torch.optim.SGD([weights], lr=0.1)

print("Weights before training:", weights.detach())

# STEP 1: Clear old gradients
optimizer.zero_grad()

# STEP 2: Forward pass
output = (weights * 3).sum()
print("Output:", output.item())

# STEP 3: Calculate a simple demonstration loss
loss = output
print("Loss:", loss.item())

# STEP 4: Backward pass
loss.backward()
print("Gradients:", weights.grad)

# STEP 5: Update the weights
optimizer.step()

print("Weights after update:", weights.detach())

# Expected:
# Initial weights: [1.0, 2.0]
# Gradients:       [3.0, 3.0]
# Learning rate:   0.1
# Updated weights: [0.7, 1.7]
#
# Update = weight - (learning rate * gradient)


# ------------------------------------------------------------
# FINISHED
# ------------------------------------------------------------

print("\n========== ALL TOPICS COMPLETED ==========")
print("You have practised PyTorch Autograd and Gradients!")
