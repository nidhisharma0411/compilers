
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-left*/rightUMINUSleft^left%NAME NUMst : NAME "=" expexp : exp \'+\' exp\n           | exp \'-\' exp\n           | exp \'*\' exp\n           | exp \'/\' exp\n           | exp \'^\' exp\n           | exp \'%\' exp\n           exp : \'-\' exp %prec UMINUSexp : \'(\' exp \')\'exp : NUMexp : NAMEst : exp'
    
_lr_action_items = {'NAME':([0,4,5,7,8,9,10,11,12,13,],[2,15,15,15,15,15,15,15,15,15,]),'-':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,],[4,-11,9,4,4,-10,4,4,4,4,4,4,4,-8,-11,9,9,-2,-3,-4,-5,-6,-7,-9,]),'(':([0,4,5,7,8,9,10,11,12,13,],[5,5,5,5,5,5,5,5,5,5,]),'NUM':([0,4,5,7,8,9,10,11,12,13,],[6,6,6,6,6,6,6,6,6,6,]),'$end':([1,2,3,6,14,15,17,18,19,20,21,22,23,24,],[0,-11,-12,-10,-8,-11,-1,-2,-3,-4,-5,-6,-7,-9,]),'=':([2,],[7,]),'+':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-11,8,-10,-8,-11,8,8,-2,-3,-4,-5,-6,-7,-9,]),'*':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-11,10,-10,-8,-11,10,10,10,10,-4,-5,-6,-7,-9,]),'/':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-11,11,-10,-8,-11,11,11,11,11,-4,-5,-6,-7,-9,]),'^':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-11,12,-10,12,-11,12,12,12,12,12,12,-6,-7,-9,]),'%':([2,3,6,14,15,16,17,18,19,20,21,22,23,24,],[-11,13,-10,13,-11,13,13,13,13,13,13,13,-7,-9,]),')':([6,14,15,16,18,19,20,21,22,23,24,],[-10,-8,-11,24,-2,-3,-4,-5,-6,-7,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'st':([0,],[1,]),'exp':([0,4,5,7,8,9,10,11,12,13,],[3,14,16,17,18,19,20,21,22,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> st","S'",1,None,None,None),
  ('st -> NAME = exp','st',3,'p_assign','pointer.py',44),
  ('exp -> exp + exp','exp',3,'p_oper','pointer.py',48),
  ('exp -> exp - exp','exp',3,'p_oper','pointer.py',49),
  ('exp -> exp * exp','exp',3,'p_oper','pointer.py',50),
  ('exp -> exp / exp','exp',3,'p_oper','pointer.py',51),
  ('exp -> exp ^ exp','exp',3,'p_oper','pointer.py',52),
  ('exp -> exp % exp','exp',3,'p_oper','pointer.py',53),
  ('exp -> - exp','exp',2,'p_uminus','pointer.py',71),
  ('exp -> ( exp )','exp',3,'p_group','pointer.py',75),
  ('exp -> NUM','exp',1,'p_num','pointer.py',79),
  ('exp -> NAME','exp',1,'p_var','pointer.py',83),
  ('st -> exp','st',1,'p_expr','pointer.py',97),
]
