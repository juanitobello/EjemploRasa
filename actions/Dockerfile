FROM rasa/rasa-sdk:3.2.1


# Use subdirectory as working directory
#WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
#USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
# RUN pip install -r requirements-actions.txt

# Copy actions folder to working directory
#COPY ./actions /app/actions

#EXPOSE 5055
# By best practices, don't run the code with root user
#USER 1000

#FROM rasa/rasa-sdk:2.7.0
WORKDIR /app
#COPY requirement.txt requirement.txt
USER root
COPY ./actions /app/actions
#RUN pip install -r requirement.txt

USER 1001