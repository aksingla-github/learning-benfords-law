import cv2
import os
import matplotlib.pyplot as plt

blue_dict, green_dict, red_dict = {}, {}, {}


def get_user_input(message):
    inp = input(message)
    return inp


def get_image(path):
    does_file_exist = os.path.isfile(path)
    if does_file_exist:
        img = cv2.imread(path)
        print(type(img))
        return img
    raise FileExistsError("File doesn't exists! Try again.")


def get_dimensions(img):
    print(img.shape)
    height, width, channels = img.shape
    return height, width, channels


def add_in_dict(num, color_dict):
    if num in color_dict:
        color_dict[num] += 1
    else:
        color_dict[num] = 1
    return color_dict


def get_BGR_values(img, height, width):
    global blue_dict, green_dict, red_dict
    for y in range(height):
        for x in range(width):
            blue, green, red = img[y, x]
            b, g, r = str(blue), str(green), str(red)
            b,g,r = int(b[0]), int(g[0]), int(r[0])
            add_in_dict(b, blue_dict)
            add_in_dict(g, green_dict)
            add_in_dict(r, red_dict)



if __name__ == "__main__":
    img = get_image(get_user_input("Enter image path for verification! "))
    height, width, channels = get_dimensions(img)
    '''
    Generally, number of channels are 3, but channels can vary. Check image data if its a specialized 
    image in different color spaces such as grayscale(has only 1 channel) or multispectral 
    '''
    get_BGR_values(img, height, width)
    plt.scatter(red_dict.keys(), red_dict.values(), marker='o', linestyle='-')
    # plt.plot(blue_dict.keys(), blue_dict.values(), marker='o', linestyle='-')
    # plt.plot(green_dict.keys(), green_dict.values(), marker='o', linestyle='-')
    plt.show()
    # get a dict and store occurrancies of red's and so on
    # Plot the graph using R,G, B values
    # check #age of graph matching benford graph
    # get the threshold %age
