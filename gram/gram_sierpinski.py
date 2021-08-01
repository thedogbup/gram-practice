def base size:
  newstroke [0 0]
  for 3:
    forward 2*size
    right 120
  newstroke this.rt
  for 3:
    forward 2*size
    right 120
  newstroke this.lb
  for 3:
    forward 2*size
    right 120

def clone1 i:
  first = layer:
    base i
  layer:
    base i
    translate 4*i 0
  layer:
    base i
    translate 0 neg(2*i*sqrt(3))
  
clone1 1