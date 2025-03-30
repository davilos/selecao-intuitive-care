import os
import pandas as pd

from requests import get
from concurrent.futures import ThreadPoolExecutor, as_completed
from zipfile import ZipFile

import pandas as pd


def parse_dates(data_series: pd.Series) -> pd.Series:
    converted_dates = pd.to_datetime(data_series, format="%d/%m/%Y", errors="coerce", cache=True)

    invalid_converted_dates = converted_dates.isna()

    converted_dates.loc[invalid_converted_dates] = pd.to_datetime(
        data_series[invalid_converted_dates], format="%Y-%m-%d", errors="coerce"
    )

    return converted_dates


def clean_dataframe(file: str):
    df = pd.read_csv(
        file,
        sep=";",
        dtype={
            "DATA": "string",
        },
    )

    for col in ["VL_SALDO_INICIAL", "VL_SALDO_FINAL"]:
        df[col] = df[col].apply(lambda x: str(x).replace(",", ".")).astype(float)

    df["DATA"] = parse_dates(df["DATA"])

    print(f"Arquivo {file} modificado com sucesso!")
    df.to_csv(file, index=False, sep=";", date_format="%Y-%m-%d")


def extract_files(file: str):
    with ZipFile(file, "r") as zip:
        zip.extractall("./data/")

    os.remove(file)

    print(f"Arquivo {file.split("/")[-1]} extraído com sucesso!")


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

    files_to_clean = [
        "./data/1T2023.csv",
        "./data/2t2023.csv",
        "./data/3T2023.csv",
        "./data/4T2023.csv",
        "./data/1T2024.csv",
        "./data/2T2024.csv",
        "./data/3T2024.csv",
        "./data/4T2024.csv",
    ]

    download_multiple_files(urls)

    for file in files_to_extract:
        extract_files(file)

    for file in files_to_clean:
        clean_dataframe(file)


if __name__ == "__main__":
    main()
