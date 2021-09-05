# All File with extension
# ./ast.sh python_filename  dot_filename generating_pdf_filename

python $1 $2

echo "}" >> $2
echo "`dot -Tpdf $2 -o $3`"
echo "`evince $3`"
