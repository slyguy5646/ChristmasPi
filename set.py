#COLOR DEFENITIONS GRB
off = (0, 0, 0)
blue = (0, 0, 255)
green = (255, 0, 0)
red = (0, 255, 0)

effectColor = [off]
effectColorString = ['off']
currentEffectString = ['off']
status = ['off']


def setColor(color):
   effectColor.clear()
   effectColor.append(color)
   if color == red:
      effectColorString.clear()
      effectColorString.append('red')
   elif color == green:
      effectColorString.clear()
      effectColorString.append('green')
   elif color == blue:
      effectColorString.clear()
      effectColorString.append('blue')
   elif color == off:
      effectColorString.clear()
      effectColorString.append('none')
   else:
      effectColorString.clear()
      effectColorString.append('a color')