# 🧾 Automação de Chamados no 1746 com Selenium

Este script automatiza o envio de chamados de **fiscalização por perturbação do sossego** no portal [https://www.1746.rio](https://www.1746.rio), utilizando Python e Selenium.

---

## 📦 Requisitos

- Python 3.7 ou superior
- Google Chrome instalado
- ChromeDriver (gerenciado automaticamente via `webdriver-manager`)

---

## 📁 Estrutura de Arquivos

```
prefeitura1746/
├── main.py           # Script principal
├── auth.txt          # Contém login, senha e telefone
├── inputs.txt        # Descrições aleatórias do problema
├── outputs.txt       # Log com protocolos enviados
├── README.md         # Este arquivo
```

---

## 🧰 Instalação de Dependências

No terminal (cmd, PowerShell ou terminal Linux/macOS):

```bash
pip install selenium webdriver-manager
```

---

## 📝 Formato do arquivo `auth.txt`

Deve conter **três linhas**, nesta ordem:

```
seu_email@exemplo.com
suaSenhaSegura123
21999999999
```

---

## 📝 Formato do arquivo `inputs.txt`

Inclua pelo menos **três frases diferentes** descrevendo a ocorrência, por exemplo:

```
Música alta e aglomeração frequente no local.
Clientes gritando na porta do estabelecimento.
Perturbação sonora constante com som automotivo.
```

O script escolhe uma aleatoriamente em cada execução.

---

## ▶️ Executando o Script

Navegue até a pasta do projeto e execute:

```bash
python main.py
```

O que o script faz:

1. Abre o site do 1746
2. Seleciona o serviço "Fiscalização de Perturbação do Sossego"
3. Faz login com seu e-mail/senha
4. Preenche os campos do formulário
5. Envia a solicitação
6. Salva o número do protocolo em `outputs.txt`

---

## 📤 Exemplo de saída no `outputs.txt`

```
Protocolo: 20254119 - seu_email@exemplo.com
```

---

## 🛟 Dicas e Considerações

- Mantenha o navegador **visível em tela** durante a execução para evitar erros de clique (evite minimizar).
- O site do 1746 pode mudar — se isso acontecer, os seletores `XPATH` podem precisar de atualização.
- Use `time.sleep()` maior no final se quiser acompanhar visualmente.

---

## ✅ Melhorias Futuras

- Executar em modo headless (sem abrir o navegador)
- Agendamento automático com `cron` ou `task scheduler`
- Captura de erros e prints de falha

---

Feito com ❤️ por Fabiano Martins Pereira
