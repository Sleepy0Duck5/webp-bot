import asyncio
import os
import sys

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, base_dir)

from webp_bot.handler import Handler

async def main():
    handler = Handler()
    urls = [
        "https://ac.namu.la/20260608sac/ec22d13d2dcd4d45983c712a4abbd7ffac24111b31d8bb479a545b704b5d7b35.mp4?expires=1782867600&key=69GD4B8Y7vyvUukADU5Jxw",
        "https://ac.namu.la/20260608sac/96955d104ce333a72f18d23e783350e52eea827ff8f7a4badcd88b72437f5dda.mp4?expires=1782867600&key=qpAry83GsFKXR7Q7DyqU8w"
    ]
    
    print("Testing from_urls...")
    try:
        image = await handler.from_urls(urls)
        print("Success! Created image:", image.get_path(), "Name:", image.get_name())
        
        import shutil
        out_path = os.path.join(base_dir, "tests", "test_output.webp")
        shutil.copy(image.get_path(), out_path)
        print("Saved to", out_path)
        image.delete()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())
