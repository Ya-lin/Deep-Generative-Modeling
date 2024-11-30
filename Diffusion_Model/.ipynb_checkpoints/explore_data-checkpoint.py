

from dataset import download_oxford102, get_oxford102
from testing import display

train, *_ = download_oxford102(val=False, test=False)
print('\n', len(train))

x, y = train[0]
print('\nimage size: ', x.shape)
print('\nlabel: ', y)

train_loader, *_ = get_oxford102(64, val=False, test=False)
print('\nlength of train data loader: ', len(train_loader))

x, y = next(iter(train_loader))
print('\n', x.shape)
print('\n', y.shape)

display(x)

