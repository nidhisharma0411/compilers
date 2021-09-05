echo "Enter Size of File Minimum(in KB)"
read size
find . -type f -size +"$size"k -exec stat -c%s" "%n {} \; | sort -rn