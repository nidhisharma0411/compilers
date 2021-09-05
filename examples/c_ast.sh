# File with extension
# ./ast.sh python_filename 

python $1

echo "`dot -Tpdf graph.dot -o graph.pdf`"
echo "`cat graph.dot`"
echo "`evince graph.pdf`"
