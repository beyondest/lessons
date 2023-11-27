import torch

                #save tensor to data.pth
tensor_data = torch.rand(100, 10)  
tensor_labels = torch.randint(2, (100,))  

torch.save({'data': tensor_data, 'labels': tensor_labels}, 'torch_data.pth')

loaded_torch_data = torch.load('torch_data.pth')
loaded_tensor_data = loaded_torch_data['data']
loaded_tensor_labels = loaded_torch_data['labels']
print(loaded_tensor_data.shape)
print(loaded_tensor_labels.shape)


