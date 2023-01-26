from captcha.image import ImageCaptcha
import random
import uuid
import os

alphabet = list("0123456789abcdefghijklmnopqrstuvwxyz")
num = list("0123456789")

image = ImageCaptcha(width=96, height=72)
img_dir = "./captcha/task3"
num_captcha = 10000

for counter in range(num_captcha):
    i = random.choices(alphabet, k=4)
    captcha = "".join(i)
    fn = os.path.join(img_dir, "%s_%s.png" % (captcha, uuid.uuid4()))
    image.write(captcha, fn)
