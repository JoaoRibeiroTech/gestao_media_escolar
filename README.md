# 🎓 Sistema de Gestão de Médias Escolares

Este é um projeto desenvolvido em Python que simula um sistema de gestão acadêmica. O foco principal é a aplicação de conceitos de **Programação Orientada a Objetos (POO)** para o gerenciamento de alunos, notas e cálculo automático de desempenho.

---

## 📂 Estrutura do Projeto

O projeto foi modularizado em dois arquivos principais para garantir a separação de responsabilidades:

* **`escola.py`**: Contém a definição da classe `Aluno`, responsável por armazenar os dados e processar as regras de negócio.
* **`media_escolar.py`**: Script de execução que gerencia a interface de usuário via terminal e a interação com o sistema.

---

## 🚀 Funcionalidades

O sistema oferece um fluxo completo de gerenciamento:

* **Cadastro de Aluno**: Coleta o nome e a matrícula do estudante com validação de entradas.
* **Gestão de Notas**:
    * Adição múltipla de notas com verificação de intervalo (0 a 10).
    * Exclusão de notas específicas caso haja erro de digitação.
* **Cálculo Automático**: O sistema calcula a média aritmética em tempo real.
* **Resultado Final**: Exibe um painel formatado com o status do aluno:
    * **Aprovado(a)**: Média $\ge 7.0$.
    * **Reprovado(a)**: Média $< 7.0$.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Python 3**: Linguagem base do projeto.
* **Orientação a Objetos**: Uso de classes, métodos, atributos privados e encapsulamento.
* **Tratamento de Exceções**: Uso de `try/except` para prevenir erros de entrada do usuário e garantir a estabilidade do programa.
* **Modularização**: Separação da lógica de backend e frontend (CLI).

---

## 💻 Como Executar

1.  Certifique-se de ter o Python instalado.
2.  Mantenha os arquivos `escola.py` e `media_escolar.py` no mesmo diretório.
3.  Abra o terminal na pasta do projeto e execute:
    ```bash
    python media_escolar.py
    ```

---
