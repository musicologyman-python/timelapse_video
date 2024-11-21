today_dir_name=$(date +%Y%m%d)

if [ ! -d "$today_dir_name" ]
then
    mkdir $today_dir_name
fi

if [ -e "capture.sh" ]
then
    cp capture.sh $today_dir_name/capture.sh
else
    echo "capture.sh not found"
    exit 1
fi

cd $today_dir_name
sh capture.sh
