
""""""" Get total time of list of videos """""""
import cv2
import os
def min_to_min_seconds(total_mins):

    total_mins, base_1OO_seconds = divmod(total_mins, 1)
    seconds = int(base_1OO_seconds *60)

    return (total_mins, seconds)

def get_total_length_of_video(video_path,verbose = False):
    video = cv2.VideoCapture(video_path)
    frame_rate = video.get(cv2.CAP_PROP_FPS)
    total_frames  = video.get(cv2.CAP_PROP_FRAME_COUNT)
    total_seconds = total_frames/frame_rate
    total_mins = total_seconds/60
    
    if verbose:
        total_minutes,total_seconds = min_to_min_seconds(total_mins)
        print(video_path,':','time:',int(total_minutes),':',total_seconds)

    return total_mins

def total_playlist_time(video_list):
    total_time=0.0
    for video_path in video_list:
        total_time += get_total_length_of_video(video_path)

    total_min,total_seconds=min_to_min_seconds(total_time)
    print('total time:',int(total_min),':',total_seconds)

def create_video_list(video_dir):
    videos=os.listdir(video_dir)
    videos=[os.path.join(video_dir,video) for
            video in videos if video.endswith(('.mp4'))]
    return videos


if __name__ == "__main__":
    VIDEO_PATH='.'
    videos=create_video_list(VIDEO_PATH)
    total_playlist_time(videos)
    
    
    





















