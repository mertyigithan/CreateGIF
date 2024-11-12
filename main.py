# Yüklenecek kütüphane;
import imageio.v3 as iio

# Fonksiyon;
def createGIF():
    print("CreateGIF'e hoş geldin :)")
    filename1 = input("GIF'te yer alacak 1. görselin dosya adını (uzantısıyla) gir: ")
    filename2 = input("GIF'te yer alacak 2. görselin dosya adını (uzantısıyla) gir: ")
    filenames = [filename1, filename2]
    images = []
    for filename in filenames:
        images.append(iio.imread(filename))
    time = float(input("Her bir görselin GIF'te ne kadar süre (ms) gösterileceğini gir: "))
    gifname = input("GIF dosyana bir isim ver: ")
    iio.imwrite(gifname+".gif", images, duration=time, loop=0)
    print(f"{gifname+".gif"} oluşturuldu!")

# Çalıştır;
createGIF()