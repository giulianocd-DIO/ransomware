# 📚 Guia Completo: Enviando seu Projeto Ransomware para GitHub
## Para Iniciantes - Passo a Passo Visual

---

## 🎯 Objetivo Final

Ao final deste guia, você terá seu projeto no GitHub com a seguinte estrutura:

```
seu_usuario/Ransomware/
├── 📄 README.md
├── 📄 LICENSE
├── 📁 scripts/
│   ├── Ransomware.py
│   └── Descriptografar.py
├── 📁 docs/
│   ├── Medidas_de_Defesa_Ransomware.md
│   └── GUIA_GITHUB_INICIANTE.md
├── 📁 test_files/
│   ├── senhas.txt
│   └── Dados_sensiveis.txt
└── 📁 images/
    ├── screenshot_criptografia.png
    ├── screenshot_descriptografia.png
    └── diagrama_ransomware.png
```

---

## ⚙️ PARTE 1: Preparação Inicial (5 minutos)

### Passo 1.1: Verificar se Git está instalado

Abra o **Terminal** (Linux/Mac) ou **Prompt de Comando** (Windows) e digite:

```bash
git --version
```

**Resultado esperado:**
```
git version 2.40.0
```

Se não aparecer nada, [baixe Git aqui](https://git-scm.com/downloads)

### Passo 1.2: Configurar sua identidade no Git

Isso é importante para que seus commits tenham seu nome!

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu_email@gmail.com"
```

**Exemplo:**
```bash
git config --global user.name "Maria Santos"
git config --global user.email "maria.santos@gmail.com"
```

### Passo 1.3: Verificar a configuração

```bash
git config --global --list
```

Você deve ver algo como:
```
user.name=Maria Santos
user.email=maria.santos@gmail.com
```

---

## 📁 PARTE 2: Organizar Arquivos Localmente (10 minutos)

### Passo 2.1: Criar a estrutura de pastas

Abra o **Explorador de Arquivos** (Windows) ou **Finder** (Mac) e crie a seguinte estrutura:

```
Ransomware/
├── scripts/
├── docs/
├── test_files/
└── images/
```

**Como criar:**

**Windows:**
1. Clique com botão direito na pasta `Ransomware`
2. Selecione "Nova Pasta"
3. Digite `scripts`
4. Repita para `docs`, `test_files` e `images`

**Linux/Mac:**
```bash
cd ~/Ransomware
mkdir scripts docs test_files images
```

### Passo 2.2: Mover os scripts Python

Mova os seguintes arquivos para a pasta `scripts/`:

- `Ransomware.py`
- `Descriptografar.py`

**Resultado:**
```
Ransomware/
└── scripts/
    ├── Ransomware.py
    └── Descriptografar.py
```

### Passo 2.3: Mover os arquivos de teste

Mova os seguintes arquivos para a pasta `test_files/`:

- `senhas.txt`
- `Dados_sensiveis.txt`

**Resultado:**
```
Ransomware/
└── test_files/
    ├── senhas.txt
    └── Dados_sensiveis.txt
```

### Passo 2.4: Mover a documentação

Mova os seguintes arquivos para a pasta `docs/`:

- `README.md`
- `Medidas_de_Defesa_Ransomware.md`
- `GUIA_GITHUB_INICIANTE.md`

**Resultado:**
```
Ransomware/
└── docs/
    ├── README.md
    ├── Medidas_de_Defesa_Ransomware.md
    └── GUIA_GITHUB_INICIANTE.md
```

### Passo 2.5: Adicionar imagens (opcional)

Se tiver capturas de tela do projeto funcionando, coloque na pasta `images/`:

```
Ransomware/
└── images/
    ├── screenshot_criptografia.png
    ├── screenshot_descriptografia.png
    └── diagrama_ransomware.png
```

### Passo 2.6: Criar arquivo .gitignore

Este arquivo diz ao Git quais arquivos **NÃO** enviar para o GitHub.

Crie um arquivo chamado `.gitignore` na raiz da pasta `Ransomware/`:

**Conteúdo do .gitignore:**
```
# Arquivos de chave de criptografia
*.key
chave.key

# Arquivos de mensagem de resgate
LEIA ISSO.txt
LEIA_ISSO.txt

# Arquivos de log
log.txt
log_*.txt
*.log

# Arquivos de cache Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Ambiente virtual
venv/
env/
ENV/

# Arquivos do sistema
.DS_Store
Thumbs.db

# Arquivos de IDE
.vscode/
.idea/
*.swp
*.swo

# Arquivos criptografados
test_files/*.txt.encrypted
```

### Passo 2.7: Criar arquivo LICENSE

Crie um arquivo chamado `LICENSE` na raiz da pasta `Ransomware/`:

**Conteúdo (Licença MIT):**
```
MIT License

Copyright (c) 2025 Seu Nome

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Estrutura Final

Sua pasta `Ransomware/` deve ficar assim:

```
Ransomware/
├── scripts/
│   ├── Ransomware.py
│   └── Descriptografar.py
├── docs/
│   ├── README.md
│   ├── Medidas_de_Defesa_Ransomware.md
│   └── GUIA_GITHUB_INICIANTE.md
├── test_files/
│   ├── senhas.txt
│   └── Dados_sensiveis.txt
├── images/
│   ├── screenshot_criptografia.png
│   ├── screenshot_descriptografia.png
│   └── diagrama_ransomware.png
├── .gitignore
└── LICENSE
```

---

## 🌐 PARTE 3: Criar Repositório no GitHub (5 minutos)

### Passo 3.1: Acessar GitHub

1. Abra seu navegador
2. Vá para [https://github.com](https://github.com)
3. Se não tiver conta, clique em **"Sign up"** para criar uma

### Passo 3.2: Fazer login

1. Clique em **"Sign in"**
2. Digite seu **username** e **senha**
3. Clique em **"Sign in"**

### Passo 3.3: Criar novo repositório

1. Clique no ícone **"+"** no canto superior direito
2. Selecione **"New repository"**

### Passo 3.4: Configurar repositório

Preencha os campos conforme indicado:

| Campo | Valor |
|-------|-------|
| **Repository name** | `Ransomware` |
| **Description** | `Projeto Educacional: Ransomware Simulado em Python para Estudo de Cibersegurança` |
| **Visibility** | `Public` (para compartilhar) ou `Private` (apenas você) |
| **Initialize this repository with** | `Deixe vazio` |

**Imagem do formulário:**
```
┌─────────────────────────────────────────────────────┐
│ Create a new repository                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Repository name *                                   │
│ [Ransomware                                   ]     │
│                                                     │
│ Description                                         │
│ [Projeto Educacional: Ransomware Simulado...  ]     │
│                                                     │
│ ○ Public    ● Private                              │
│                                                     │
│ ☐ Initialize this repository with a README        │
│ ☐ Add .gitignore                                   │
│ ☐ Choose a license                                 │
│                                                     │
│                              [Create repository]   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Passo 3.5: Criar repositório

Clique em **"Create repository"**

**Resultado:** Você verá uma página com instruções e um URL como:
```
https://github.com/seu_usuario/Ransomware.git
```

---

## 💻 PARTE 4: Enviar Arquivos para GitHub (10 minutos)

### Passo 4.1: Abrir Terminal na pasta do projeto

**Windows (PowerShell):**
1. Abra a pasta `Ransomware` no Explorador
2. Clique na barra de endereço
3. Digite `powershell`
4. Pressione **Enter**

**Linux/Mac:**
```bash
cd ~/Ransomware
```

### Passo 4.2: Inicializar Git no projeto

```bash
git init
```

**Resultado esperado:**
```
Initialized empty Git repository in /home/usuario/Ransomware/.git/
```

### Passo 4.3: Adicionar todos os arquivos

```bash
git add .
```

Este comando adiciona **todos** os arquivos da pasta (exceto os no `.gitignore`)

### Passo 4.4: Verificar o que será enviado

```bash
git status
```

**Resultado esperado:**
```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   LICENSE
        new file:   docs/GUIA_GITHUB_INICIANTE.md
        new file:   docs/Medidas_de_Defesa_Ransomware.md
        new file:   docs/README.md
        new file:   images/screenshot_criptografia.png
        new file:   scripts/Ransomware.py
        new file:   scripts/Descriptografar.py
        new file:   test_files/senhas.txt
        new file:   test_files/Dados_sensiveis.txt
```

### Passo 4.5: Fazer o primeiro commit

Um commit é como um "snapshot" do seu projeto:

```bash
git commit -m "Projeto inicial: Ransomware Simulado para fins educacionais"
```

**Resultado esperado:**
```
[master (root-commit) abc1234] Projeto inicial: Ransomware Simulado para fins educacionais
 10 files changed, 2500 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 LICENSE
 ...
```

### Passo 4.6: Adicionar repositório remoto

Este é o link para o GitHub:

```bash
git remote add origin https://github.com/seu_usuario/Ransomware.git
```

**Substitua `seu_usuario` pelo seu username do GitHub!**

### Passo 4.7: Verificar conexão

```bash
git remote -v
```

**Resultado esperado:**
```
origin  https://github.com/seu_usuario/Ransomware.git (fetch)
origin  https://github.com/seu_usuario/Ransomware.git (push)
```

### Passo 4.8: Enviar arquivos para GitHub

```bash
git push -u origin master
```

**Na primeira vez, você será solicitado a autenticar. Veja a próxima seção!**

---

## 🔐 PARTE 5: Autenticação no GitHub (5 minutos)

### Opção A: Usar Token de Acesso Pessoal (Recomendado)

#### Passo 5A.1: Gerar Token no GitHub

1. Vá para [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Clique em **"Generate new token"**
3. Dê um nome: `Git CLI Token`
4. Selecione os escopos:
   - ✅ `repo` (acesso completo ao repositório)
   - ✅ `read:user` (ler informações do usuário)
5. Clique em **"Generate token"**
6. **Copie o token** (você não verá novamente!)

#### Passo 5A.2: Usar o Token

Quando o Git pedir senha, **cole o token** que você copiou:

```
Username for 'https://github.com': seu_usuario
Password for 'https://seu_usuario@github.com': [cole o token aqui]
```

### Opção B: Usar SSH (Mais Seguro)

#### Passo 5B.1: Gerar chave SSH

```bash
ssh-keygen -t ed25519 -C "seu_email@gmail.com"
```

Pressione **Enter** para todas as perguntas (deixar padrão)

#### Passo 5B.2: Adicionar chave ao GitHub

**Linux/Mac:**
```bash
cat ~/.ssh/id_ed25519.pub
```

**Windows (PowerShell):**
```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
```

Copie a saída e vá para [https://github.com/settings/keys](https://github.com/settings/keys)

1. Clique em **"New SSH key"**
2. Cole a chave
3. Clique em **"Add SSH key"**

#### Passo 5B.3: Usar SSH no Git

```bash
git remote set-url origin git@github.com:seu_usuario/Ransomware.git
```

---

## ✅ PARTE 6: Verificar no GitHub (2 minutos)

### Passo 6.1: Acessar seu repositório

1. Vá para [https://github.com/seu_usuario/Ransomware](https://github.com/seu_usuario/Ransomware)
2. Você deve ver todos os seus arquivos!

### Passo 6.2: Verificar a estrutura

Você deve ver:

```
Ransomware/
├── scripts/
├── docs/
├── test_files/
├── images/
├── .gitignore
├── LICENSE
└── README.md (exibido automaticamente)
```

### Passo 6.3: Verificar o README

O arquivo `docs/README.md` deve estar visível na página principal

---

## 🔄 PARTE 7: Atualizações Futuras (Sempre que fizer mudanças)

### Passo 7.1: Fazer mudanças nos arquivos

Edite seus scripts ou documentação normalmente

### Passo 7.2: Verificar mudanças

```bash
git status
```

### Passo 7.3: Adicionar mudanças

```bash
git add .
```

### Passo 7.4: Fazer commit

```bash
git commit -m "Descrição do que foi alterado"
```

**Exemplos de boas mensagens:**
```bash
git commit -m "Adicionar tratamento de erro no Ransomware.py"
git commit -m "Atualizar documentação de defesa"
git commit -m "Adicionar novas screenshots"
git commit -m "Corrigir bug na descriptografia"
```

### Passo 7.5: Enviar para GitHub

```bash
git push origin master
```

---

## 🆘 Solução de Problemas Comuns

### Problema 1: "fatal: not a git repository"

**Solução:**
```bash
git init
```

### Problema 2: "error: remote origin already exists"

**Solução:**
```bash
git remote remove origin
git remote add origin https://github.com/seu_usuario/Ransomware.git
```

### Problema 3: "Permission denied (publickey)"

**Solução:** Use HTTPS em vez de SSH
```bash
git remote set-url origin https://github.com/seu_usuario/Ransomware.git
```

### Problema 4: "fatal: could not read Username"

**Solução:** Use um token de acesso pessoal em vez de senha

### Problema 5: Arquivo grande não pode ser enviado

**Solução:** Adicione ao `.gitignore` e remova do Git
```bash
echo "arquivo_grande.bin" >> .gitignore
git rm --cached arquivo_grande.bin
git add .gitignore
git commit -m "Remover arquivo grande"
git push
```

### Problema 6: "Updates were rejected because the remote contains work that you do not have locally"

**Solução:**
```bash
git pull origin master --allow-unrelated-histories
git push origin master
```

---

## 📋 Checklist Final

Antes de considerar seu projeto completo, verifique:

- ✅ Repositório criado no GitHub
- ✅ Todos os scripts estão em `scripts/`
- ✅ Toda documentação está em `docs/`
- ✅ Arquivos de teste estão em `test_files/`
- ✅ Imagens estão em `images/`
- ✅ `.gitignore` está configurado
- ✅ `LICENSE` está presente
- ✅ `README.md` está visível na página principal
- ✅ Primeiro commit foi feito
- ✅ Arquivos foram enviados com `git push`
- ✅ Repositório é acessível em GitHub

---

## 🎓 Próximos Passos

Agora que seu projeto está no GitHub, você pode:

1. **Adicionar Tópicos:** Vá para Settings > Topics
   - Adicione: `python`, `ransomware`, `cybersecurity`, `educational`

2. **Criar Releases:** Vá para Releases > Create a new release
   - Versione seu projeto (v1.0, v1.1, etc.)

3. **Adicionar Badges:** Mostre status do projeto no README
   ```markdown
   ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
   ![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)
   ![Educational](https://img.shields.io/badge/Purpose-Educational-green)
   ```

4. **Ativar Discussions:** Settings > Features > Discussions
   - Permita que outros façam perguntas

5. **Compartilhar:** Envie o link para amigos, professores, comunidades

---

## 💡 Dicas Importantes

### Boas Práticas

✅ **Faça commits frequentes** - Um commit para cada mudança importante
✅ **Mensagens descritivas** - Explique o que foi alterado
✅ **Atualize o README** - Mantenha documentação atualizada
✅ **Use .gitignore** - Não envie arquivos desnecessários
✅ **Proteja credenciais** - Nunca envie senhas ou chaves

### Evite

❌ Commits com mensagens como "mudanças" ou "fix"
❌ Enviar arquivos de log ou temporários
❌ Enviar credenciais ou chaves privadas
❌ Fazer commits muito grandes com muitas mudanças
❌ Esquecer de fazer push regularmente

---

## 📚 Recursos Adicionais

- [Documentação oficial do Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Hello World](https://guides.github.com/activities/hello-world/)

---

## 🎉 Parabéns!

Você aprendeu a:
- ✅ Organizar um projeto profissionalmente
- ✅ Usar Git para versionamento
- ✅ Publicar no GitHub
- ✅ Colaborar com outros desenvolvedores

Agora seu projeto está seguro, versionado e acessível para o mundo todo!

**Lembre-se: Quanto mais você praticar, mais fácil fica!**

---

*Última atualização: 29 de outubro de 2025*
*Autor: Manus AI - Especialista em Educação em Cibersegurança*

