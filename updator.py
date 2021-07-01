import os
from pdf2image import convert_from_path
from PIL import Image

last_number = len(os.listdir(r"assets\img\Important"))


while True:
    path_to_check = input("Where to check for new file : ")

    cnt=1
    for file in os.listdir(path_to_check):
        print(f"{cnt}....." + file)
        cnt+=1
    number = int(input("Give file Number : "))
    name_to_check = os.listdir(path_to_check)[number-1]
    print(name_to_check)
    status = input("Is this the file to be converted or Transfer: (Y/N) ")
    if status == "Y":
        break
    else:
        continue

final_path = os.path.join(path_to_check,name_to_check)
path_to_save = os.path.join(os.getcwd(),r"assets\img\Important")

if name_to_check[int(name_to_check.index("."))+1:] == "pdf":

    images = convert_from_path(final_path,poppler_path=r"C:\Program Files\poppler-21.03.0\Library\bin")

    jpeg_file = ""
    for image in images:
        last_number +=1
        jpeg_file = "Certificate_"+ str(last_number)+".jpeg"
        image.save(jpeg_file,'JPEG')

    image_final = Image.open(os.path.join(os.getcwd(),jpeg_file))
    image_final.save(os.path.join(path_to_save,jpeg_file[:len(jpeg_file)-5]+".jpg"))
    os.remove(os.path.join(os.getcwd(),jpeg_file))

    print("***Successfully Converted****")
else:
    ch = input("Is it already a Image ? (Y/N) ")
    if ch == "Y":
        image_final = Image.open(final_path)
        imager_final = image_final.convert('RGB')
        imager_final.save(os.path.join(path_to_save,"Certificate_"+str(int(last_number)+1)+".jpg"))
        print("***Successfully Copied****")
    else:
        print("Please try Again")


ch = input("Do you want to add new code to file: (Y/N) ")
if ch == "Y":
    file1 = open(r"index.html","rt")
    text1 = file1.read()
    # print(text1[text1.index("<!-- #unique -->") + 16])
    text1 = text1[:text1.index("<!-- #unique -->") + 16] + f'\n\t\t\t\t\t\t<div class="carousel-cell">\n\t\t\t    \t\t\t<img class="w3-image" src="assets\img\Important\Certificate_{str(int(last_number))}.jpg">\n\t\t\t\t\t\t</div>' +text1[text1.index("<!-- #unique -->") + 16:]
    # print("*************************************")
    # print(text1)
    # print("*************************************")


    file2 = open(r"dark_index.html")
    text2 = file2.read()
    # print(text2[text2.index("<!-- #unique -->") + 16])
    text2 = text2[:text2.index("<!-- #unique -->") + 16] + f'\n\t\t\t\t\t\t<div class="carousel-cell">\n\t\t\t    \t\t\t<img class="w3-image" src="assets\img\Important\Certificate_{str(int(last_number))}.jpg">\n\t\t\t\t\t\t</div>' +text2[text2.index("<!-- #unique -->") + 16:]
    # print("*************************************")
    # print(text2)
    # print("*************************************")

    file1.close()
    file2.close()

    #******************************
    file1 = open(r"index.html",'w')
    file1.write(text1)
    file1.close()
    #******************************
    file2 = open(r"dark_index.html",'w')
    file2.write(text2)
    file2.close()

print("Do you wanna open Github Type 'Y' or 'N'" )
ch = input()
if ch == 'Y' or ch == 'y':
    os.system("github")
else:
    print("Thank you for using my services.")