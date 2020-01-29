import os


def discovery(initialPath):
    extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img'  # Arquivos do Sitema
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # imagens
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # Audios
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # Vídeos
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # Microsoft office
        # OpenOffice, Adobe, Latex, Markdown, etc
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
        'yml', 'yaml', 'json', 'xml', 'csv',  # Dados estruturados e config
        'db', 'sql', 'dbf', 'mdb', 'iso',  # Bancos de dados e imagens de disco

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css'  # Tecnologias web
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # Código fonte C e C++
        'java', 'class', 'jar'  # Códigos fonte Java
        'ps', 'bat', 'vb',  # Scripts de sistemas windows
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # Scripts de sistemas unix
        'go', 'py', 'pyc', 'bf', 'coffee',  # Outros tipos de códigos fonte

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # Arquivos compactados e Backups
    ]

    for dirPath, dirs, files in os.walk(initialPath):
        for _file in files:
            absPath = os.path.abspath(os.path.join(dirPath, _file))
            ext = absPath.split('.')[-1]
            if ext in extensions:
                yield absPath


if __name__ == '__main__':
    x = discovery(os.getcwd())
    for i in x:
        print(i)
