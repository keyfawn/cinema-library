# cinema-library
## Author: Savin Oleg (keyfawn)
**Kinoteka** is a program in which you can store your films, cartoons. It is possible to add a movie by pressing *Ctrl + A*, change the selected movie with *Ctrl + E* and delete the selected cartoon - *Ctrl + D*. It is possible to sort the list of movie titles. Designed for users who do not have access to the Internet.
The main classes are "Window" (main window), "WindowCinema" (movie window), "AddCinema" (window that adds a movie), "EditGenre" (window that edits the list of genres), "WindowAbout" (window containing a description of the program ). For the convenience of quickly making changes to the source code and the best readability, the classes have been divided into separate files.
My project uses the PyQt5 library. With it, you can create full-fledged programs.


### Listing of interesting code

```
def addFileCinema(self):
     if not self.nameCinema.text():
         QMessageBox.critical(self, "Error", "You didn't provide a title")
         return
     if self.db.check_film_name(self.nameCinema.text()):
         QMessageBox.critical(self, "Error", "There is already a movie with the same name")
         return
     path = QFileDialog.getOpenFileName(self, 'Select movie', '',
                                                       'Video (*MP4);; Video (*WebM);; Video (*MOV);; Video (*AVI);; Video (*FLV);; Video (*WMV);;All files (*)')[0]
     if path:
         self.textShortFileCinema.setText('*file selected')
         self.pathCinema = f"resourses/video/vid_{self.nameCinema.text()}_.{Utils.get_file_ex(path)}"
         shutil.copyfile(path, self.pathCinema)
```
         
The meaning of this function is that it copies the video file selected by the user into its own *resources/video* directory called *vid_{self.nameCinema.text()}_.{Utils.get_file_ex(path)* . If the movie name field is empty or the name matches an already existing movie, a critical error will be raised.

### Screenshots
![This is an image](https://i.ibb.co/cJQWsg5/33.jpg)

![This is an image](https://i.ibb.co/DM9XqP3/22.jpg)

![This is an image](https://i.ibb.co/PtY9VjT/1.jpg)
    
### Video
[![Watch the video](https://i.ibb.co/JFwfD4V/cinema.png)](https://youtu.be/6bwWnhj3tgQ)
