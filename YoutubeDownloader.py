# Current version: pytube 15.0.0
from pytube import YouTube
from os import path, rename, system
from colorama import Fore
from os import startfile

system("cls")
print("Preparando dependências...")

def downloadMP3(url, userPath = "."):
	try:
		yt = YouTube(url)
		print(f"Baixando: {yt.title}", end=" ")
		video = yt.streams.filter(only_audio = True).first()
		out_file = video.download(output_path = userPath)
		base, ext = path.splitext(out_file)
		new_file = base + '.mp3'
		rename(out_file, new_file)
		print("!")
	except Exception as e:
		try:
			return [yt.title, str(e)]
		except:
			return [str(e)]

	return yt.title;



links = [
"https://www.youtube.com/watch?v=ZnrIiuhrEko&ab_channel=Andrezitos"
]


for c in range(0, len(links)):
	v = downloadMP3(links[c], r".\music_raw_download")

	errors = []

	if (type(v) == list):
		print(f"{Fore.RED}Erro ao baixar: {v[0]}{Fore.WHITE}")
		errors.append(v)
	else:
		print(f"{Fore.GREEN}Download completo! " + v, f"{Fore.WHITE}")

print(f"\n\nErros:\n\n{errors}")

print("\n\nPronto para executar conversor!\n")
# input("-> ")
startfile("Mp3Converter.py")