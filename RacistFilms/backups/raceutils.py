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
    frame = cv2.resize(frame, (640, 480))

    for i in range(0, frames_skipped+1):
        video.read()

    return flag, frame


def __race_detect(f_img_tuple):
    """
    Find race and gender of analyzed face. The function iterates through list of ROI considered to contain faces, and
      puts them through racial detection analysis

    Inputs:
    f_img_tuple - function returning tuple of ROIs which'll be analyzed

    Outputs:
    face_data - dict containing race and gender
    """

    face_data_list = []

    for face_area in f_img_tuple():
        face_data = DeepFace.analyze(face_area, actions=('race', 'gender'), enforce_detection=False)

        face_data_list.append(face_data)

    return face_data_list


@__race_detect
def __detect_face_areas(f_img):
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
    face_detect = face_cascade.detectMultiScale(f_img(), scaleFactor=1.05, minNeighbors=5)

    for face in face_detect:

        roi = f_img()[face[1]:face[1] + face[3], face[0]:face[0] + face[3]]
        rois.append(roi)

    return tuple(rois)


@__detect_face_areas
def detect_races(img):
    """
    Parses image to __detect_face_areas, and leaves them for further analysis. Provided just for reading convenience,
    any image transforms (such as color space, size changes) should be done here.

    Inputs:
    img - image array in 8UC3 format. Others might work, it wasn't tested (don;t put too much thought into program that
      detects skin colour in movies lol.

    Outputs:
    None
    """

    return img


def build_figure(labels_dict, video_name):

    fig = go.Figure(data=[go.Bar(
        x=tuple(labels_dict.keys()),
        y=tuple(labels_dict.values()),
        textposition='auto'
    )])

    fig.update_layout(title_text=video_name)

    return fig
