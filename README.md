# FrameBot

This script can be used to run Every <mask> Frame in Order facebook page.

## Usage

1. `git clone https://github.com/Wikidepia/FrameBot`, to download the source code.
2. `cd FrameBot`, to enter the directory.
3. `python3 -m venv venv && . venv/bin/activate` to create and activate a virtual environment.
3. `pip install -U -r requirements.txt`, to install the requirements.
4. Copy-paste `config.ini.example` to `config.ini` and replace the values with your own.
5. Put videos to `videos` folder, make sure it start with `e<episode>`. For example `e1.mp4`.
5. Run with `python3 main.py`.
6. Stop with <kbd>CTRL+C</kbd> and `deactivate` the virtual environment.

## Credits

[Boidushya](https://github.com/Boidushya/FrameBot), [Hayden Faulkner](https://medium.com/@haydenfaulkner/extracting-frames-fast-from-a-video-using-opencv-and-python-73b9b7dc9661)
