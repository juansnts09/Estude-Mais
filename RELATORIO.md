# Relatório – EstudaMais: Assistente Inteligente de Estudos

**Aluno:** Juan Pereira dos Santos  
**Turma:** 3ª série do Ensino Médio  
**Área:** Desenvolvimento de Sistemas  
**Projeto:** Personalização de um agente de Inteligência Artificial com RAG

## 1. Objetivo do projeto

O EstudaMais é um assistente de inteligência artificial criado para apoiar estudantes durante os estudos. Sua função é explicar conceitos de programação, responder dúvidas e ajudar o aluno a revisar conteúdos de forma simples e organizada.

Nesta versão, o agente foi direcionado aos conteúdos iniciais de Python. O projeto utiliza um RAG simplificado (Retrieval-Augmented Generation), que procura informações em uma pequena base de documentos antes de formular a resposta.

## 2. Especificações da IA

- **Nome:** EstudaMais.
- **Finalidade:** apoio educacional e esclarecimento de dúvidas.
- **Público-alvo:** estudantes do Ensino Médio, especialmente da área de Desenvolvimento de Sistemas.
- **Linguagem:** português do Brasil.
- **Tecnologia:** Python.
- **Base de conhecimento:** arquivo `mock_rag.json`.
- **Recuperação de informações:** comparação de palavras da pergunta com títulos, conteúdos e palavras-chave dos documentos.
- **Memória:** histórico simples das perguntas e respostas, salvo em `memoria.json`.
- **Personalização:** nome do estudante e série escolar são variáveis usadas na montagem do prompt.

## 3. Personalização do RAG e do prompt

A base RAG foi personalizada com cinco assuntos: Python, variáveis, estruturas de repetição, listas e funções. Cada documento possui título, conteúdo e palavras-chave para facilitar a recuperação.

O prompt interno recebe as variáveis `nome_estudante`, `serie`, `pergunta` e `contexto`. Assim, a explicação pode considerar o nível escolar do estudante e o conteúdo encontrado na base.

Também foram definidas regras fixas (invariáveis): responder em português, usar o material recuperado, não inventar informações, avisar quando não encontrar o assunto e proteger dados pessoais.

## 4. O que a IA deve fazer

- Explicar conteúdos de programação com linguagem simples.
- Recuperar informações relacionadas à pergunta na base RAG.
- Apresentar exemplos curtos para facilitar o entendimento.
- Considerar o nível escolar informado.
- Manter um histórico básico das interações.
- Avisar quando não houver material suficiente para responder.

## 5. O que a IA não deve fazer

- Inventar conteúdos ou apresentar suposições como fatos.
- Fingir que consultou fontes que não estão na base.
- Responder como especialista sobre assuntos fora de sua finalidade.
- Solicitar senhas ou dados pessoais desnecessários.
- Substituir o professor ou garantir que toda resposta esteja correta.
- Afirmar que possui acesso à internet ou a uma IA externa: esta versão é um protótipo local com recuperação por palavras-chave.

## 6. Onde pode ser aplicada

O EstudaMais pode ser usado em escolas, cursos técnicos, plataformas de ensino e ambientes virtuais de aprendizagem. Também pode apoiar revisões antes de provas, explicar conceitos básicos de programação e indicar conteúdos que o estudante precisa estudar novamente.

Em versões futuras, poderá receber materiais da escola, separar os conteúdos por disciplina e utilizar um modelo de linguagem conectado a uma base vetorial mais completa.

## 7. Testes e correções

Foram preparados testes automatizados para verificar se:
1. Uma pergunta sobre Python recupera o documento correto.
2. Uma pergunta sobre `while` recupera estruturas de repetição.
3. Um tema que não existe na base retorna resultado vazio.
4. O prompt inclui o nome, a série e as regras fixas.

Para executar os testes, use:

```bash
python -m unittest -v
```

Para iniciar o agente, use:

```bash
python main.py
```

**Observação:** os testes automatizados verificam a recuperação e a montagem do prompt. A resposta desta versão é produzida por regras simples, sem conexão com um modelo de linguagem externo.

## 8. Conclusão

O desenvolvimento do EstudaMais mostrou como um agente pode ser personalizado de acordo com uma finalidade específica. O uso do RAG permite consultar uma base de conhecimento antes de responder, enquanto as variáveis e regras do prompt ajudam a manter as respostas adequadas ao estudante. O protótipo ainda é simples, mas demonstra uma aplicação prática de Python e inteligência artificial na educação.
