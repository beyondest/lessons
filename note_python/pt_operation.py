import torch
from torch.utils.data import DataLoader,TensorDataset
from torchvision import datasets,transforms
from sklearn.model_selection import train_test_split
                #save tensor to data.pth
tensor_data = torch.rand(100, 10)  
tensor_labels = torch.randint(2, (100,))  

torch.save({'data': tensor_data, 'labels': tensor_labels}, 'torch_data.pth')

loaded_torch_data = torch.load('torch_data.pth')
loaded_tensor_data = loaded_torch_data['data']
loaded_tensor_labels = loaded_torch_data['labels']
print(loaded_tensor_data.shape)
print(loaded_tensor_labels.shape)


                #How to make datasets and make dataloader
              
train_root_dir = 'petimages/train' 

'''use this to apply data augumentation'''     
custom_transform  = transforms.Compose([
    transforms.ToTensor(),
    transforms.ConvertImageDtype(torch.float32),
    transforms.Normalize([0.5,0.5,0.5],[0.229,0.224,0.225]),
    transforms.Resize((224,224)),
    transforms.CenterCrop(224),
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(0.5),
    transforms.RandomVerticalFlip(0.5),
    transforms.ColorJitter(brightness=0,
                           contrast=0,
                           saturation=0,
                           hue=0),
    transforms.RandomPerspective(),
    transforms.RandomErasing(),
    transforms.Lambda(),
    ...
])  


'''method 1: when images are in right folder sorted by class, use this to generate torch_dataset'''
'''this will automatically make lables by alphabetically'''
'''train_root_dir/0_Dog,1_Cat,...'''
custom_dataset = datasets.ImageFolder(train_root_dir,custom_transform)

'''method 2: when ori_X,ori_y is loaded from some file ,use this to generate torch_dataset'''
X = torch.Tensor()
y = torch.Tensor()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=10)
X_train,X_test,y_train,y_test=map(lambda data: torch.from_numpy(data).to(dtype=torch.float32),[X_train,X_test,y_train,y_test])
y_train,y_test=map(lambda data: data.reshape(-1,1),[y_train,y_test])
dataset=TensorDataset(X_train,y_train)
    
custom_dataset = TensorDataset(X_train,y_train)
         


  
