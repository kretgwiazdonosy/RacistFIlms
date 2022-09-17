""""
A brief module containing all race detection and analytic tools
"""

from deepface import DeepFace
import cv2
import plotly.graph_objects as go

# this bozo is a function loading training file
classifier = 'classifiers/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(classifier)


def read_video(video, frames_skipped=0):
    """
    Read one frame and skip given amount of next frames, so the video'll be analyzed faster

    Inputs:
    frames_skipped - how many frames should be skipped when the function will be called again
    video - analyzed video

    Outputs:
    frame - video frame array (8UC3 format)
    flag - if none frame's been grabbed, then 'False' value is returned
    """

    flag, frame = video.read()

    try:
        frame = cv2.resize(frame, (640, 480))

    except cv2.error:
        print('shit happened during resizing, handle this later. kind regards')

    for i in range(0, frames_skipped+1):
        video.read()

    return flag, frame


def race_detect(anal_img):
    """
    Find race and gender of analyzed face. The function iterates through list of ROI considered to containg

    Inputs:
    img_path - analyzed image array OR path to analyzed img

    Outputs:
    face_data - dict containing race and gender
    """

    face_data = DeepFace.analyze(anal_img, actions=('race', 'gender'), enforce_detection=False)

    return face_data


def detect_face_areas(img):
    """
    Detects faces on given image, and creates regions of interest that include them.

    Inputs:
    image - function returning image array in 8U format (others might work, idk)

    Outputs:
    rois - tuple of regions of interest with detected faces
    """
    print('Wykonywanie funkcji detect_face_areas')
    rois = []

    # run detection
    face_detect = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)

    for face in face_detect:

        roi = img[face[1]:face[1] + face[3], face[0]:face[0] + face[3]]
        rois.append(roi)

    return tuple(rois)


def build_figure(labels_dict, video_name):

    fig = go.Figure(data=[go.Bar(
        x=tuple(labels_dict.keys()),
        y=tuple(labels_dict.values()),
        textposition='auto'
    )])

    fig.update_layout(title_text=video_name)

    return fig
