import re

def assemble(lines):
  projects_graph =[]            # initializes the projects graph
  students_graph = []           # initializes the students graph

  for line in lines:
    if line != "" and "//" not in line:         # checks if the line isnt a comment or empty
      if not "A" in line:       # checks if the line doesnt contains a student
        subject = re.search("(\w+), (\w), (\w)", line)      # splits the project data
        project_id = subject.group(1); vacancies = subject.group(2); minimum_grade = subject.group(3) # gets the project data

        project = {"id": project_id, "vacancies": vacancies, "minimum_grade": minimum_grade, "participants": []}        # assigns the data
        
        projects_graph.append(project)
      
      else:
        subject = re.search("\((\w+)\):\((\w+), (\w+), (\w+)\)(|\ )\((\w+)\)", line)        # splits the student data
        student_id = subject.group(1); preferences = [subject.group(2), subject.group(3), subject.group(4)]; grade = subject.group(6)       # gets the project data

        student = {"id": student_id, "preferences": preferences, "grade": grade, "attempts": []}        # assigns the data

        students_graph.append(student)

  return projects_graph, students_graph