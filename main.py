from PIL import Image

for x in range(256):
    # Create 3 256x256 images.
    imageR = Image.new('RGB', (256, 256))
    imageG = Image.new('RGB', (256, 256))
    imageB = Image.new('RGB', (256, 256))
    # Load the pixel data
    pixelsR = imageR.load()
    pixelsG = imageG.load()
    pixelsB = imageB.load()

    for y in range(256):
        for z in range(256):
            pixelsR[y, z] = (x, y, z)
            pixelsG[y, z] = (y, x, z)
            pixelsB[y, z] = (y, z, x)

    # Save the image.
    imageR.save(f'./out/red/{x}.png')
    imageG.save(f'./out/green/{x}.png')
    imageB.save(f'./out/blue/{x}.png')

# Output completion.
print("Images saved to output.")