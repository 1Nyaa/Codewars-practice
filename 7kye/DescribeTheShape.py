
# You will be given the number of angles of a shape with equal sides and angles,
# and you need to return the number of its sides, and the measure of the interior angles.

def describe_the_shape(ang):
    if ang < 3:
        return "this will be a line segment or a dot"
    else:
        return f"This shape has {ang} sides and each angle measures {int((ang - 2) * 180/ ang)}"
