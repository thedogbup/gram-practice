def genHex:
  choice = ["0" "4" "8" "b" "f"]
  result = "#"
  for 8:
    result = result + pick choice
  result

forward 10
turn 120
repeat 3

i = 1
copypaste 338:
    translate i/10 i/10
    rotate [0 0] i
    fillcolor genHex
    i = i + 1
