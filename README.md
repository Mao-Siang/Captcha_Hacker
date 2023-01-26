# Captcha_Hacker
This is my implementation of [Captcha Hacker](https://www.kaggle.com/competitions/captcha-hacker).

## Methods
First, generate more training data using the captcha package by running:
```python
python3 gendata.py
```
You can modify the number of words in the captcha by editing the value of `k` in line 13, the output directory by editing the `img_dir` variable, and the number of new generated images by editing the `num_captcha` variable.

Then, use pretrained ResNet-18 model with linear layers to predict the captcha.

## Train

### Data
Generate more training data using `gendata.py` or add other datasets to train together with the provided data.

### Start training
Run the python notebook on Colab (Recommended).
If you want to run at local, make sure you have torch, cv2, torchvision, etc. packages installed.<br>
<br>
Install by pip:
```bash
pip install torch opencv-python torchvision
```

## Inference
You can use the pretrained model [here](shorturl.at/lAM354) to predict the captcha and write into `submission.csv`.

Run the `inference.ipynb` on Google Colab (Recommended).

Then submit the CSV file to [Kaggle](https://www.kaggle.com/competitions/captcha-hacker/data) to check the results.


