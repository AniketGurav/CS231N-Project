import numpy as np
import matplotlib.pyplot as plt

def disable_axis(ax):
	ax.set_xticklabels([])
	ax.set_yticklabels([])


def plot_img(img):
    ax = plt.subplot(1,1,1)
    plt.imshow(img)
    disable_axis(ax)


def sample_img(imgs):
    return imgs[np.random.choice(range(len(imgs)))]

def sample_img_many(imgs, num):
    return imgs[np.random.choice(range(len(imgs)), num, replace=False)]


def sample_and_show(imgs):
    sample = sample_img(imgs)
    plot_img(sample)
    return sample


def plot_images(imgs, size = (12, 6), title=None):
    """
    Input: 
        imgs: [image]
    """
    fig = plt.figure(figsize=size)
    for i, img in enumerate(imgs):
        ax = fig.add_subplot(1, len(imgs), i+1)
        if img.shape[-1] == 1: img = img.reshape(img.shape[:-1]) # in case of one channel
        plt.imshow(img)
        disable_axis(ax)
    if title: plt.suptitle(title)
    plt.show()

def plot_batch_images(imgs, size = (12, 6), title=None):
    """
    Input: 
        imgs: nd array of [batch_size, ...]
    """
    imgs = [imgs[i] for i in range(imgs.shape[0])]
    plot_images(imgs, size, title)


def sample_and_show_many(imgs, num):
    samples = sample_img_many(imgs, num)
    plot_images(samples)
    