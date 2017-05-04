import requests
import pygame

BASE_URL = "https://www.random.org/"


def get_nums_array(size, minimum, maximum, col=1, base=10):
    if size > 10000:
        size = size % 10000
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
    hsl_codes = get_nums_array(total_pixels, 0, 359)
    x_pos = 0
    y_pos = 0
    for i in range(0, total_pixels):
        # color = pygame.Color.hsla((code, 100, 100, 100))
        # Draw on each pixel
        color = ''
        if i >= len(hsl_codes):
            color = hsl_codes[i - len(hsl_codes)]
        else:
            color = hsl_codes[i]
        if x_pos >= x_size:
            y_pos += 1
            x_pos = 0
        pixArr[x_pos][y_pos] = pygame.Color.hsla((color, 100, 100, 100))





if __name__ == '__main__':
    pygame.init()
    size = width, height = 128, 128
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)
    generate_random_image(width, height, screen)
