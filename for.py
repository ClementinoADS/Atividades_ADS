alunos = [
    {"nome": "Júlio", "nota": 8.5},
    {"nome": "Pablo", "nota": 4.0},
    {"nome": "Kaio", "nota": 7.0},
    {"nome": "João Lucas", "nota": 5.5}
]

print("Relatório de Notas")

#Range com len para navegar pelo indice da lista
for i in range(len(alunos)):
    aluno = alunos[i]
    status = "Aprovado" if aluno["nota"] >= 6 else "Reprovado"
    
    print(f"{i + 1}. {aluno['nome']}: {aluno['nota']} - {status}")

