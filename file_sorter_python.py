import os 
import shutil
import time

def main(i,video_formats,image_formats,pdf_formats):
    #docx files
    if ".docx" in i or ".doc" in i:
        Download_docx(i)

    #Video files
    elif f".{i}" in video_formats:
        Download_video(i)

    #image files
    elif f".{i}" in image_formats:
        Download_image(i)
    
    #pdf files
    elif f".{i}" in pdf_formats:
        Download_pdf(i)

    #powerpoint files
    elif i in ".ppt":
        Download_powerpoint(i)
    
    #exe files
    elif i in ".exe":
        Download_exe(i)

    #any other files like zip files or something any miscellaneous files if you will...
    else:
        Download_other(i)

def Download_docx(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\docx")
def Download_video(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\video")
def Download_image(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\image")
def Download_pdf(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\pdf")
def Download_powerpoint(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\powerpoint")
def Download_exe(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\execu")
def Download_other(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\miscellaneous")

if __name__ == '__main__':
    
    video_formats = ["mp4", "avi", "mov", "wmv", "flv", "mkv", "webm", "mpeg"]
    image_formats = ["jpeg", "png", "gif", "bmp", "tiff", "svg", "webp", "heif"]
    pdf_formats = ['pdf', 'html']

    dir = r"C:\Users\ldogb\Downloads"
    while 1:
        time.sleep(20)
        files = os.listdir(dir)
        if files:
            for i in files:
                main(i,video_formats,image_formats,pdf_formats)

        

