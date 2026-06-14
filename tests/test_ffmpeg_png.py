import os
import uuid
import ffmpeg
import tempfile
import shutil

def test_hstack_webp():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    icon_path = os.path.join(base_dir, "resources", "icon_small.png")
    
    icon_path2 = os.path.join(tempfile.gettempdir(), "temp_icon2.png")
    shutil.copy(icon_path, icon_path2)
    
    random_filename = uuid.uuid4().hex
    result_filepath = os.path.join(tempfile.gettempdir(), f"{random_filename}.webp")

    w = 200
    h = 200
    
    streams = [
        ffmpeg.input(filename=icon_path).filter('scale', w=w, h=h),
        ffmpeg.input(filename=icon_path2).filter('scale', w=w, h=h)
    ]
    
    joined = ffmpeg.filter(streams, 'hstack', inputs=len(streams))
    
    try:
        joined.output(
            result_filepath,
            vcodec="libwebp",
            lossless=1,
            vframes=1,
        ).run(overwrite_output=True)
        print("Success, saved to", result_filepath)
        print("Size:", os.path.getsize(result_filepath))
    except ffmpeg.Error as e:
        print("Error:", e.stderr.decode('utf-8'))

if __name__ == "__main__":
    test_hstack_webp()
