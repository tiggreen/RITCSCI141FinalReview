#Author @tiggreen

class Course():
	__slots__ = ('name', 'start_time', 'stop_time')

def mkCourse(n, starttime, stoptime):
	c = Course()
	c.name = n
	c.start_time = starttime
	c.stop_time = stoptime
	return c

def readCourse(file):
	retList = []
	for line in open(file): 
		fields = line.split()
		course = mkCourse(fields[0], int(fields[1]), int(fields[2]))
		retList.append(course)
	return retList

#Pre-condition: The list of input courses must be ordered by end time
def greedySchedule(courses):
	schedule = list()
	courses = courses[:]
	while len(courses) > 0:
		selcourse = courses.pop(0)
		schedule.append(selcourse)
		elected = list()
		for course in courses:
			# Check for conflict
			if course.start >= selcourse.stop_time:
				elected.append(course)
		courses = elected
	return schedule
