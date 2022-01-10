from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.geometry("600x600")
root.configure(bg = "black")

label_image = Label(root, bg = "white", highlightthickness = 5)
label_image.place(relx = 0.5, rely = 0.5, anchor = CENTER)

img_path = ""

def Open_Image():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Text File", filetypes=[("Image Files", "*.jpg *.gif *.png *.jpeg")])
    print(img_path)
    img = ImageTk.PhotoImage(Image.open(img_path))
    label_image["image"] = img
    img.close()

def rotateImage():
    global img_path
    im = Image.open(img_path)
    rotated_img = im.rotate(180)
    img = ImageTk.PhotoImage(rotated_img)
    label_image["image"] = img
    img.close()
    
open_image_btn = Button(root, text = "Open Image", font = ("courier", 18, "bold"), relief = "solid", padx = 0.5, pady = 0.5, command = Open_Image)
open_image_btn.place(relx = 0.5, rely = 0.25, anchor = CENTER)

rotate_image_btn = Button(root, text = "Rotate Image", font = ("courier", 18, "bold"), relief = "solid", padx = 0.5, pady = 0.5, command = rotateImage)
rotate_image_btn.place(relx = 0.5, rely = 0.75, anchor = CENTER)

credit_label = Label(root, text = "Created by - Joshua Thomas", bg = "black", fg = "white", font = ("courier", 10, "normal"))
credit_label.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()

