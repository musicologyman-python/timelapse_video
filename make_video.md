# Convert still images to video

To convert still images to video:

```bash
ffmpeg -r 30 -pattern_type glob -i "*.jpeg" -s 1024x768 -pix_fmt yuv420p -vcodec libx264 20241004.mp4
 ```

In the above, `-r 30` is the output framerate

To trim the video

 ```bash
ffmpeg -i 20241004.mp4 -ss 76.833 -t 77.3 -vcodec copy sleeping.mp4
 ```
