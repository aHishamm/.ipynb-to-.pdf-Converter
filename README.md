# .ipynb to .pdf Converter 
This is a Streamlit Python application that converts .ipynb files to .pdf files seamlessly. 

### **Docker Container Deployment**
- To create a Docker container, a Dockerfile is provided. Make sure Docker Desktop is installed. The Dockerfile contains the following steps: 
```bash
FROM python:3.10
ADD . . 
RUN pip install -r requirements.txt 
RUN apt update 
RUN apt install texlive -y
RUN apt install texlive-xetex texlive-fonts-recommended texlive-plain-generic texlive-latex-extra pandoc -y
EXPOSE 7250 
ENTRYPOINT ["streamlit","run"] 
CMD ["./app.py","--server.headless","true","--server.fileWatcherType","none","--browser.gatherUsageStats","false","--server.port=7250","--server.address=0.0.0.0"]
```
- To build the Docker image from the Dockerfile, run the following command in the terminal or powershell: 
```bash
docker build -t converter_image . 
```
- To run a Docker container with the name 'converter_container' on port 7250: 
```bash
docker run -p 7250:7250 --name converter_container converter_image
```


### **Huggingface Deployment**

