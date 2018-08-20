# Practical Deep OCR for scene text using CTPN + CRNN


#### Please note that the CTPN code used in this post has been updated.
#### Instead of the Caffe based CTPN I have migrated to (Tensorflow CTPN by eragonruan](https://github.com/eragonruan/text-detection-ctpn)

This folder contains two notebooks which demonstrate use of CTPN [1,2, 5] for
Text box detection and CRNN (PyTorch implmentation) [3,4] for Text character recognition. Most online tutorials 
describe traditional OCR techniques using Tessaract. However Tessaract is not useful for scene text recognition, 
i.e. text occurring in natural scenes, with wide variation in fonts, colors and background. Over the last couple of years 
significant improvements have been made in using deep learning for OCR, in this demo we will show how you can use 
a textbox detector and a text recognition model to perform OCR on scene text. Its possible to get good
out-of-box performance without any having to perform any fine-tuning. Finally this pipeline has been integrated in 
Deep Video Analytics and can be used in conjunction with other detection/indexing models, and eventually in future can be fine-tuned
(similar to YOLO detectors).

To run following two notebooks, start docker container (containers will be automatically downloaded from docker-hub) 
using following command and open the url show in terminal.

````bash
# If you have an nvidia GPU with nvidia-docker and Docker
nvidia-docker run -p 8888:8888 -it akshayubhat/dva-auto:gpu bash
# Else if DONT have a GPU run following docker command
docker run -p 8888:8888 -it akshayubhat/dva-auto:latest bash
# Switch to Master branch and pull
git reset --hard && git checkout --track origin/master && git pull
cd /root/DVA/docs/experiments/ocr
jupyter notebook --ip=0.0.0.0 --no-browser --allow-root
# Above command will give you a url in form of http://0.0.0.0:8888/?token=824231234fbb231231231d438465f
# REPLACE 0.0.0.0 with localhost (e.g. http://localhost:8888/?token=824231234fbb231231231d438465f ) 
# Open above URL in your favorite browser
````


Its possible to run this code on CPU but it will be very slow and requires setting cpu_mode in detect_text.ipynb. However
since the code runs using Docker there are no dependencies to install!

Once you have started the container, go to the Jupyter notebook url displayed in the console and navigate to "notebooks/OCR".

## Text detection

![detection](detection.png "detection")

The textbox detection is implemented using Connectionist Text Proposal Network [1,2].
In this demo images in [images](/notebooks/OCR/images/) folder are processed using CTPN and extracted textboxes are stored in the [boxes](/notebooks/OCR/boxes/)
folder. 

You can find the notebook here
[https://github.com/AKSHAYUBHAT/DeepVideoAnalytics/blob/master/notebooks/OCR/detect_text.ipynb](https://github.com/AKSHAYUBHAT/DeepVideoAnalytics/blob/master/notebooks/OCR/detect_text.ipynb)


## Text recognition

![recognition](recognition.png "recognition")

In this notebook the stored [boxes](/notebooks/OCR/boxes/) are then processed using CRNN [3,4] to extract text. 
Note that you cannot import caffe and pytorch into same notebook/process since it causes library/static linking issues.

You can find the notebook here
[https://github.com/AKSHAYUBHAT/DeepVideoAnalytics/blob/master/notebooks/OCR/recognize_text.ipynb](https://github.com/AKSHAYUBHAT/DeepVideoAnalytics/blob/master/notebooks/OCR/recognize_text.ipynb)


## Integration with Deep Video Analytics

Both CTPN & CRNN have been integrated into [Deep Video Analytics](https://www.deepvideoanalytics.com) and now its possible to run OCR directly on videos/images
without having to write any code. Extracted text can be conveniently queried using Postgres full-text search through the User Interface.


### References:

1. [https://github.com/tianzhi0549/CTPN](https://github.com/tianzhi0549/CTPN)
2. [https://github.com/qingswu/CTPN (CUDA 8.0 compatible, used here)](https://github.com/qingswu/CTPN)
3. [https://github.com/meijieru/crnn.pytorch](https://github.com/meijieru/crnn.pytorch)
4. [https://github.com/bgshih/crnn (Original implementation)](https://github.com/bgshih/crnn)
5. [https://github.com/eragonruan/text-detection-ctpn](https://github.com/eragonruan/text-detection-ctpn)
