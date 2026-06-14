import os
import ffmpeg

def test_hstack():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    icon_path = os.path.join(base_dir, "resources", "icon_small.png")
    out_path = os.path.join(base_dir, "tests", "test_hstack_scaled.webp")
    
    try:
        streams = [
            ffmpeg.input(icon_path).filter('scale', w=200, h=200),
            ffmpeg.input(icon_path).filter('scale', w=200, h=200)
        ]
        joined = ffmpeg.filter(streams, 'hstack', inputs=len(streams))
        out = ffmpeg.output(joined, out_path, vcodec="libwebp", loop=0, vsync=0)
        ffmpeg.run(out, overwrite_output=True)
        print("Success, saved to", out_path)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_hstack()
