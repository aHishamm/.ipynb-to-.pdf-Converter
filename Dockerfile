FROM python:3.10
ADD . . 
RUN pip install -r requirements.txt 
RUN apt update 
RUN apt install texlive -y
RUN apt install texlive-xetex texlive-fonts-recommended texlive-plain-generic texlive-latex-extra pandoc -y
EXPOSE 7250 
ENTRYPOINT ["streamlit","run"] 
CMD ["./app.py","--server.headless","true","--server.fileWatcherType","none","--browser.gatherUsageStats","false","--server.port=7250","--server.address=0.0.0.0"]
 