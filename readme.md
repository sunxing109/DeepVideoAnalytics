# Deep Video Analytics &nbsp; &nbsp; [![Build Status](https://travis-ci.org/AKSHAYUBHAT/DeepVideoAnalytics.svg?branch=master)](https://travis-ci.org/AKSHAYUBHAT/DeepVideoAnalytics) [![Build Status](https://travis-ci.org/AKSHAYUBHAT/DeepVideoAnalytics.svg?branch=stable)](https://travis-ci.org/AKSHAYUBHAT/DeepVideoAnalytics/branches)
#### by [Akshay Bhat](http://www.akshaybhat.com)

![UI Screenshot](docs/figures/emma.png "Emma Watson, from poster of her latest subject appropriate movie The Circle")

Deep Video Analytics is a platform for indexing and extracting information from videos and images.
With latest version of docker installed correctly, you can run Deep Video Analytics in minutes
locally (even without a GPU) using a single command.

### Architecture

Deep Video Analytics implements a client-server architecture pattern, where clients can access state of the server
via a REST API. For uploading, processing data, training models, performing queries, i.e. mutating the state
clients can send DVAPQL (Deep Video Analytics Processing and Query Language) formatted as JSON. The query represents
a directed acyclic graph of operations.

### Visual Data Network

A separate repository [VisualDataNetwork/root](https://github.com/VisualDataNetwork/root) maintains examples of
DVAPQL scripts for performing tasks such as processing image dataset (e.g. COCO), Youtube videos, Twitch livestreams,
training FAISS indexers  etc.


### Installation & Demo

Please visit [https://www.deepvideoanalytics.com](https://www.deepvideoanalytics.com)

### Documentation

- For a quick overview we **strongly recommend** going through the [presentation in readme.pdf](/docs/readme.pdf)

### Experiments

- **OCR example has been moved to [/docs/experiments/ocr](/docs/experiments/ocr) directory**.

### Code organization

- /client : Python client using DVA REST API
- /configs : ngnix config + default models + processing pipelines
- /deploy : Dockerfiles + Instructions for development, single machine deployment and scalable deployment with Kubernetes
- /docs : Documentation, tutorial and experiments
- /tests : Tests, Notebooks for interactive debugging andtest data
- /repos : Code copied from third party repos, e.g. Yahoo LOPQ, TF-CTPN etc.
- /server : dvalib + django server contains contains bulk of the code for UI, App and models.
- /logs : Empty dir for storing logs

### Libraries present in this repository and their licenses

| Library  | Link to the license | 
| -------- | ------------------- |
| YAD2K  |  [MIT License](https://github.com/allanzelener/YAD2K/blob/master/LICENSE)  |
| AdminLTE2  |  [MIT License](https://github.com/almasaeed2010/AdminLTE/blob/master/LICENSE) |
| FabricJS |  [MIT License](https://github.com/kangax/fabric.js/blob/master/LICENSE)  |
| Facenet   |  [MIT License](https://github.com/davidsandberg/facenet)  |
| JSFeat   |  [MIT License](https://inspirit.github.io/jsfeat/)  |
| MTCNN   |  [MIT License](https://github.com/kpzhang93/MTCNN_face_detection_alignment)  |
| Insight Face   |  [MIT License](https://github.com/deepinsight/insightface)  |
| CRNN.pytorch  |  [MIT License](https://github.com/meijieru/crnn.pytorch/blob/master/LICENSE.md)  |
| Original CRNN code by Baoguang Shi  |  [MIT License](https://github.com/bgshih/crnn) |
| Object Detector App using TF Object detection API |  [MIT License](https://github.com/datitran/Object-Detector-App) | 
| Plotly.js |  [MIT License](https://github.com/plotly/plotly.js/blob/master/LICENSE) | 
| Text Detection CTPN  |  [MIT License](https://github.com/eragonruan/text-detection-ctpn/LICENSE) |
| SphereFace  |  [MIT License](https://github.com/wy1iu/sphereface/blob/master/license) |
| Segment annotator  |   [BSD 3-clause](https://github.com/kyamagu/js-segment-annotator/blob/master/LICENSE) |
| Youtube 8M feature extractor weights  | [Apache 2.0](https://github.com/google/youtube-8m) |
| LOPQ   |  [Apache 2.0](https://github.com/yahoo/lopq/blob/master/LICENSE)  | 
| Open Images Pre-trained network  |  [Apache 2.0](https://github.com/openimages/dataset/blob/master/LICENSE) |
| Interval Tree  |  [Apache 2.0](https://github.com/chaimleib/intervaltree) |

### Libraries present in container (/root/thirdparty/)

| Library  | Link to the license |
| -------- | ------------------- |
| faiss | [BSD + PATENTS License](https://github.com/facebookresearch/faiss/blob/master/LICENSE) |
| dlib | [Boost Software License](https://github.com/davisking/dlib/blob/master/dlib/LICENSE.txt) |



### Additional libraries & frameworks

* FFmpeg (not linked, called via a Subprocess)
* Tensorflow 
* OpenCV
* Numpy
* Pytorch
* Docker
* LMDB
* Nvidia-docker
* Docker-compose
* All packages in [requirements.txt](/requirements.txt)
* All dependancies installed in [CPU Dockerfile](/deploy/dockerfiles/Dockerfile) & [GPU Dockerfile](/deploy/dockerfiles/Dockerfile.gpu)


# License & Copyright

**Copyright 2016-2018, Akshay Bhat, All rights reserved.**

# Contact

Deep Video Analytics is nearing stable 1.0, we expect to release in Summer 2018.
The license will be relaxed once a stable release version is reached.
Please contact me for more information.
 
