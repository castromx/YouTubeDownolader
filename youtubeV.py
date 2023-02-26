from pytube import YouTube

link = input('Введіть силку на відео:')
video = YouTube(link)
quality = input('Вкажіть якість відео(Висока/Низька):')

if quality == 'Висока':
	output = video.streams.get_highest_resolution()
if quality =='Низька':
	output = video.streams.get_lowest_resolution()

output.download()

#відео установлюється в папку з програмою