//梅花 (王安石)
//Plum blossom (Wang An Shi)

def genHex:
  choice = ["7" "8" "9" "a" "b" "c" "d" "e" "f"]
  result = "#"
  for 8:
    result = result + pick choice
  result

for 16 as i:
  layer:
    text "牆角數枝梅凌寒獨自開遙知不是雪為有暗香來".(i)
    floodfill genHex
//     rotate [0 0] (pick [0 15 30 45 60 75 90 105 120 135 150 165 180 195 210 225 240 255 270 285 300 315 330 345])