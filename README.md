# Gerador de Contratos - Modelo Permuta

MVP simples em Streamlit para gerar contratos de **Permuta de Ativos** com cláusulas dinâmicas.

## 🚀 Como rodar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Deploy no Render
1. Suba este projeto em um repositório no GitHub.
2. No Render, crie um Web Service com Python 3.11.
3. Start Command:
   ```bash
   streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   ```
