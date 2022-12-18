# cinema-library
## Author: Savin Oleg (keyfawn)
**Kinoteka** is a program in which you can store your films, cartoons. It is possible to add a movie by pressing *Ctrl + A*, change the selected movie with *Ctrl + E* and delete the selected cartoon - *Ctrl + D*. It is possible to sort the list of movie titles. Designed for users who do not have access to the Internet.
The main classes are "Window" (main window), "WindowCinema" (movie window), "AddCinema" (window that adds a movie), "EditGenre" (window that edits the list of genres), "WindowAbout" (window containing a description of the program ). For the convenience of quickly making changes to the source code and the best readability, the classes have been divided into separate files.
The functionality related to project maintenance has been moved to a separate utility class Utils to reduce code copying. It mainly has the functionality of working with the database.

### Technologies used

The following libraries were used in the development of the project:
- PyQt5 - My project uses the PyQt5 library. With it, you can create full-fledged programs. It is installed using a simple command in Terminal.
- Shutil - to copy banner and video files to a separate resource directory.
- os - for working with video and graphics in the project directories. Getting the full path, removing unused resources, etc.
- subprocess - to run the video directly from the project.
- sqlite3 - for working with the project database.

In addition, several programming methodologies have been applied:
1. The entire project as a whole is developed in accordance with the OOP methodology.
2. As mentioned earlier, for convenience, each individual page and its functionality are placed in separate classes. UI components also exist separately from functionality. This design method uses the Page Object pattern.

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
