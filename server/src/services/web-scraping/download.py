import os

from requests import get
from zipfile import ZipFile, ZIP_DEFLATED

from concurrent.futures import ThreadPoolExecutor, as_completed


def create_zip(zip_name: str, files: list[str]):
    usual_zip_compression = ZIP_DEFLATED

    with ZipFile(zip_name, "w", usual_zip_compression) as zip:
        for file in files:
            output_file_name = file.split("/")[-1]

            zip.write(file, output_file_name)
            print(f"Arquivo {output_file_name} adicionado ao zip.")


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
    save_path = "./data/"

    os.makedirs(save_path, exist_ok=True)

    path_files = [
        "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
        "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf",
    ]

    download_multiple_files(path_files)

    files = [save_path + url.split("/")[-1] for url in path_files]
    create_zip(f"{save_path}files.zip", files)


if __name__ == "__main__":
    main()
