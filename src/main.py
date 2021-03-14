import math
from time import time

from PIL import Image, ImageDraw

from mandelbrot import mandelbrot
from julia import julia


MAX_ITER = 80

# Image size (pixels)
WIDTH = 30000
HEIGHT = 15000

# Plot window
RE_START = -1.5
RE_END = -0.5
IM_START = -0.25
IM_END = 0.25

# c constant used to compute the Julia set
# c = complex(0.285, 0.01)
# Other interesting values:
# c = complex(-0.7269, 0.1889)
# c = complex(-0.8, 0.156)
# c = complex(-0.4, 0.6)

mappings = {
    'wikipedia': [
        (66, 30, 15),
        (25, 7, 26),
        (9, 1, 47),
        (4, 4, 73),
        (0, 7, 100),
        (12, 44, 138),
        (24, 82, 177),
        (57, 125, 209),
        (134, 181, 229),
        (211, 236, 248),
        (241, 233, 191),
        (248, 201, 95),
        (255, 170, 0),
        (204, 128, 0),
        (153, 87, 0),
        (106, 52, 3),
    ]}


def produce_image(mapping):
    start_time = time()

    im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        print(f'@ {x}th range of pixels [{time() - start_time}]')
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            # Compute the number of iterations
            m = mandelbrot(c)
            # The color depends on the number of iterations

            if m < MAX_ITER and m > 0:
                color = mapping[m % 16]
            else:
                color = (0, 0, 0)

            # Plot the point
            draw.point([x, y], color)

    im.save('output/plot.png', 'PNG')

    duration = time() - start_time
    print(f'Operation took {round(duration, 2)} seconds')


def main():
    produce_image(mappings['wikipedia'])


if __name__ == '__main__':
    main()
