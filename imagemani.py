import cv2
import numpy as np
import matplotlib.pyplot as plt

image= cv2.imread("C:/medhansh/python/expert/module2/lessom2/example.jpg")
image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def rotate():
    (h,w)=image_rgb.shape[:2]
    center=(w//2, h//2)
    m= cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated=cv2.warpAffine(image_rgb, m, (w,h))

    plt.imshow(rotated)
    plt.title('Rotated image')
    plt.show()

def bright():
    brightness_matrix=np.ones(image_rgb.shape, dtype='uint8') * 50
    brighter= cv2.add(image_rgb, brightness_matrix)

    plt.imshow(brighter)
    plt.title('brighter image')
    plt.show()

def crop():
    cropped_image= image_rgb[500:4000, 1000:4000]
    plt.imshow(cropped_image)
    plt.title('Cropped image')
    plt.show()

def main():
    while True:
        inp =input("Do you want to: \n1.crop(c) \n2.brighten(b) \n3.rotate(r) \n4.exit \nthe image: ").lower()
        if inp=='exit':
            break
        if inp=='c':
            crop()
            continue
        elif inp=='r':
            rotate()
            continue
        elif inp=='b':
            bright()
            continue
        else:
            print("Write valid response")
            continue

if __name__ == "__main__":
    main()
