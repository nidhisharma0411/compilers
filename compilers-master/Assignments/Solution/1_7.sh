ls
echo "Enter Filename"
read Filename
echo "How many copies you want to make"
read copy

for((i=0;i<$copy;i++))
	do
		echo "Enter New Filename with you want to copy(With Extension)"
		read new_file
		echo "`cp $Filename $new_file`"
	done