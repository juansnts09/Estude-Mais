# EstudaMais – Assistente Inteligente de Estudos

Protótipo em Python de um agente educacional com RAG simplificado.

## Arquivos
- `main.py`: código do agente e interface no terminal.
- `mock_rag.json`: base de conhecimento personalizada.
- `memoria.json`: histórico criado automaticamente durante o uso.
- `test_main.py`: testes automatizados.
- `RELATORIO.md`: relatório do projeto.

## Requisitos
Python 3.8 ou superior. Não precisa instalar bibliotecas externas.

## Como executar
```bash
python main.py
```

## Como testar
```bash
python -m unittest -v
```

## Personalização
No `main.py`, altere `nome_estudante` e `serie` ao criar `AgenteDuvidas`.
Adicione novos documentos ao `mock_rag.json`, mantendo os campos `titulo`, `conteudo` e `palavras_chave`.

## Limitação
Este é um protótipo didático. O RAG usa correspondência simples de palavras-chave e não utiliza embeddings nem um modelo generativo externo.
