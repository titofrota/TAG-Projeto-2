#################################################
# Universidade de Brasília - UnB                #
# Departamento de Ciência da Computação         #
# Teoria e Aplicação de Grafos - 2021/1         #
# Ítalo Frota - 18/0019279                      #
#################################################

from Initializer import assemble

        
def main():
  with open("entradaProj2TAG.txt") as f:
    lines = f.read().strip().split("\n")

  students_graph, projects_graph = assemble(lines)

  

  # for student in students_graph:
  #   print(student)

  # for project in projects_graph:
  #   print(project)


if __name__== "__main__" :
  main()