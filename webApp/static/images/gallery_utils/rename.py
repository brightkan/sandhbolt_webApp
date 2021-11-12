
# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
  
# Function to rename multiple files
def main():
  
    for count, filename in enumerate(os.listdir("GALLERY"),40):
        dst = str(count)
        src = "GALLERY/"+filename
        dst =dst+".jpg"
        print("The filename is", filename) 
        print("The new name is", dst)
        # rename() function will
        # rename all the files
        os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
