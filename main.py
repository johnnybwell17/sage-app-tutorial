import numpy as np

from waggle.data.vision import Camera
from waggle.plugin import Plugin


def compute_mean_color(image):
    return np.mean(image, axis=(0, 1)).astype(float)


def main():
    with Plugin() as plugin:
        # Open the camera and take a snapshot.
        with Camera() as camera:
            snapshot = camera.snapshot()

        # Compute and publish the mean RGB values.
        mean_color = compute_mean_color(snapshot.data)
        plugin.publish("color.mean.r", mean_color[0], timestamp=snapshot.timestamp)
        plugin.publish("color.mean.g", mean_color[1], timestamp=snapshot.timestamp)
        plugin.publish("color.mean.b", mean_color[2], timestamp=snapshot.timestamp)

        # Save and upload the captured image.
        snapshot.save("snapshot.jpg")
        plugin.upload_file("snapshot.jpg", timestamp=snapshot.timestamp)


if __name__ == "__main__":
    main()
