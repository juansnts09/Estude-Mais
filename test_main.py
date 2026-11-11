import unittest
import tempfile
from unittest.mock import patch
from main import recuperar_documento, AgenteDuvidas

DOCUMENTOS_TESTE = [
    {
        "titulo": "Python",
        "conteudo": "Python é uma linguagem de programação.",
        "palavras_chave": ["linguagem", "código"]
    },
    {
        "titulo": "Estruturas de repetição",
        "conteudo": "O for e o while repetem comandos.",
        "palavras_chave": ["laço", "loop", "for", "while"]
    }
]

class TesteRAG(unittest.TestCase):
    def test_recupera_documento_python(self):
        resultado = recuperar_documento("O que é Python?", DOCUMENTOS_TESTE)
        self.assertEqual(resultado["titulo"], "Python")

    def test_recupera_estruturas(self):
        resultado = recuperar_documento("Como funciona o while?", DOCUMENTOS_TESTE)
        self.assertEqual(resultado["titulo"], "Estruturas de repetição")

    def test_nao_encontra_tema_desconhecido(self):
        resultado = recuperar_documento("Quero aprender astronomia", DOCUMENTOS_TESTE)
        self.assertIsNone(resultado)

class TesteAgente(unittest.TestCase):
    def test_prompt_tem_regras_e_variaveis(self):
        agente = AgenteDuvidas(nome_estudante="Juan", serie="3ª série do Ensino Médio")
        documento = DOCUMENTOS_TESTE[0]
        prompt = agente.montar_prompt("O que é Python?", documento)
        self.assertIn("Juan", prompt)
        self.assertIn("3ª série do Ensino Médio", prompt)
        self.assertIn("Não invente informações", prompt)

if __name__ == "__main__":
    unittest.main()
