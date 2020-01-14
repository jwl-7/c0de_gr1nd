from test_framework import generic_test


def flip_color(x, y, image):
    color = image[x][y]
    image[x][y] ^= 1
    moves = (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)
    for nxt_x, nxt_y in moves:
        if (
            0 <= nxt_x < len(image) and
            0 <= nxt_y < len(image[nxt_x]) and
            image[nxt_x][nxt_y] == color
        ):
            flip_color(nxt_x, nxt_y, image)


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
