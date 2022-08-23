# Define base image to build from
FROM python:3.10

# Create a working directory
WORKDIR /app

# Copy all the requirements into the new directory
COPY requirements.txt ./requirements.txt

# Upgrade pip and install all the requirments
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port to be used
EXPOSE 8501

# Copy app files from the current directory to workdir
COPY . /app

# Create an entry point to make our image executable
ENTRYPOINT ["streamlit", "run"]

# Run the app
CMD ["website_app.py"]

#----------------------------------------------------------#

#================ Build the image =================#
# docker build -t my_web_app -f Dockerfile .       #
#                                                  #
#============== Run the image built ===============#
# docker run -p 8501:8501 my_web_app:latest        #
#==================================================#
