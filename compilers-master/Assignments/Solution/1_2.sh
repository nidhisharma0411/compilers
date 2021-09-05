echo "Enter Path : "
read Path
echo "Enter File Type Read(r), Write(w), Executable(x) and SetUID Files(s): "
read Type

if [ $Type == 'r' ] 
then
	ls -l $Path | grep "^-r" 
	echo "Total Readable Files are : `ls -l $Path | grep "^-r" | wc -l`" 
elif [ $Type == 'w' ]; then
	ls -l $Path | grep -E "^--w|^-rw" 
	echo "Total Writable Files are : `ls -l $Path | grep -E "^--w|^-rw" | wc -l`" 
elif [ $Type == 's' ]; then
	ls -l $Path | grep -E "^-r-sr"
	echo "Total SetUID Files are : `ls -l $Path | grep -E "^-r-sr" | wc -l`"
else
	ls -l $Path | grep -E "^---x|^-r-x|^-rwx|^--wx" 
	echo "Total Executable Files are : `ls -l $Path | grep -E "^---x|^-r-x|^-rwx|^--wx" | wc -l`" 
fi

