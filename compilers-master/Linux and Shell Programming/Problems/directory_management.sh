list(){
	echo "Directory - `pwd | sed 's#.*/##'`"

	case $1 in
	     1) et=py ;; ##len="3" ;;
         2) et="c" ;; ##len="2" ;;
         3) et="cpp" ;; ##len="4" ;;
         4) et="php" ;; ##len="4" ;;
         5) et="sh" ;; ##len="3" ;;
         *) ##$len='0' ;;
    esac

	for entry in *
	do
		if [ -d "$entry" ]; then
			cd $entry
			list
			cd ../
		elif [ -f "$entry" ]; then
			modDate1="`date -r $entry +"%Y-%m-%d %H:%M:%s"`"

			## Other Options
			# if [[ ! -f ${entry}.py ]] ; then
			# 	## if [ "$modDate1" "<" "2018-05-28 12:08:1527143894" ]; then
			# 		echo " ---> File - $entry $modDate1"
			# 		cp "$entry" "/home/jarvis/Desktop/all_c_program/"
			# 	## fi
			# fi
			# if [ ${entry: -$2"} == "$1" ]; then
			# 	## if [ "$modDate1" "<" "2018-05-28 12:08:1527143894" ]; then
			# 		echo " ---> File - $entry $modDate1"
			# 		cp "$entry" "/home/jarvis/Desktop/all_c_program/"
			# 	## fi
   #          fi


            folder="new_php"
			if [ "${entry##*.}" = "$et" ]; then
				## if [ "$modDate1" "<" "2018-05-28 12:08:1527143894" ]; then
					echo " ---> File - $entry $modDate1"
					cp "$entry" "/home/jarvis/Desktop/$folder/"
				## fi
            fi	
		fi
	done
}

echo "Choose File Formats"
echo "1.) Python"
echo "2.) C"
echo "3.) C++"
echo "4.) PHP"
echo "5.) Shell"
echo "6.) None"

read E_T



list $E_T ##$len