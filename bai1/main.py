from guizero import App, Box, Picture, Text

app = App("Ứng dụng gallery", width=800, height=600)

gallery_box = Box(app, layout="grid", border=True)

picture1 = Picture(gallery_box, image="pic1.jpg", grid=[0,0], width=200, height=200)
picture1 = Picture(gallery_box, image="pic2.jpg", grid=[1,0], width=200, height=200)
picture1 = Picture(gallery_box, image="pic3.jpg", grid=[0,1], width=200, height=200)
picture1 = Picture(gallery_box, image="pic4.jpg", grid=[1,1], width=200, height=200)

app.display()