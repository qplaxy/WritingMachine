
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSRESTAleftMULTIPLICACIONDIVISIONrightUMENOSrightPOTENCIAADD AND BEGIN COMA CONTINUEDOWN CONTINUELEFT CONTINUERIGHT CONTINUEUP CORCHETEDER CORCHETEIZQ DEF DIV DIVISION DOWN EQUAL FALSE FIN GREATER ID IF IFELSE IGUAL IGUALES INT MAIN MAYORQUE MENORQUE MULT MULTIPLICACION OR PARA PARENTESISDER PARENTESISIZQ PLUS POS POSX POSY POTENCIA POWER PUT PYC RANDOM REPEAT RESTA RUN SMALLER SPEED STRING SUBSTR SUM TRUE UNTIL UP USECOLOR WHILE sentencias : sentencias sentencia\n                            | sentencia\n    sentencia : expresion\n                 | add\n                 | continue\n                 | pos\n\n    sentencia : DEF ID IGUAL valor PYC\n    sentencia : PUT ID IGUAL valor PYC\n                 | PUT ID IGUAL expresion PYC\n    add : ADD CORCHETEIZQ ID CORCHETEDER PYC\n           | ADD CORCHETEIZQ ID ID CORCHETEDER PYC\n           | ADD CORCHETEIZQ ID INT CORCHETEDER PYC\n    valor : INT\n             | ID\n             | expresion\n    continue : CONTINUEUP INT PYC\n                | CONTINUEUP ID PYC\n                | CONTINUEUP expresion PYC\n                | CONTINUEDOWN INT PYC\n                | CONTINUEDOWN ID PYC\n                | CONTINUEDOWN expresion PYC\n                | CONTINUERIGHT INT PYC\n                | CONTINUERIGHT ID PYC\n                | CONTINUERIGHT expresion PYC\n                | CONTINUELEFT INT PYC\n                | CONTINUELEFT ID PYC\n                | CONTINUELEFT expresion PYC\n    pos : POS CORCHETEIZQ expresion COMA expresion CORCHETEDER PYC\n            | POS CORCHETEIZQ valor COMA valor CORCHETEDER PYC\n            | POS CORCHETEIZQ valor COMA expresion CORCHETEDER PYC\n            | POS CORCHETEIZQ expresion COMA valor CORCHETEDER PYC\n            | POSX expresion PYC\n            | POSX valor PYC\n            | POSY expresion PYC\n            | POSY valor PYC\n    expresion : expresion PLUS expresion\n               | expresion RESTA expresion\n               | expresion MULTIPLICACION expresion\n               | expresion DIVISION expresion\n               | expresion POTENCIA expresion\n   expresion : RESTA expresion %prec UMENOSexpresion : INTexpresion : PARENTESISIZQ expresion PARENTESISDERexpresion : condicioncondicion : expresion MAYORQUE expresion\n                 | expresion MENORQUE expresion\n                 | expresion IGUALES expresion\n    '
    
