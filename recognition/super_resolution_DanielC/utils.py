import torchvision.transforms as transforms
"""
IO paths to data and parameters to be tuned.

By default:
    - num_epochs = 40
    - learning rate = 0.001
    - batch_size = 30
    - out_channels = 256
    - downsample_size = (60,64)

With default configuration and gpu 3070TI, training should take about 23 
minutes.
"""

# IO-paths
#replace with path to train directory
train_dir = "F:/COMP3710/data/AD_NC/train" 

#replace with path to test directory
test_dir = "F:/COMP3710/data/AD_NC/test" 

#replace with where model is saved
model_path = "F:/COMP3710/model/model.pt" 



# Hyper-parameters
num_epochs = 40
learning_rate = 0.001
batch_size = 30

out_channels = 256

min_loss = 99999999

# Downsample-parameters 
downsample_size = (60,64)

def resize_tensor(tensor):
    """
    Resize the tensor to dresired down sampling size.

    Param:
        Tensor to be resized

    Returns:
        Resized version of the tensor
    """
    transform = transforms.Compose([transforms.Resize(downsample_size)])

    return transform(tensor)
