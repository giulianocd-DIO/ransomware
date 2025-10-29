# Instruções para Enviar o Projeto ao GitHub

Para compartilhar seu projeto no GitHub, siga os passos abaixo. Certifique-se de ter uma conta no GitHub e o Git instalado em sua máquina local.

## 1. Inicializar um Repositório Git Local

Navegue até a pasta raiz do seu projeto (`Malware`) no terminal e inicialize um novo repositório Git:

```bash
cd Malware
git init
```

## 2. Adicionar os Arquivos ao Repositório

Adicione todos os arquivos do seu projeto ao stage (área de preparação) do Git. O comando `.` adiciona todos os arquivos no diretório atual e subdiretórios.

```bash
git add .
```

## 3. Realizar o Primeiro Commit

Crie o primeiro commit, que é um "instantâneo" das suas alterações. A mensagem do commit deve ser descritiva.

```bash
git commit -m "Primeiro commit: Projeto de simulacao de ransomware"
```

## 4. Criar um Repositório no GitHub

1.  Acesse o GitHub (github.com) e faça login em sua conta.
2.  No canto superior direito, clique no sinal de `+` e selecione `New repository`.
3.  Dê um nome ao seu repositório (por exemplo, `Simulacao-Ransomware-Python`).
4.  Adicione uma descrição opcional.
5.  Escolha se o repositório será `Public` (público) ou `Private` (privado).
6.  **Não** inicialize o repositório com um README, .gitignore ou licença, pois você já tem esses arquivos localmente.
7.  Clique em `Create repository`.

## 5. Conectar o Repositório Local ao Remoto

Após criar o repositório no GitHub, você verá uma página com instruções. Copie o comando para adicionar o repositório remoto. Ele será algo parecido com:

```bash
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

Substitua `SEU_USUARIO` pelo seu nome de usuário do GitHub e `SEU_REPOSITORIO` pelo nome que você deu ao seu repositório.

## 6. Enviar os Arquivos para o GitHub

Finalmente, envie seus arquivos locais para o repositório remoto no GitHub. O comando `main` pode ser `master` dependendo da configuração padrão do seu Git.

```bash
git push -u origin main
```

Se for a primeira vez que você envia para o GitHub, pode ser que o Git solicite suas credenciais (nome de usuário e senha/token de acesso pessoal).

## 7. Verificar no GitHub

Após o push, atualize a página do seu repositório no GitHub para ver todos os seus arquivos lá. Se você criou uma pasta `/images` com capturas de tela, elas também aparecerão.
