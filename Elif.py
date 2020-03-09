Year = input('To know your school level, please input the year you study: ')
Year = int(Year)
if Year < 2006:
	print('Before or during Elementary School')
elif Year >= 2006 and Year < 2009:
	print('Junior High School')
elif Year >= 2009 and Year < 2012:
	print('Senior High School')
elif Year >= 2012 and Year <= 2017:
	print('College')
else:
	print('Full Time Worker in the society')