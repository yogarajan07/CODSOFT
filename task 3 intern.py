import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, Label, Button


class ImageCaptioner:
    def __init__(self):
        print("Loading model...")
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        print("Model loaded.")

    def generate_caption(self, image_path):
        try:
            image = Image.open(image_path).convert("RGB")
            inputs = self.processor(image, return_tensors="pt")
            with torch.no_grad():
                output = self.model.generate(**inputs)
            caption = self.processor.decode(output[0], skip_special_tokens=True)
            return caption
        except Exception as e:
            return f"Error: {str(e)}"


class CaptioningApp:
    def __init__(self, root):
        self.captioner = ImageCaptioner()
        self.root = root
        self.root.title("image Captioning with AI")
        self.root.geometry("600x600")
        self.root.configure(bg="black")

        self.image_label = Label(root, text="load an image to caption", bg="white", font=("Arial", 14))
        self.image_label.pack(pady=10)

        self.image_display = Label(root, bg="white")
        self.image_display.pack(pady=10)

        self.caption_text = Label(root, text="", wraplength=500, bg="white", font=("Arial", 12), fg="blue")
        self.caption_text.pack(pady=20)

        self.upload_button = Button(root, text="load Image", command=self.upload_image, font=("Arial", 12), bg="green", fg="white", padx=10, pady=5)
        self.upload_button.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            try:
                img = Image.open(file_path)
                img.thumbnail((400, 400))
                tk_image = ImageTk.PhotoImage(img)
                self.image_display.config(image=tk_image)
                self.image_display.image = tk_image 
                self.caption_text.config(text="Generating caption...")

                self.root.update()
                caption = self.captioner.generate_caption(file_path)
                self.caption_text.config(text=f"caption:{caption}")
            except Exception as e:
                messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CaptioningApp(root)
    root.mainloop()
