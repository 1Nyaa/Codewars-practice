
# The rgb function is incomplete.
# Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# Valid decimal values for RGB are 0 - 255.
# Any values that fall out of that range must be rounded to the closest valid value.

def rgb(r, g, b):
    rgb = []
    for i in [r, g, b]:
        if i > 255:
            rgb.append(255)
        elif i < 0:
            rgb.append(0)
        else:
            rgb.append(i)
    return ('%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])).upper()
