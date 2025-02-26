import torch 
z = torch.zeros(5,3)
print("z : ", z)
print("z.dtype : ",z.dtype)

ones = torch.ones(2,3)
print("ones : ", ones)

twos = torch.ones(2,3) * 2 # every element is multiplied by 2

print("twos: ", twos)

threes = ones + twos
print("threes: ", threes)
print("threes shape : ", threes.shape)

r1 = torch.rand(2,3)
r2 = torch.rand(2,3)
r3 = r1 + r2
print("r3 : ", r3)