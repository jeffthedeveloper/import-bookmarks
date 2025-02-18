import csv
import os
import shutil

def get_links(filename):
    """Lê um arquivo TXT e retorna uma lista de links."""
    with open(filename, "r") as f:
        reader = csv.reader(f)
        links = [row[0] for row in reader]
    return links

def create_import_html(links, folder_name="my_bookmarks"):
    """Cria um arquivo HTML com os links, agrupados em uma pasta."""
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    with open("import.html", "w") as f:
        f.write("<bookmarks>\n")
        f.write(f"\t<folder name=\"{folder_name}\">\n")
        for link in links:
            f.write(f"\t\t<bookmark href=\"{link}\" title=\"{link}\" bookmark=\"true\">\n")
        f.write(f"\t</folder>\n")
        f.write("</bookmarks>\n")

def import_bookmarks():
    """Abre o arquivo HTML no navegador."""
    os.system("start import.html")

def main():
    """Função principal do script."""
    filename = "links.txt"  # Nome do arquivo TXT com os links

    links = get_links(filename)
    create_import_html(links)
    import_bookmarks()

if __name__ == "__main__":
    main()