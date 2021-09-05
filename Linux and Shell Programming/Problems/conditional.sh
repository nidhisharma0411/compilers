read a
read b
read c

if [ $a != $b ] && [ $b != $c ]
then 
  echo "SCALENE"
elif [ \( $a == $b \) -o \( $b == $c \) ]
then
  echo "EQUILATERAL"
else
  echo "ISOSCELES"
fi