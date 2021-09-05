## PLY Examples

1. Simple Calculator ([calc.py](https://github.com/ihiteish/compilers/blob/master/examples/calc.py)) - A Simple Calculator with +, -, *, /, % and Power
  * command - python calc.py

2. Calculator with Complex Number Support([complex.py](https://github.com/ihiteish/compilers/blob/master/examples/complex.py)) , can perform +, -, *, / and Power on complex numbers, pass complex number (real,imag)
  * command - python complex.py

3. Single Expression AST([ast.py](https://github.com/ihiteish/compilers/blob/master/examples/ast.py)) - Will generate AST for single expression link a+b,a-c,a/d,a*d. Run this file using ast.sh
  * Change Permission of ast.sh to executable first and run this command
  * commmand - ./ast.sh python_filename(ast.py)  generating_dot_filename(eg. graph.dot) generating_pdf_filename(eg. graph.pdf)

4. Full AST([complete_ast.py](https://github.com/ihiteish/compilers/blob/master/examples/complete_ast.py)) - Will generate a full AST for given expression. Run using c_ast.sh(Inst. in c_ast.sh comments)
  * Change Permission of ast.sh to executable first and run this command
  * command - ./ast.sh python_filename(here it is complete_ast.py)
