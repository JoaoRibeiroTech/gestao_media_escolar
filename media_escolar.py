from time import sleep
from escola import Aluno
import os

aluno = Aluno()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_nota():
      try:
            quantidade_notas = int(input('Quantas notas deseja adicionar? '))
            for i in range(quantidade_notas):
                  while True:
                        try:
                              valor_nota = float(input(f'Digite o valor da {i+1}ª nota: '))
                              if aluno.inserir_nota(valor_nota):
                                    print(f"Nota {valor_nota} adicionada!")
                                    break
                              else:
                                    print("Nota inválida! Deve ser entre 0 e 10.")
                        except ValueError:
                                    print("Erro! Digite um número válido (ex: 8.5).")
      except ValueError:
        print('Erro! Digite um valor numérico inteiro para a quantidade.')    

def excluir_nota():     
      if not aluno.tem_notas():
            print('Não há notas para excluir!')
            return
      
      while True:
            print(f'As notas são:\n {aluno.get_notas()}')
            try:
                  apagar_nota = float(input('Digite a nota que deseja excluir: '))
                  if aluno.retirar_nota(apagar_nota):
                        print(f'Sucesso! A nota {apagar_nota} foi removida.')
                  else:
                        print(f'Erro: A nota {apagar_nota} não está na lista.')
            except ValueError:
                  print(f'Erro! A nota "{apagar_nota}" não foi encontrada ou a entrada é inválida. Tente novamente.')

            continuar = input('Deseja excluir outra nota? (S/N): ').upper()
            if continuar != 'S':
                  break    

def main():
    limpar_tela()
    print("--- SISTEMA DE GESTÃO ESCOLAR ---")
    aluno.coletar_dados()
    while True:
              try:
            
                  print('''
Menu de Opções:
1. Adicionar Nota
2. Excluir Nota
3. Ver Resultado Final
4. Sair''')
                  escolha = int(input('Escolha uma opção: '))
                  if escolha == 1:
                        adicionar_nota()
                  elif escolha == 2:
                        excluir_nota()
                  elif escolha == 3:
                        if not aluno.tem_notas():
                              print('Aviso: Adicione notas antes de ver o resultado!')
                        else:
                              aluno.exibir_resultado()
                              input("Pressione ENTER para continuar...")
                  elif escolha == 4:
                        print('Saindo...')
                        sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                  else:
                        print('Número não reconhecido! Tente novamente.')
              except ValueError:
                     print('Número não reconhecido! Tente novamente.')

if __name__ == "__main__":
    main()