_lr_action_items = {'DEF':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[7,7,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'PUT':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[8,8,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'RESTA':([0,1,2,3,4,5,6,9,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,32,33,35,37,38,40,41,43,44,46,47,48,50,52,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,85,86,88,92,93,94,95,96,98,100,103,104,105,110,111,112,113,],[9,9,-2,23,-4,-5,-6,9,-42,9,-44,9,9,9,9,9,9,-1,9,9,9,9,9,9,9,9,-41,23,-42,23,-42,23,-42,23,-42,23,9,23,-42,23,-36,-37,-38,-39,-40,23,23,23,9,9,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,23,-32,-33,-34,-35,-42,23,23,9,9,-7,-8,-9,-10,23,23,-11,-12,-28,-31,-29,-30,]),'INT':([0,1,2,3,4,5,6,9,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,32,47,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,92,93,94,95,96,98,104,105,110,111,112,113,],[10,10,-2,-3,-4,-5,-6,10,-42,10,-44,35,38,41,44,50,50,-1,10,10,10,10,10,10,10,10,-41,50,-36,-37,-38,-39,-40,-45,-46,-47,85,85,-43,91,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,50,85,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'PARENTESISIZQ':([0,1,2,3,4,5,6,9,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,32,47,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,92,93,94,95,96,98,104,105,110,111,112,113,],[11,11,-2,-3,-4,-5,-6,11,-42,11,-44,11,11,11,11,11,11,-1,11,11,11,11,11,11,11,11,-41,11,-36,-37,-38,-39,-40,-45,-46,-47,11,11,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,11,11,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'ADD':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[13,13,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'CONTINUEUP':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[14,14,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'CONTINUEDOWN':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[15,15,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'CONTINUERIGHT':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[16,16,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'CONTINUELEFT':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[17,17,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'POS':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[18,18,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'POSX':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[19,19,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'POSY':([0,1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[20,20,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'$end':([1,2,3,4,5,6,10,12,21,32,54,55,56,57,58,59,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,94,95,96,98,104,105,110,111,112,113,],[0,-2,-3,-4,-5,-6,-42,-44,-1,-41,-36,-37,-38,-39,-40,-45,-46,-47,-43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-32,-33,-34,-35,-7,-8,-9,-10,-11,-12,-28,-31,-29,-30,]),'PLUS':([3,10,12,32,33,35,37,38,40,41,43,44,46,48,50,52,54,55,56,57,58,59,60,61,64,78,85,86,88,100,103,],[22,-42,-44,-41,22,-42,22,-42,22,-42,22,-42,22,22,-42,22,-36,-37,-38,-39,-40,22,22,22,-43,22,-42,22,22,22,22,]),'MULTIPLICACION':([3,10,12,32,33,35,37,38,40,41,43,44,46,48,50,52,54,55,56,57,58,59,60,61,64,78,85,86,88,100,103,],[24,-42,-44,-41,24,-42,24,-42,24,-42,24,-42,24,24,-42,24,24,24,-38,-39,-40,24,24,24,-43,24,-42,24,24,24,24,]),'DIVISION':([3,10,12,32,33,35,37,38,40,41,43,44,46,48,50,52,54,55,56,57,58,59,60,61,64,78,85,86,88,100,103,],[25,-42,-44,-41,25,-42,25,-42,25,-42,25,-42,25,25,-42,25,25,25,-38,-39,-40,25,25,25,-43,25,-42,25,25,25,25,]),'POTENCIA':([3,10,12,32,33,35,37,38,40,41,43,44,46,48,50,52,54,55,56,57,58,59,60,61,64,78,85,86,88,100,103,],[26,-42,-44,26,26,-42,26,-42,26,-42,26,-42,26,26,-42,26,26,26,26,26,26,26,26,26,-43,26,-42,26,26,26,26,]),'MAYORQUE':([3,10,12,32,33,35,37,38,40,41,43,44,46,48,50,52,54,55,56,57,58,59,60,61,64,78,85,86,88,100,103,],[27,-42,-44,-41,27,-42,27,-42,27,-42,27,-42,27,27,-42,27,-36,-37,-38,-39,-40,27,27,27,-43,27,-42,27,27,27,27,]),'MENORQUE':([3,10,12,32,33,35,37,38,40,41,43,44,46,48,50,52,54,55,56,57,58,59,60,61,64,78,85,86,88,100,103,],[28,-42,-44,-41,28,-42,28,-42,28,-42,28,-42,28,28,-42,28,-36,-37,-38,-39,-40,28,28,28,-43,28,-42,28,28,28,28,]),'IGUALES':([3,10,12,32,33,35,37,38,40,41,43,44,46,48,50,52,54,55,56,57,58,59,60,61,64,78,85,86,88,100,103,],[29,-42,-44,-41,29,-42,29,-42,29,-42,29,-42,29,29,-42,29,-36,-37,-38,-39,-40,29,29,29,-43,29,-42,29,29,29,29,]),'ID':([7,8,14,15,16,17,19,20,34,47,62,63,65,92,93,],[30,31,36,39,42,45,51,51,65,51,51,51,89,51,51,]),'PARENTESISDER':([10,12,32,33,54,55,56,57,58,59,60,61,64,],[-42,-44,-41,64,-36,-37,-38,-39,-40,-45,-46,-47,-43,]),'PYC':([10,12,32,35,36,37,38,39,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,84,85,86,87,88,90,97,99,106,107,108,109,],[-42,-44,-41,66,67,68,69,70,71,72,73,74,75,76,77,80,81,-13,-14,82,83,-36,-37,-38,-39,-40,-45,-46,-47,-43,94,-13,-15,95,96,98,104,105,110,111,112,113,]),'COMA':([10,12,32,50,51,54,55,56,57,58,59,60,61,64,78,79,],[-42,-44,-41,-13,-14,-36,-37,-38,-39,-40,-45,-46,-47,-43,92,93,]),'CORCHETEDER':([10,12,32,50,51,54,55,56,57,58,59,60,61,64,65,85,89,91,100,101,102,103,],[-42,-44,-41,-13,-14,-36,-37,-38,-39,-40,-45,-46,-47,-43,90,-13,97,99,106,107,108,109,]),'CORCHETEIZQ':([13,18,],[34,47,]),'IGUAL':([30,31,],[62,63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'sentencia':([0,1,],[2,21,]),'expresion':([0,1,9,11,14,15,16,17,19,20,22,23,24,25,26,27,28,29,47,62,63,92,93,],[3,3,32,33,37,40,43,46,48,52,54,55,56,57,58,59,60,61,78,86,88,100,103,]),'add':([0,1,],[4,4,]),'continue':([0,1,],[5,5,]),'pos':([0,1,],[6,6,]),'condicion':([0,1,9,11,14,15,16,17,19,20,22,23,24,25,26,27,28,29,47,62,63,92,93,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'valor':([19,20,47,62,63,92,93,],[49,53,79,84,87,101,102,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> sentencias sentencia','sentencias',2,'p_sentencias','parser.py',62),
  ('sentencias -> sentencia','sentencias',1,'p_sentencias','parser.py',63),
  ('sentencia -> expresion','sentencia',1,'p_sentencia_expr','parser.py',73),
  ('sentencia -> add','sentencia',1,'p_sentencia_expr','parser.py',74),
  ('sentencia -> continue','sentencia',1,'p_sentencia_expr','parser.py',75),
  ('sentencia -> pos','sentencia',1,'p_sentencia_expr','parser.py',76),
  ('sentencia -> DEF ID IGUAL valor PYC','sentencia',5,'p_sentencia_asignacion','parser.py',86),
  ('sentencia -> PUT ID IGUAL valor PYC','sentencia',5,'p_sentencia_cambio','parser.py',92),
  ('sentencia -> PUT ID IGUAL expresion PYC','sentencia',5,'p_sentencia_cambio','parser.py',93),
  ('add -> ADD CORCHETEIZQ ID CORCHETEDER PYC','add',5,'p_add','parser.py',105),
  ('add -> ADD CORCHETEIZQ ID ID CORCHETEDER PYC','add',6,'p_add','parser.py',106),
  ('add -> ADD CORCHETEIZQ ID INT CORCHETEDER PYC','add',6,'p_add','parser.py',107),
  ('valor -> INT','valor',1,'p_valor','parser.py',135),
  ('valor -> ID','valor',1,'p_valor','parser.py',136),
  ('valor -> expresion','valor',1,'p_valor','parser.py',137),
  ('continue -> CONTINUEUP INT PYC','continue',3,'p_continue','parser.py',146),
  ('continue -> CONTINUEUP ID PYC','continue',3,'p_continue','parser.py',147),
  ('continue -> CONTINUEUP expresion PYC','continue',3,'p_continue','parser.py',148),
  ('continue -> CONTINUEDOWN INT PYC','continue',3,'p_continue','parser.py',149),
  ('continue -> CONTINUEDOWN ID PYC','continue',3,'p_continue','parser.py',150),
  ('continue -> CONTINUEDOWN expresion PYC','continue',3,'p_continue','parser.py',151),
  ('continue -> CONTINUERIGHT INT PYC','continue',3,'p_continue','parser.py',152),
  ('continue -> CONTINUERIGHT ID PYC','continue',3,'p_continue','parser.py',153),
  ('continue -> CONTINUERIGHT expresion PYC','continue',3,'p_continue','parser.py',154),
  ('continue -> CONTINUELEFT INT PYC','continue',3,'p_continue','parser.py',155),
  ('continue -> CONTINUELEFT ID PYC','continue',3,'p_continue','parser.py',156),
  ('continue -> CONTINUELEFT expresion PYC','continue',3,'p_continue','parser.py',157),
  ('pos -> POS CORCHETEIZQ expresion COMA expresion CORCHETEDER PYC','pos',7,'p_pos','parser.py',173),
  ('pos -> POS CORCHETEIZQ valor COMA valor CORCHETEDER PYC','pos',7,'p_pos','parser.py',174),
  ('pos -> POS CORCHETEIZQ valor COMA expresion CORCHETEDER PYC','pos',7,'p_pos','parser.py',175),
  ('pos -> POS CORCHETEIZQ expresion COMA valor CORCHETEDER PYC','pos',7,'p_pos','parser.py',176),
  ('pos -> POSX expresion PYC','pos',3,'p_pos','parser.py',177),
  ('pos -> POSX valor PYC','pos',3,'p_pos','parser.py',178),
  ('pos -> POSY expresion PYC','pos',3,'p_pos','parser.py',179),
  ('pos -> POSY valor PYC','pos',3,'p_pos','parser.py',180),
  ('expresion -> expresion PLUS expresion','expresion',3,'p_expresion_op','parser.py',212),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_op','parser.py',213),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_expresion_op','parser.py',214),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion_op','parser.py',215),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_op','parser.py',216),
  ('expresion -> RESTA expresion','expresion',2,'p_expresion_menos','parser.py',244),
  ('expresion -> INT','expresion',1,'p_expresion_num','parser.py',250),
  ('expresion -> PARENTESISIZQ expresion PARENTESISDER','expresion',3,'p_factor_expr','parser.py',256),
  ('expresion -> condicion','expresion',1,'p_expresion_condicion','parser.py',262),
  ('condicion -> expresion MAYORQUE expresion','condicion',3,'p_condiciones','parser.py',267),
  ('condicion -> expresion MENORQUE expresion','condicion',3,'p_condiciones','parser.py',268),
  ('condicion -> expresion IGUALES expresion','condicion',3,'p_condiciones','parser.py',269),
]