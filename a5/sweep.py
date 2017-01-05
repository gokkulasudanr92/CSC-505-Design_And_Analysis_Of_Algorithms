import sys

n = int(raw_input().strip())

class LineSegment(object):
	def __init__(self, points):
		if points[2] > points[0]:
			self.left = (points[0], points[1])
			self.right = (points[2], points[3])
		else:
			self.right = (points[0], points[1])
			self.left = (points[2], points[3])
		
	def __cmp__(self, other):
		return cmp(self.left[0], other.left[0])
	
def doIntersect(l1, l2):
	#slope of equation l1
	m1 = (l1.right[1] - l1.left[1]) / (l1.right[0] - l1.left[0])
	
	#slope of equation l2
	m2 = (l2.right[1] - l2.left[1]) / (l2.right[0] - l2.left[0])
	
	#Lines are parallel to each other so no intersection
	if m1 == m2:
		return False
	else:
		#Lines are not parallel but there is an intersection point
		#Find the intersection point and do a check for items
		
		x = (m1 * l1.left[0] - m2 * l2.left[0] + l2.left[1] - l1.left[1]) / (m1 - m2)
		y = m1 * x - m1 * l1.left[0] + l1.left[1]
		
		check = True
		
		if x < min(l1.left[0], l1.right[0]):
			check = False
		
		if x > max(l1.left[0], l1.right[0]):
			check = False
			
		if y < min(l1.left[1], l1.right[1]):
			check = False
			
		if y > max(l1.left[1], l1.right[1]):
			check = False
		
		if x < min(l2.left[0], l2.right[0]):
			check = False
		
		if x > max(l2.left[0], l2.right[0]):
			check = False
			
		if y < min(l2.left[1], l2.right[1]):
			check = False
			
		if y > max(l2.left[1], l2.right[1]):
			check = False
		
		""" if x == -95:
			print x, y, check """
		
		if check:
			return True
		else:
			return False
	
def calc_intersect(l1, l2):
	#slope of equation l1
	m1 = (l1.right[1] - l1.left[1]) / (l1.right[0] - l1.left[0])
	
	#slope of equation l2
	m2 = (l2.right[1] - l2.left[1]) / (l2.right[0] - l2.left[0])
	
	# m1 * x - m1 * l1.left[0] + l1.left[1] = m2 * x - m2 * l2.left[0] + l2.left[1]
	x = (m1 * l1.left[0] - m2 * l2.left[0] + l2.left[1] - l1.left[1]) / (m1 - m2)
	
	# y = m1 * x - m1 * x1 + y1
	y = m1 * x - m1 * l1.left[0] + l1.left[1]
	
	x =  '%.2f' % round(x, 2)
	y = '%.2f' % round(y, 2)
	return (x, y)
	
#List of line segments
lines = []
for i in range(n):
	points = map(float, raw_input().strip().split(' '))
	lines.append(LineSegment(points))
lines.sort()

""" for i in lines:
	print i.left, "   ", i.right """

pts = []
for i in range(n):
	pts.append((lines[i].left[0], lines[i].left[1], i))
	pts.append((lines[i].right[0], lines[i].right[1], i))
	
pts.sort(key = lambda x:x[1])
pts.sort(key = lambda x:x[0])

