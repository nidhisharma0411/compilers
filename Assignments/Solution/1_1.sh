echo "Enter Path : "
read Path
echo "Enter Type File(f) or Directory(d) : "
read Type

if [ $Type == 'f' ] 
then
	file='-'
else
	file='d'
fi

ls -l $Path | grep "^$file" 
echo "Total Files/Directory : `ls -l $Path | grep "^$file"  | wc -l`" 