import os

def main():
    source = "temp_dataset_cycleGAN/testB"
    destination = "temp_dataset_cycleGAN/"
    for count, filename in enumerate(os.listdir(source)):
        dst ="b-" + str(count) + ".png"
        src = source + filename
        dst = destination + dst
        os.rename(src, dst)

if __name__ == '__main__':
    main()