Instruction:
 -  install djangorestframework by typing "pip install djangorestframework" in command line or visualcode terminal
 -  install django-cors-headers by typing "pip install django-cors-headers" in command line or visualcode terminal
 -  install react-bootstrap by typing "npm install react-bootstrap@next bootstrap@5.1.0" in command line or visualcode terminal
 -  install react-router-dom by typing "npm install --save react-router-dom" in command line or visualcode terminal
   After install files from above start with activate the environment by typing "dev\Scripts\activate" in cmd
   type "python manage.py runserver" at "challenge/DjangoAPI/" to running python server that will be recieve api from react it will locate at "127.0.0.1:8000"
   type "npm start" at "challenge/filestorage-app" to start react website it will locate at "127.0.0.1:3000"
   In the website will have Home and Storage. There will be list of files in the storage.
   Delete the file by clicking delete button at the end of each file.
   Upload button will open pop-up for upload a files each file will be list one by one and
 can delete by click "X" button at the end of each file. The upload button in the bottom of the pop-up is for upload all the files. 


CLI Command: 
  fs-store.py is store in DjangoAPI folder you can run command from there.
  python .\fs-store.py upload-file <file> # for upload file on cmd
  python .\fs-store.py delete-file <file> # for delete file on cmd
  python .\fs-store.py list-file # for view the file list on cmd