import csv
import os
import shutil

def get_links(filename):
    """Lê um arquivo TXT e retorna uma lista de links."""
    with open(filename, "r") as f:
        reader = csv.reader(f)
        links = [row[0] for row in reader]
    return links

def create_import_html(links):
    """Cria um arquivo HTML com os links."""
    with open("import.html", "w") as f:
        f.write("<bookmarks>\n")
        for link in links:
            f.write(f"\t<bookmark href=\"{link}\" title=\"{link}\" bookmark=\"true\">\n")
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