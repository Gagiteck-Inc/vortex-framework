from PIL import Image, ImageDraw
import random

class AvatarGenerator:
    def __init__(self, size=200):
        self.size = size

    def generate_avatar(self):
        # Create a blank canvas
        avatar = Image.new("RGB", (self.size, self.size), "white")
        draw = ImageDraw.Draw(avatar)

        # Random background color
        bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.rectangle([0, 0, self.size, self.size], fill=bg_color)

        # Generate random shapes (circles and rectangles)
        for _ in range(5):
            shape_type = random.choice(["circle", "rectangle"])
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            if shape_type == "circle":
                x = random.randint(10, self.size - 10)
                y = random.randint(10, self.size - 10)
                radius = random.randint(5, 40)
                draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=color)

            else:  # Rectangle
                x1 = random.randint(10, self.size - 40)
                y1 = random.randint(10, self.size - 40)
                x2 = random.randint(x1 + 10, self.size - 10)
                y2 = random.randint(y1 + 10, self.size - 10)
                draw.rectangle([x1, y1, x2, y2], fill=color)

        return avatar

# Usage
if __name__ == "__main__":
    generator = AvatarGenerator(size=200)
    avatar = generator.generate_avatar()
    avatar.show()  # Display the generated avatar
    avatar.save("Avatar5.png")  # Save the avatar to a file
