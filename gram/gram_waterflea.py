def genHex:
  choice = ["0" "4" "8" "b" "f"]
  result = "#"
  for 6:
    result = result + pick choice
  result = result + "11"

for 100 as i:
  layer:
    for 3:
      turnforward i i
    dogbone 5
    floodfill genHex