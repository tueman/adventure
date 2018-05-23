import math

def TriangleArea():
   try:
       b = float(input('Input base.'))
       h = float(input('Input height.'))
       Area = round(b * h / 2, 4)
       print('Area =', Area)
   except ValueError:
       print('Error: Input was not a number.')

def Rectangle():   # also applies to parallelogram
    try:
        l = float(input('Input length.'))
        w = float(input('Input width.'))
        Perimeter = round((l * 2) + (w * 2), 4)
        Area = round(l * w, 4)
        print('Perimeter =', Perimeter, '\nArea =', Area)
    except ValueError:
        print('Error: Input was not a number.')

def BoxVolume():
   try:
       l = float(input('Input length.'))
       w = float(input('Input width.'))
       h = float(input('Input height.'))
       Volume = round(l * w * h, 4)
       print('Volume =', Volume)
   except ValueError:
       print('Error: Input was not a number.')

def Square():
    try:
        l = float(input('Input length.'))
        Perimeter = round(l * 4, 4)
        Area = round(l ** 2, 4)
        CubeSurface = round((l ** 2) * 6, 4)
        CubeVolume = round(l ** 3, 4)
        print('Perimeter =', Perimeter, '\nArea =', Area, '\nCube Surface Area =', CubeSurface, '\nCube Volume =',
              CubeVolume)
    except ValueError:
        print('Error: Input was not a number.')

def Circle():   # asks for radius
    try:
        r = float(input('Input radius.'))
        Circumference = round(r * 2 * math.pi, 4)
        Area = round((r ** 2) * math.pi, 4)
        SphereSurface = round((r ** 2) * 4 * math.pi, 4)
        SphereVolume = round((r ** 3) * 4 / 3 * math.pi, 4)
        print('Circumference =', Circumference, '\nArea =', Area, '\nSphere Surface Area =', SphereSurface,
              '\nSphere Volume =', SphereVolume)
    except ValueError:
        print('Error:Input was not a number.')
