from PIL import Image
import os
from os import listdir


def asciiConvert(image, saveas, scale):
    scale = int(scale)

    #otvori sliku i uzmi veličinu slike
    img = Image.open(image)
    w, h = img.size

    #resize-anje slike
    resized_path = "resized_temp.jpg"
    img.resize((w // scale, h // scale)).save(resized_path)

    #otvori novu sliku
    img = Image.open(resized_path)
    w, h = img.size #za uzet novu visinu i širinu

    #lista s visinom i širinuom resize-ane slike
    grid = []
    for i in range(h):
        grid.append(["X"] * w)
    
    pixel = img.load()

    for y in range(h):
        for x in range(w):
            if sum(pixel[x,y]) == 0:
                grid[y][x] = "#"
            elif sum(pixel[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pixel[x,y]) in range(100,200):
                grid[y][x] = "%"
            elif sum(pixel[x,y]) in range(200,300):
                grid[y][x] = "&"
            elif sum(pixel[x,y]) in range(300,400):
                grid[y][x] = "*"
            elif sum(pixel[x,y]) in range(400,500):
                grid[y][x] = "+"
            elif sum(pixel[x,y]) in range(500,600):
                grid[y][x] = "/"
            elif sum(pixel[x,y]) in range(600,700):
                grid[y][x] = "("
            elif sum(pixel[x,y]) in range(700,800):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "
    
    art = open(saveas, "w")

    for row in grid:
        art.write("".join(row) + "\n")

    art.close()

if __name__ == '__main__':
    folder_path = "C:/Users/Washington/Desktop/photo to ascii art/images"
    scale = 3
    counter = 0

    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', 'jpeg'))][:5]
    for image in image_files:
        image_path = os.path.join(folder_path, image)

        base_name, ext = os.path.splitext(image)
        output_file = os.path.join(folder_path, f"{base_name}_ascii.txt")

        asciiConvert(image_path, output_file, scale)
        counter += 1
        print(f"Conversion number {counter} completed.")

    print("All conversions are complete!")