
# Write function potatoes with
#
# parameter p0 - initial percent of water
# parameter w0 - initial weight
# parameter p1 - final percent of water
# potatoes should return the final weight coming out of the oven w1 truncated as an int.

def potatoes(p0, w0, p1):
    return (w0 * (100 - p0)) // (100 - p1)
