videos=(1029 1028 1026 1022 1021 1019 1018 1017 1016 1015 1014 1012)
for v in ${videos[@]}
do 
	ffmpeg -r 30 -pattern_type glob -i "video_2024$v/*.jpeg" -s 1024x768 -pix_fmt yuv420p -vcodec libx264 2024$v.mp4
done
