from os import system, listdir, startfile, getcwd,  rename
from unicodedata import normalize
from time import sleep

def remover_acentos(path):
	print("Removendo espaços e acentuações...")
	names = listdir(path)

	for c in names:
		cf = c.replace(" ", "_")
		rename(path + c, path + normalize('NFKD', cf).encode('ASCII', 'ignore').decode('ASCII'));


def write(txt):
	with open(f"{getcwd()}\\ffmpeg\\bin\\script.bat", "w", encoding="utf-8") as esc:
		esc.write(str(txt))
		esc.close()

write("")
path = getcwd()
remover_acentos = remover_acentos(r".\music_raw_download" + "\\")
musics = listdir(r".\music_raw_download")

txt = ""
for c in range(0, len(musics)):
	txt += f"cd {getcwd()}\\ffmpeg\\bin && ffmpeg -i {path}\\music_raw_download\\{musics[c]} -c:a libmp3lame {path}\\musics\\{musics[c]}\n"

write(txt + "\npause")

# input(":")

print("Removendo arquivos .mp4...")
system(r"cd .\music_raw_download && del *.mp4")

print("Executando script")
sleep(3)
startfile(path + "\\ffmpeg\\bin\\script.bat")