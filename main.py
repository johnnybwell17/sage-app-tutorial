import cv2
import numpy as np

from waggle.plugin import Plugin


def compute_mean_color(image):
    return np.mean(image, axis=(0, 1)).astype(float)


def main():
    # Load the tutorial image
    image_bgr = cv2.imread("example.jpg")

    if image_bgr is None:
        raise FileNotFoundError("Could not open example.jpg")

    # OpenCV loads images as BGR; convert to RGB
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    # Compute mean RGB values
    mean_color = compute_mean_color(image_rgb)

    print(f"Mean red:   {mean_color[0]:.2f}")
    print(f"Mean green: {mean_color[1]:.2f}")
    print(f"Mean blue:  {mean_color[2]:.2f}")

    # Publish results locally
    with Plugin() as plugin:
        plugin.publish("color.mean.r", float(mean_color[0]))
        plugin.publish("color.mean.g", float(mean_color[1]))
        plugin.publish("color.mean.b", float(mean_color[2]))


if __name__ == "__main__":
    main()