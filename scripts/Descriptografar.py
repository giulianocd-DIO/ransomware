from cryptography.fernet import Fernet
import os

#1. Carregar a chave salva
def carregar_chave():
    return open("Malware/chave.key", "rb").read()

#2. Descriptografar um único arquivo
def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptados = file.read()
    dados_desencriptados = f.decrypt(dados_encriptados)
    with open(arquivo, "wb") as file:
        file.write(dados_desencriptados)

#3. Encontrar arquivos para descriptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome.endswith(".txt"):
                lista.append(caminho)
    return lista

#4. Execução principal
def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("Malware/Teste_arquivos")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print("Descriptografia concluída! Seus arquivos foram restaurados.")

if __name__ == "__main__":
    main()

