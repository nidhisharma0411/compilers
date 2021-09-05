echo "Enter Minimum and Maximum numbers for finding even : "
read Min Max
echo "Enter No of Integers Per Line(1 to 5) "
read A


FLAG=0

if [ $A -gt 5 ]; then
	echo "No of Integers Per Line Cannot be Greater than 5"
else
	for((i=$Min;i<=$Max;i++))
	do
		if [ `echo "$i % 2" | bc` -eq 0 ]; then
			printf "$i "
			FLAG=$((FLAG + 1))
			if [ $FLAG == $A ];then
				printf " \n"
				FLAG=0
			fi
			fi
	done
fi