sweeped_lines = []
#intersecting line segments
intersect = []
intersect_event = []
#print onSegment(lines[0], (-21.0, -15.0))
line_remove = -1
for p in pts:
	#Left point event 
	if p[0] == lines[p[2]].left[0] and p[1] == lines[p[2]].left[1]:
		sweeped_lines.append((p[2], lines[p[2]]))
		
		#find segments above given left point
		l = len(sweeped_lines)
		seg_above = []
		seg_below = []
		
		for i in range(l):
			if sweeped_lines[i][1].left[1] >= lines[p[2]].left[1]:
				seg_above.append(sweeped_lines[i][0])
				
			if sweeped_lines[i][1].left[1] < lines[p[2]].left[1]:
				seg_below.append(sweeped_lines[i][0])
		
		#Write logic for finding intersecting lines
		for i in range(len(seg_above)):
			if doIntersect(lines[p[2]], lines[seg_above[i]]):
				t_1 = (p[2], seg_above[i]) in intersect
				t_2 = (seg_above[i], p[2]) in intersect
				if not t_1 and not t_2:
					intersect.append((p[2], seg_above[i]))
					intersect_event.append((True, seg_above[i], p[2]))
		
		for i in range(len(seg_below)):
			if doIntersect(lines[p[2]], lines[seg_below[i]]):
				t_1 = (p[2], seg_below[i]) in intersect
				t_2 = (seg_below[i], p[2]) in intersect
				if not t_1 and not t_2:
					intersect.append((p[2], seg_below[i]))
					intersect_event.append((True, p[2], seg_below[i]))
	
	#Right point event
	if p[0] == lines[p[2]].right[0] and p[1] == lines[p[2]].right[1]:
		#Write logic for finding intersecting lines
		l = len(sweeped_lines)
		seg_above = []
		seg_below = []
		
		for i in range(l):
			if sweeped_lines[i][1].left[1] >= lines[p[2]].left[1]:
				seg_above.append(sweeped_lines[i][0])
				
			if sweeped_lines[i][1].left[1] < lines[p[2]].left[1]:
				seg_below.append(sweeped_lines[i][0])
		
		for i in range(len(seg_above)):
			for j in range(len(seg_below)):
				if seg_above[i] != seg_below[j] and doIntersect(lines[seg_above[i]], lines[seg_below[j]]):
					t_1 = (seg_above[i], seg_below[j]) in intersect
					t_2 = (seg_below[j], seg_above[i]) in intersect
					if not t_1 and not t_2:
						intersect.append(seg_above[i], seg_below[j])
						intersect_event.append((True, seg_above[i], seg_below[j]))
		
		if len(intersect_event) == 0:			
			sweeped_lines.remove((p[2], lines[p[2]]))
		else:
			line_remove = p[2]
	
	#After intersecting it is possible for the next lines to intersect
	for ev in intersect_event:
		if ev[0]:
			l = len(sweeped_lines)
			#All lines above the 2nd line
			seg_l2 = []
			#All lines below the 1st line
			seg_l1 = []
		
			for i in range(l):
				if sweeped_lines[i][1].left[1] >= lines[ev[2]].left[1]:
					seg_l2.append(sweeped_lines[i][0])
				
				if sweeped_lines[i][1].left[1] < lines[ev[1]].left[1]:
					seg_l1.append(sweeped_lines[i][0])
				
			for i in range(len(seg_l2)):
				if doIntersect(lines[seg_l2[i]], lines[ev[2]]):
					t_1 = (ev[2], seg_l2[i]) in intersect
					t_2 = (seg_l2[i], ev[2]) in intersect
					if not t_1 and not t_2:
						intersect.append((seg_above[i], ev[2]))
		
			for i in range(len(seg_l1)):
				if doIntersect(lines[ev[1]], lines[seg_l1[i]]):
					t_1 = (ev[1], seg_l1[i]) in intersect
					t_2 = (seg_l1[i], ev[1]) in intersect
					if not t_1 and not t_2:
						intersect.append((ev[1], seg_l1[i]))
			
			intersect_event.remove(ev)
					
	if line_remove != -1:
		sweeped_lines.remove((line_remove, lines[line_remove]))
		line_remove = -1	
		
#Find the intersecting point:
res_array = []
for i in intersect:
	r = calc_intersect(lines[i[0]], lines[i[1]])
	res_array.append((float(r[0]), float(r[1])))

res_array.sort(key = lambda x:x[0])
for i in res_array:
	x = '%.2f' % round(i[0], 2)
	y = '%.2f' % round(i[1], 2)
	print x, y