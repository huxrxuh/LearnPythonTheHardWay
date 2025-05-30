#Closures

def constructor(color, size):
    """This function makes functions."""
    print(">>> constructor color:", color, "size:", size)

    def repeater():
        """This function uses color, size"""
        print("### repeater color:", color, "size:", size)

    print("<<< exit constructor");
    return repeater

#what's return are repeater functions
blue_xl = constructor("blue", "xl")
green_sm = constructor("green", "sm")

#see how these repeaters "know" the parameters?
for i in range(0,4):
    blue_xl()
    green_sm()
