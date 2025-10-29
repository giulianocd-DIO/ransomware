# Projeto de Simulação de Ransomware em Python

## Visão Geral

Este projeto educacional tem como objetivo simular o comportamento de um ransomware em um ambiente controlado, utilizando scripts Python. Ele permite entender como um ataque de ransomware funciona, desde a criptografia de arquivos até a exigência de resgate, e como reverter a criptografia (neste ambiente simulado). Além disso, o projeto inclui uma documentação abrangente sobre medidas de prevenção e defesa contra ransomware.

**Atenção:** Este projeto é estritamente para fins educacionais e deve ser executado apenas em ambientes controlados e isolados. A execução em sistemas de produção ou com arquivos reais pode resultar em perda permanente de dados.

## Conteúdo do Repositório

*   `Ransomware.py`: Script Python que simula a criptografia de arquivos de texto (`.txt`) em um diretório específico.
*   `Descriptografar.py`: Script Python que simula a descriptografia dos arquivos criptografados pelo `Ransomware.py`, utilizando a chave gerada.
*   `Teste_arquivos/`: Pasta contendo arquivos de texto de exemplo (`senhas.txt`, `Dados_sensiveis.txt`) que serão usados para a simulação.
*   `chave.key`: Arquivo gerado pelo `Ransomware.py` que armazena a chave de criptografia. Essencial para a descriptografia.
*   `LEIA ISSO.txt`: Arquivo gerado pelo `Ransomware.py` que contém a mensagem de "resgate" após a criptografia.
*   `Medidas_de_Defesa_Ransomware.md`: Documento detalhando as medidas de prevenção e defesa contra ransomware.

## Como Usar

### Pré-requisitos

*   Python 3.x instalado.
*   Biblioteca `cryptography` instalada (`pip install cryptography`).

### Passos para Simulação

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd Malware
    ```

2.  **Crie os arquivos de teste (se ainda não existirem):**
    Certifique-se de que a pasta `Teste_arquivos` e os arquivos `senhas.txt` e `Dados_sensiveis.txt` estejam presentes, conforme a estrutura:
    ```
    Malware/
    ├── Teste_arquivos/
    │   ├── senhas.txt
    │   └── Dados_sensiveis.txt
    ├── Ransomware.py
    ├── Descriptografar.py
    └── Medidas_de_Defesa_Ransomware.md
    ```

3.  **Execute o script de Ransomware:**
    Este script irá gerar uma chave de criptografia (`chave.key`), criptografar os arquivos `.txt` dentro de `Teste_arquivos/` e criar a mensagem de resgate (`LEIA ISSO.txt`).
    ```bash
    python3 Ransomware.py
    ```
    Verifique o conteúdo dos arquivos em `Teste_arquivos/` e o arquivo `LEIA ISSO.txt`.

4.  **Execute o script de Descriptografia:**
    Este script utilizará a `chave.key` gerada para descriptografar os arquivos em `Teste_arquivos/`, restaurando seu conteúdo original.
    ```bash
    python3 Descriptografar.py
    ```
    Verifique novamente o conteúdo dos arquivos em `Teste_arquivos/` para confirmar a descriptografia.

## Reflexão sobre Defesa

O documento `Medidas_de_Defesa_Ransomware.md` detalha as principais estratégias para proteger-se contra ataques de ransomware, incluindo:

*   **Antivírus e EDR:** Soluções para detecção e resposta a ameaças.
*   **Firewall:** Barreiras de rede para controlar o tráfego.
*   **Sandboxing:** Ambientes isolados para análise segura de arquivos suspeitos.
*   **Conscientização do Usuário:** Treinamento para identificar e evitar táticas de engenharia social.
*   **Outras Medidas Essenciais:** Backups imutáveis, atualizações de software, princípio do menor privilégio e MFA.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções ou sugestões. Abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. (Nota: O arquivo LICENSE não está incluído neste exemplo, mas é uma boa prática adicioná-lo.)

