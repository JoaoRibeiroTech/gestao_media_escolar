class Aluno:
    def __init__(self, nome='', matricula=0):
        self._nome = nome
        self._matricula = matricula
        self._notas = []

    def __str__(self):
        return f"Nome: {self._nome}, Matrícula: {self._matricula}, Média: {self.calcular_media():.1f}"
    
    def coletar_dados(self):
        self._nome = input('Digite o nome do aluno: ').strip()
        while True:
            try:
                self._matricula = int(input('Digite a matrícula do aluno: '))
                if self._matricula <= 0:
                    print('A matrícula deve ser um número positivo.')
                    continue
                break
            except ValueError:
                print('Matrícula inválida! Deve ser um número inteiro.')

    def inserir_nota(self, nota):
        if 0 <= nota <= 10:
            self._notas.append(nota)
            return True
        return False

    def retirar_nota(self, nota):
        if nota in self._notas:
            self._notas.remove(nota)
            return True
        return False

    def tem_notas(self):
        return len(self._notas) > 0

    def get_notas(self):
        return self._notas

    def calcular_media(self):
        if not self._notas:
            return 0.0
        return sum(self._notas) / len(self._notas)

    def exibir_resultado(self):
        media = self.calcular_media()
        status = "Aprovado(a)" if media >= 7 else "Reprovado(a)"
        print("-" * 30)
        print(f"Aluno: {self._nome}")
        print(f"Matrícula: {self._matricula}")
        print(f"Média Final: {media:.1f}")
        print(f"Status: {status}")
        print("-" * 30)