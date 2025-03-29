import os
from requests import get
from concurrent.futures import ThreadPoolExecutor, as_completed

from zipfile import ZipFile


def extract_files(file: str):
    with ZipFile(file, "r") as zip:
        zip.extractall("./data/")

    os.remove(file)

    print("Arquivos extraídos com sucesso!")


def download_file(url: str, file_name: str):
    response = get(url, stream=True)

    response.raise_for_status()

    with open(file_name, "wb") as file:
        for chunk in response.iter_content(chunk_size=65536):
            if chunk:
                file.write(chunk)

    print(f"Arquivo {file_name.split('/')[-1]} baixado com sucesso!")


def download_multiple_files(urls: list[str]):
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures_list = []

        for url in urls:
            save_path = "./data/"
            file_name = save_path + url.split("/")[-1]
            futures_list.append(executor.submit(download_file, url, file_name))

        for future in as_completed(futures_list):
            try:
                future.result()
            except Exception as exc:
                print(f"Ocorreu um erro ao baixar o arquivo: {exc}")


def main():
    os.makedirs("./data/", exist_ok=True)

    urls = [
        "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv",
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/1T2023.zip",
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/2T2023.zip",
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/3T2023.zip",
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/4T2023.zip",
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/1T2024.zip",
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/2T2024.zip",
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/3T2024.zip",
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/4T2024.zip",
    ]

    files_to_extract = [
        "./data/1T2023.zip",
        "./data/2T2023.zip",
        "./data/3T2023.zip",
        "./data/4T2023.zip",
        "./data/1T2024.zip",
        "./data/2T2024.zip",
        "./data/3T2024.zip",
        "./data/4T2024.zip",
    ]

    download_multiple_files(urls)

    for file in files_to_extract:
        extract_files(file)


if __name__ == "__main__":
    main()
