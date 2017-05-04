import requests
import pygame

BASE_URL = "https://www.random.org/"


def get_nums_array(size, minimum, maximum, col=1, base=10):
    if size > 10000:
        size = 10000
    full_url = BASE_URL + 'integers/?num=' + str(size) + '&min=' + \
        str(minimum) + '&max=' + str(maximum) + '&col=' + str(col) + \
        '&base=' + str(base) + '&format=plain&rnd=new'
    print(full_url)
    request = requests.get(full_url)
    numbers_list = []
    for num in request.content:
        numbers_list.append(num)
    print(numbers_list)
    return numbers_list


def generate_random_image(x_size, y_size, canvas):
    total_pixels = x_size * y_size
    pixArr = pygame.PixelArray(canvas)
    color_nums = get_nums_array(total_pixels, 0, 255)
    color_iter = 0
    x_pos = 0
    y_pos = 0
    for i in range(0, total_pixels):
        # color = pygame.Color.hsla((code, 100, 100, 100))
        # Draw on each pixel
        color = ''
        color_range_check = (i - (len(color_nums) * color_iter)) * 3
        print(color_range_check)
        if color_range_check + 2 >= len(color_nums):
            get_nums_array(total_pixels, 0, 255)
            color_iter += 1
        color = [color_nums[(i - (len(color_nums) * color_iter)) * 3 + j] for j in range(0, 3)]
        if x_pos >= x_size:
            y_pos += 1
            x_pos = 0
        pixArr[x_pos][y_pos] = (color[0], color[1], color[2])


if __name__ == '__main__':
    pygame.init()
    size = width, height = 128, 128
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)
    generate_random_image(width, height, screen)
