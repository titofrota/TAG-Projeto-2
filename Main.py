#################################################
# Universidade de Brasília - UnB                #
# Departamento de Ciência da Computação         #
# Teoria e Aplicação de Grafos - 2021/1         #
# Ítalo Frota - 18/0019279                      #
#################################################

from Initializer import assemble

def gale_shapley(projects_graph, students_graph, assigned_students):
  s_count = 1
  iterations_count = 0

  while (True):
    if iterations_count <= 10 and iterations_count > 0:        # prints the first 10 iterations
      print(f"\nIteração nº {iterations_count}")
      for project in projects_graph:
        id = project["id"]
        participants = project["participants"]

        print(f"[{id}]: {participants}")

    for student in students_graph:
      if (len(student["attempts"]) == 3):       # checks if student has tried all his attempts
        s_count += 1
        if (s_count == (len(students_graph)*10)): return projects_graph, students_graph, assigned_students    # stops when everyone was checked 

      for preference in student["preferences"]:
        if preference not in student["attempts"]: student["attempts"].append(preference)      # inserts the current preference in the attempts
        attempt = next(item for item in projects_graph if item["id"] == preference)     # gets the selected project

        if student not in assigned_students:      # checks if student wasnt assigned to a project
          if len(attempt["participants"]) != int(attempt["vacancies"]):     # checks if the project isnt full
            if(student["grade"] >= attempt["minimum_grade"]):        # checks if the student has the minimum grade
              attempt["participants"].append(student["id"])     # assigns the student as a participant
              student["assigned_to"] = attempt["id"]
              assigned_students.append(student)             # inserts the student on the assigned students list
              # print(f"{student}\n")

          else:
            # substitution algorithm
            for participant in attempt["participants"]:
              selected_participant = next(item for item in students_graph if item["id"] == participant)     # gets the selected participant

              if(student["grade"] > selected_participant["grade"]) and (student != selected_participant):         # if the current student grade is greather than the selected participants grade
                assigned_students.remove(selected_participant)              # removes the selected participant
                attempt["participants"].remove(selected_participant["id"])

                attempt["participants"].append(student["id"])     # assigns the student as a participant
                assigned_students.append(student)             # inserts the student on the assigned students list
                break
        # substitution algorithm for already assigned students
        else:
          for proj in projects_graph:             # gets currently assigned project
            if proj["id"] in student["assigned_to"]:
              current_project = proj
              break

          if current_project != attempt:
            if (int(attempt["minimum_grade"]) > int(current_project["minimum_grade"])):       # checks if the minimum grade on the attempt is greater than the currently assigned
              if len(attempt["participants"]) == int(attempt["vacancies"]):           # checks if the attempt project is full
                # substitution algorithm
                for participant in attempt["participants"]:
                  selected_participant = next(item for item in students_graph if item["id"] == participant)     # gets the selected participant

                  if(student["grade"] > selected_participant["grade"]):         # if the current student grade is greather than the selected participants grade
                    assigned_students.remove(selected_participant)              # removes the selected participant
                    attempt["participants"].remove(selected_participant["id"])

                    attempt["participants"].append(student["id"])     # assigns the student as a participant
                    assigned_students.append(student)
                    break 

              else:                 # if the attempt project isnt full
                if student["id"] in current_project["participants"]:
                  current_project["participants"].remove(student["id"])
                  attempt["participants"].append(student["id"])
                  
    iterations_count += 1


def main():
  with open("entradaProj2TAG.txt") as f:
    lines = f.read().strip().split("\n")

  projects_without_maximum = []
  assigned_students = []
  students_without_project = []
  projects_graph, students_graph = assemble(lines)      # reads the input file
  gale_shapley(projects_graph, students_graph, assigned_students)

  # projects output
  print("\n\n\nOUTPUT FINAL:")
  for project in projects_graph:
    id = project["id"]
    participants = project["participants"]

    if len(participants) < int(project["vacancies"]):
      projects_without_maximum.append(project["id"])
    print(f"[{id}]: {participants}")

  # non assigned students output
  for student in students_graph:
    if student not in assigned_students:
      students_without_project.append(student["id"])

  print(f"\nProjetos que não atingiram a quantidade máxima de participantes:{projects_without_maximum}")
  print(f"\nAlunos sem projeto:{students_without_project}")


if __name__== "__main__" :
  main()



# References: https://www.vitoshacademy.com/python-algorithms-stable-matching-problem/, https://en.wikipedia.org/wiki/Gale–Shapley_algorithm