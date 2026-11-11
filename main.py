import json
import re
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).parent
RAG_FILE = BASE_DIR / "mock_rag.json"
MEMORY_FILE = BASE_DIR / "memoria.json"

REGRAS_FIXAS = [
    "Responda em português do Brasil, com linguagem simples e respeitosa.",
    "Use o material recuperado do RAG como base para explicar os assuntos.",
    "Não invente informações quando o material não trouxer a resposta.",
    "Se não encontrar conteúdo relacionado, informe isso e peça um tema mais específico.",
    "Explique para ensinar, usando exemplos curtos quando forem úteis.",
    "Não solicite senhas, dados pessoais ou informações confidenciais."
]

def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9\s]", " ", texto)

def carregar_rag():
    with open(RAG_FILE, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def recuperar_documento(pergunta, documentos=None):
    """Recupera o documento mais relacionado usando correspondência simples de termos."""
    if documentos is None:
        documentos = carregar_rag()

    termos = set(normalizar(pergunta).split())
    termos = {t for t in termos if len(t) > 2}
    melhor_documento = None
    maior_pontuacao = 0

    for documento in documentos:
        texto = normalizar(
            documento["titulo"] + " " + documento["conteudo"] + " " +
            " ".join(documento.get("palavras_chave", []))
        )
        palavras_documento = set(texto.split())
        pontuacao = len(termos.intersection(palavras_documento))
        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_documento = documento

    if maior_pontuacao == 0:
        return None
    return melhor_documento

def carregar_memoria():
    if not MEMORY_FILE.exists():
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        return []

def salvar_memoria(historico):
    with open(MEMORY_FILE, "w", encoding="utf-8") as arquivo:
        json.dump(historico[-20:], arquivo, ensure_ascii=False, indent=2)

class AgenteDuvidas:
    def __init__(self, nome_estudante="Estudante", serie="Ensino Médio"):
        self.nome_estudante = nome_estudante
        self.serie = serie
        self.historico = carregar_memoria()

    def montar_prompt(self, pergunta, documento):
        contexto = (
            f"Título: {documento['titulo']}\n"
            f"Conteúdo: {documento['conteudo']}"
            if documento else "Nenhum conteúdo relevante foi encontrado no RAG."
        )
        prompt = f"""
Você é o EstudaMais, um assistente educacional.
Estudante: {self.nome_estudante}
Série: {self.serie}
Pergunta: {pergunta}
Contexto recuperado:
{contexto}

Regras fixas:
- {chr(10).join(REGRAS_FIXAS)}
- Diferencie informação do material e exemplos criados para explicar.
- Se o contexto não responder à pergunta, não complete com suposições.
"""
        return prompt.strip()

    def responder(self, pergunta):
        documento = recuperar_documento(pergunta)
        prompt = self.montar_prompt(pergunta, documento)

        if documento is None:
            resposta = (
                "Não encontrei esse tema no material do EstudaMais. "
                "Tente perguntar sobre Python, variáveis, listas, funções ou "
                "estruturas de repetição."
            )
        else:
            resposta = (
                f"Com base no material sobre **{documento['titulo']}**: "
                f"{documento['conteudo']}"
            )

        self.historico.append({
            "pergunta": pergunta,
            "resposta": resposta,
            "documento_utilizado": documento["titulo"] if documento else None
        })
        salvar_memoria(self.historico)
        return resposta

def iniciar_chat():
    agente = AgenteDuvidas()
    print("=== EstudaMais: Assistente de Estudos ===")
    print("Digite 'sair' para encerrar.\n")
    while True:
        pergunta = input("Você: ").strip()
        if pergunta.lower() in {"sair", "退出"}:
            print("EstudaMais: Bons estudos!")
            break
        if not pergunta:
            print("EstudaMais: Digite uma pergunta para começar.")
            continue
        print("EstudaMais:", agente.responder(pergunta), "\n")

if __name__ == "__main__":
    iniciar_chat()
