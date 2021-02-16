import machine
import network
import math
import neopixel

def HSV_to_RGB(h, s, v):
    i = math.floor(h*6)
    f = (h*6) -i
    p = v*(1-s)
    q = v*(1-f*s)
    t = v*(1-(1-f)*s)
    rem = i%6

    if rem == 0: r = v; g = t; b = p
    if rem == 1: r = q; g = v; b = p
    if rem == 2: r = p; g = v; b = t
    if rem == 3: r = p; g = q; b = v
    if rem == 4: r = t; g = p; b = v
    if rem == 5: r = v; g = p; b = q

    return (round(r*255), round(g*255), round(b*255))

