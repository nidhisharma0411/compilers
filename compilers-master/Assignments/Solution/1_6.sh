echo "Delete a File or undelete recent file"
echo "Enter 1 for Deleting a file and 2 for undeleting a file"
read action

if [ $action == 1 ]; then
	ls
	echo "Enter Filename"
	read Filename
	pwd="`pwd`/"
	sed -i "1i $pwd" $Filename
	mv $Filename /home/jarvis/Recycle/
	echo "File Deleted"
else
	echo "Recently Deleted Files are"
	ls /home/jarvis/Recycle/
	cd /home/jarvis/Recycle/
	echo "Enter Filename You want to restore"
	read filename
	path=$(head -n 1 "$filename")
	sed -i 1,1d $filename
	mv $filename $path
	echo "File Restored"
fi
