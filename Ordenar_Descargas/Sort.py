import os
from shutil import move, register_archive_format
import shutil
from pathlib import Path

src=os.getcwd()
path=Path(src)

regedit=path.joinpath("Regedit")
video=path.joinpath("Videos")
music=path.joinpath("Music")
documents=path.joinpath("Documents")
binaries=path.joinpath("Binaries")
rar=path.joinpath("Rar")
script=path.joinpath("Scripts")
Image=path.joinpath("Images")
print(video)
videoext=[".mp4",".exo"]
musicext=[".mp3",".wav"]
imagesext=[".jpg",".png",".gif",".jpeg",".ico"]
documentsext=[".docx",".pdf",".pptx",".txt",".xlsx",".doc",".ppsx"]
binariesext=[".exe",".msi"]
rarext=[".rar",".zip"]
scriptsext=[".py",".sql",".html",".css","j.s"]
regeditext=[".reg"]

dirlist=os.listdir(src)
filteredlist=[]
for items in dirlist:
    for i in list(items):
        if(i == "."):
            filteredlist.append(items)

for files in filteredlist:
    filename,file_ext=os.path.splitext(files)
    print(filename,file_ext)
    try:
        if not filename:
            pass
        elif file_ext in (musicext):
            if not music.exists():
                music.mkdir()
            shutil.move(
                os.path.join(src,f'{filename}{file_ext}'),
                os.path.join(src,'Music',f'{filename}{file_ext}')
            )
        elif file_ext in (imagesext):
            if not Image.exists():
                Image.mkdir()
            shutil.move(
                os.path.join(src,f'{filename}{file_ext}'),
                os.path.join(src,'Images',f'{filename}{file_ext}')
            )
        elif file_ext in (documentsext):
            if not documents.exists():
                documents.mkdir()
            shutil.move(
                os.path.join(src,f'{filename}{file_ext}'),
                os.path.join(src,'Documents',f'{filename}{file_ext}')
            )
        elif file_ext in (rarext):
            if not rar.exists():
                rar.mkdir()
            shutil.move(
                os.path.join(src,f'{filename}{file_ext}'),
                os.path.join(src,'Rar',f'{filename}{file_ext}')
            )
        elif file_ext in (scriptsext):
            if not script.exists():
                script.mkdir()
            shutil.move(
                os.path.join(src,f'{filename}{file_ext}'),
                os.path.join(src,'Scripts',f'{filename}{file_ext}')
            )
        elif file_ext in (binariesext):
            if not binaries.exists():
                binaries.mkdir()
            shutil.move(
                os.path.join(src,f'{filename}{file_ext}'),
                os.path.join(src,'Binaries',f'{filename}{file_ext}')
            )
        elif file_ext in (videoext):
            
            if not video.exists():
                video.mkdir() 
            shutil.move(
                os.path.join(src,f'{filename}{file_ext}'),
                os.path.join(src,'Videos',f'{filename}{file_ext}')
            )
        elif file_ext in (regeditext):
            if not regedit.exists():
                regedit.mkdir()
                
            #comentario
            shutil.move(
                os.path.join(src,f'{filename}{file_ext}'),
                os.path.join(src,'Regedit',f'{filename}{file_ext}'))
    except(FileNotFoundError,PermissionError):
        pass
        
       
        


