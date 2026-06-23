"""
Headless replacement for simple Turtle commands that writes an SVG file.
This avoids the `turtle`/Tk dependency so the script can run on systems
without Tcl/Tk. It implements minimal `forward()` and `left()` functions
and writes `fractal.svg` to the current directory.
"""

import math

_x, _y = 100.0, 250.0
_angle = 0.0  # degrees, 0 = right
_segments = []

def forward(dist):
	global _x, _y
	rad = math.radians(_angle)
	nx = _x + dist * math.cos(rad)
	ny = _y - dist * math.sin(rad)
	_segments.append(((_x, _y), (nx, ny)))
	_x, _y = nx, ny

def left(deg):
	global _angle
	_angle = (_angle + deg) % 360

def right(deg):
	"""Rotate clockwise by deg degrees (convenience wrapper)."""
	global _angle
	_angle = (_angle - deg) % 360

def backward(dist):
	"""Move backwards by dist (draws a segment)."""
	# reuse forward with a negative distance
	forward(-dist)

def write_svg(path, width=500, height=500):
	parts = []
	parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
	parts.append('<rect width="100%" height="100%" fill="white"/>')
	for (x1, y1), (x2, y2) in _segments:
		parts.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="black" stroke-width="2" />')
	parts.append('</svg>')
	with open(path, 'w') as f:
		f.write('\n'.join(parts))


def tree(length):

    if length < 5:
        return

    forward(length)

    left(30)
    tree(length * 0.7)

    right(60)
    tree(length * 0.7)

    left(30)
    backward(length)

    
tree(100)
write_svg('fractal.svg')
print('Wrote my.svg')