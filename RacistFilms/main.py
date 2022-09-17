import raceutils
import glob
import cv2
import keyboard

# create paths to films
print('Tworzenie ścieżek')
films_path = []
for film_path in glob.glob('materials/videos/*.mp4'):
    films_path.append(film_path.replace(chr(92), '/'))

races = {'black': 0,
         'white': 0,
         'asian': 0,
         'indian': 0,
         'middle eastern': 0,
         'latino hispanic': 0}

# read those videos
print('Odtworzenie filmów')
for film_path in films_path:
    vid_name = film_path.split('/')[-1]
    vid = cv2.VideoCapture(film_path)

    isVidPlaying, frame = raceutils.read_video(vid, frames_skipped=0)

    print('Wykonanie pętli isVidPlaying')
    while isVidPlaying:

        for face_area in raceutils.detect_face_areas(frame):
            detection = raceutils.race_detect(face_area)

            print(detection)
            for race in races:
                if race == detection['dominant_race']:
                    races[race] += 1
                    break

            print(f'Przeanalizowano {int((vid.get(cv2.CAP_PROP_POS_FRAMES)/vid.get(cv2.CAP_PROP_FRAME_COUNT)*100))}%'
                  f' filmu {vid_name}')

        isVidPlaying, frame = raceutils.read_video(vid, frames_skipped=45)

        if keyboard.is_pressed('q'):
            break

    raceutils.build_figure(races, vid_name).write_image(f"graphs/{vid_name.replace('.mp4', '')}.pdf")

    races = {'black': 0,
             'white': 0,
             'asian': 0,
             'indian': 0,
             'middle eastern': 0,
             'latino hispanic': 0}

vid.release()
