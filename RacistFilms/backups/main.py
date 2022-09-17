import raceutils
import glob
import cv2

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

    isVidPlaying, frame = raceutils.read_video(vid, frames_skipped=5)

    print('Wykonanie pętli isVidPlaying')
    while isVidPlaying:

        for face in raceutils.detect_races(frame):

            for race in races:

                if race == face['dominant_race']:
                    races[race] += 1

        isVidPlaying, frame = raceutils.read_video(vid, frames_skipped=5)

    raceutils.build_figure(races, vid_name).write_image(f"graphs/{vid_name.replace('.mp4', '')}.pdf")

    races = {'black': 0,
             'white': 0,
             'asian': 0,
             'indian': 0,
             'middle eastern': 0,
             'latino hispanic': 0}

vid.release()

