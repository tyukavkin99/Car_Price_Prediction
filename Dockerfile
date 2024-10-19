# Use a base image with Python
FROM python:3.12.4

# Set the working directory in the container
WORKDIR /app

# Copy the repository
RUN git clone https://github.com/tyukavkin99/Car_Price_Prediction.git .

# Install the requirements
RUN pip install -r requirements.txt

# Listen to the specified port
EXPOSE 8501

# Run the app
ENTRYPOINT ["streamlit", "run", "car_price_streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
