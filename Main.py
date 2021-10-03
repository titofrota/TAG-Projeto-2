#################################################
# Universidade de Brasília - UnB                #
# Departamento de Ciência da Computação         #
# Teoria e Aplicação de Grafos - 2021/1         #
# Ítalo Frota - 18/0019279                      #
#################################################

from Initializer import assemble

def gale_sharpley(projects_graph, students_graph):
  assigned_students = []
  s_count = 1

  while (True):
    for student in students_graph:
      if (len(student["attempts"]) == 3):       # checks if student has tried all his attempts
        s_count += 1
        if (s_count == len(students_graph)): return projects_graph, students_graph    # stops when everyone was checked 

      for preference in student["preferences"]:
        if student not in assigned_students:      # checks if student wasnt assigned to a project
          if preference not in student["attempts"]: student["attempts"].append(preference)

          attempt = next(item for item in projects_graph if item["id"] == preference)     # gets the selected project

          if len(attempt["participants"]) != int(attempt["vacancies"]):     # checks if the project isnt full
            if((student["grade"] >= attempt["minimum_grade"]) and student not in assigned_students):        # checks if the student has the minimum grade
              attempt["participants"].append(student["id"])     # assigns the student as a participant
              assigned_students.append(student)             # inserts the student on the assigned students list



def main():
  with open("entradaProj2TAG.txt") as f:
    lines = f.read().strip().split("\n")

  projects_graph, students_graph = assemble(lines)

  # for student in students_graph:
  #   print(student)

  # for project in projects_graph:
  #   print(project)

  gale_sharpley(projects_graph, students_graph)

  # projects_graph[1]["participants"].append(students_graph[1])
  # if students_graph[1] in projects_graph[1]["participants"]: print(projects_graph[1])

  # a = next(item for item in projects_graph if item["id"] == "P35")
  # print(next(item for item in projects_graph if item["id"] == "P35")["participants"])

  for project in projects_graph:
    id = project["id"]
    participants = project["participants"]

    print(f"[{id}]: {participants}")

if __name__== "__main__" :
  main()