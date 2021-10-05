# Algoritmo de Gale-Shapley

# Teoria e Aplicação de Grafos - UnB - 2021/1
 - Ítalo Frota - 18/0019279 

O repositório contém o projeto 2 da disciplina de Teoria e Aplicação de Grafos ministrada na Universidade de Brasília no semestre 2021/1. 

*Considere para efeito deste projeto que uma determinada universidade oferece anualmente uma lista de cinquenta (50) projetos financiados e abertos a participação de alunos. Cada projeto é orientado e gerenciado por professores que estabelecem as quantidades mínima e máxima de alunos que podem ser aceitos em determinado projeto, bem como requisitos de histórico e tempo disponível que os alunos devem possuir para serem aceitos. Esses requisitos de histórico e tempo são pré-avaliados e cada aluno possui uma Nota agregada inteira de [3, 4, 5], sendo 3 indicando suficiente, 4 muito boa, e 5 excelente. Neste ano duzentos (200) alunos se candidataram aos projetos. O ideal é que o máximo de projetos sejam realizados, mas somente se o máximo de alunos qualificados tenham tido o interesse para tal. Para uma seleção impessoal e competitiva um algoritmo que realize um emparelhamento estável máximo deve ser implementado. Este projeto pede a elaboração, implementação e testes com a solução final de emparelhamento máximo estável para os dados fornecidos. Os alunos podem indicar no máximo três (3) preferências em ordem dos projetos.*

# Algoritmo
O algoritmo implementado foi baseado no pseudocódigo indicado na wikipedia (https://en.wikipedia.org/wiki/Gale–Shapley_algorithm), mas nesta versão, a comparação de preferência leva em conta a nota dos estudantes, que precisa atingir um mínimo e, nos casos de substituição, ser maior que a dos estudantes já alocados. Além disso, quando a nota mínima do projeto atual do estudante é menor do que a de outro projeto de sua preferência, e ele também atinge a nova nota, há a troca de projeto para que o estudante esteja no projeto com maior nota mínima.


# Como executar?
Basta executar no terminal:

    python3 Main.py

 
