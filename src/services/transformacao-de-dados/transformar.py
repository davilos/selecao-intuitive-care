import pandas as pd
from tabula import read_pdf
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import os


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Remove carriage return
    return df.replace(r"\r+", " ", regex=True)


def create_zip(csv_file: str):
    usual_zip_compression = ZIP_DEFLATED
    zip_name = "Teste_Davilos.zip"

    with ZipFile(zip_name, "w", usual_zip_compression) as zip:
        zip.write(csv_file)

    os.remove(csv_file)

    print(f"Arquivo {csv_file} adicionado ao zip.")


def convert_table_to_csv(src_pdf: str, output_path: str):
    columns = [
        "PROCEDIMENTO",
        "RN (alteração)",
        "VIGÊNCIA",
        "OD",
        "AMB",
        "HCO",
        "HSO",
        "REF",
        "PAC",
        "DUT",
        "SUBGRUPO",
        "GRUPO",
        "CAPÍTULO",
    ]

    dfs = read_pdf(
        input_path=src_pdf,
        # Poderia pegar apenas as páginas da tabela (pages="3-181"), mas no edital tem (todas as páginas)
        pages="all",
        lattice=True,
        pandas_options={"header": None, "names": columns, "skiprows": 3},
        stream=False,
        multiple_tables=False,
    )

    full_df = pd.concat(dfs)

    full_df = clean_dataframe(full_df)

    full_df = full_df.rename(
        columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}
    )

    full_df.to_csv(output_path, index=False)


def main():
    src_path = Path(__file__).resolve().parents[1]
    path_to_pdf = (
        src_path / "web-scraping/files/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    )

    csv_name = "table.csv"

    convert_table_to_csv(path_to_pdf.as_posix(), csv_name)

    create_zip(csv_name)


if __name__ == "__main__":
    main()
