import configparser
import os
import time

import facebook
import schedule

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    frame_dir = sorted(
        [f for f in os.listdir("./frames") if not f.startswith(".")],
        key=lambda f: f.lower(),
    )
    if len(frame_dir) == 0:
        raise ValueError("Frame folder is empty.")

    # Save temporary data about amount of frame
    with open("./tmp_data", "a+") as f:
        f.seek(0)
        filled = f.read(1)
        if not filled:
            total_frames = str(len(frame_dir))
            f.write(total_frames)
        else:
            f.seek(0)
            total_frames = str(f.readline())

    return post(frame_dir[0], total_frames)


def post(frame_fname, total_frames):
    fb_token = config["framebot"]["fb_token"]
    prefix = config["framebot"]["prefix"]
    current_frame = f"frames/{frame_fname}"
    current_frame_num = os.path.splitext(frame_fname)[0]

    message = (
        f"{prefix} | Episode 1 | Frame {current_frame_num} out of {str(total_frames)}"
    )
    graph = facebook.GraphAPI(fb_token)
    graph.put_photo(image=open(current_frame, "rb"), message=message)
    print(f"Posted frame {current_frame_num} of {str(total_frames)} successfully!")
    os.remove(current_frame)


if __name__ == "__main__":
    interval = config["framebot"]["interval"]
    schedule.every(interval).minutes.do(main).run()
    while True:
        schedule.run_pending()
        time.sleep(1)
