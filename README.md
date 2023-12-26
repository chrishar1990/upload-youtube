# Youtube Upload


## Description

The CLI app searches for an s3 bucket for a particular video file and uploads the file to a YouTube channel.

## Getting Started

### Dependencies

*requirements code: Install packages with pip: -r requirements.txt
* Use a Python Virtual Environment if you run the code without the dockerfile.

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program
* "file path and name of the file you want to give."
''' python3 app.py --input'''

* Example:
  '''python3 app.py --input /home/treeboy/upload-youtube/ocean.mp4'''

*You can also download run install the Dockerfile and run it.

## Help

*https://www.youtube.com/watch?v=eq-mjehACe4&ab_channel=SoftwareSage    How to upload to Youtube.
*You will also need an account with Google Cloud to upload and allow youtube apis. It is explained in the video above. You will need to verify the application if you want to have a non-private video uploaded. 
If you already have a video you can use the upload youtube file only. an example of what to use with the code below.
```
python3 upload_video.py --file="/home/treeboy/upload-youtube/ocean.mp4" --title="Ocean" --description="Test app" --keywords="Python, programming" --category="28" --privacyStatus="private"
```


## Acknowledgments

Inspiration, code snippets, etc.
* [davidrazmadzeExtra]([https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46](https://github.com/davidrazmadzeExtra/YouTube_Python3_Upload_Video)https://github.com/davidrazmadzeExtra/YouTube_Python3_Upload_Video)
