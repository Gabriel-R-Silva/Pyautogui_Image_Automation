import automated
import sys
from automated import find_image

automated.start_system('C:\\Windows\\System32\\calc.exe')

find_image(r'image\calculator\2.png', click=True)

find_image(r'image\calculator\+.png', click=True)

find_image(r'image\calculator\2.png', click=True)

find_image(r'image\calculator\=.png', click=True)

#result is 1+1 = 2 at this point the error will occur
find_image(r'image\calculator\correct_result.png')

find_image(r'image\calculator\exit.png', click=True)

sys.exit(0)