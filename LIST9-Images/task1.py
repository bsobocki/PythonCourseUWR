import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

count = 0

def do_smth(src, change): 
    global count
    img = mpimg.imread(src)
    src = src.split('.png')[0]
    change_img(img, change, src+'_plot_'+str(count))
    count+=1
    return img

def change_img(img, change, plot_name):
    fig = plt.figure(figsize=(20,10))  

    before = fig.add_subplot(1, 2, 1)
    before.set_title("Before")
    show = plt.imshow(img)
    plt.colorbar(ticks=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], orientation='horizontal')

    img = change(img)

    after = fig.add_subplot(1, 2, 2)
    after.set_title("After")
    plt.colorbar(ticks=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], orientation='horizontal')

    plt.imshow(img)
    plt.savefig(plot_name+'.png')
    return img


def delete_gray(img):
    epsilon = 0.2
    for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                pixel = img[i][j]
                if abs(pixel[0] - pixel[1]) <= epsilon and abs(pixel[1] - pixel[2]) <= epsilon:
                    if j>=10 :
                        pixel[0]  = img[i][j-10][0]
                        pixel[1] = img[i][j-10][1]
                        pixel[2] = img[i][j-10][2]
    return img

def more_color(img):
    add_more = 0.01
    add_less = 0.005
    for row in img:
        for pixel in row:
            index = 0
            max_p = pixel[0]
            for i in range(1,3):
                if pixel[i] > max_p:
                    max_p = pixel[i]
                    index = i
            pixel[i] += add_more


def gray_scale(img):
    for row in img:
        for pixel in row:
            a = ( pixel[0] + pixel[1] + pixel[2] ) / 3
            pixel[0] = a
            pixel[1] = a
            pixel[2] = a
    return img


def gray_to_white(img):
    epsilon = 0.001
    for row in img:
        for pixel in row:
            if abs(pixel[0] - pixel[1]) <= epsilon and abs(pixel[1] - pixel[2]) <= epsilon:
                pixel[0]  = 1.0
                pixel[1] = 1.0
                pixel[2] = 1.0
    return img

def gray_plus_random(img):
    epsilon = 0.001
    for row in img:
        for pixel in row:
            if abs(pixel[0] - pixel[1]) <= epsilon and abs(pixel[1] - pixel[2]) <= epsilon:
                pixel[0]  += np.random.randint(100)/100
                pixel[1] +=  np.random.randint(65)/100
                pixel[2] +=  np.random.randint(30)/100
    return img


#do_smth('Ideas1.png', delete_gray)
#do_smth('hq.png', gray_scale)
#do_smth('hq.png', gray_to_white)
#change_img(do_smth('Ideas1.png', gray_scale), gray_plus_random, 'random_color_plot.png')
change_img(mpimg.imread('Ideas1.png'), more_color, 'aaa.png')