# ETSYAutomation


## Setup:

- install dependencies:
  `pip install -r requirements.txt`
  
- create a `.env` file and add the follwing content:
  ```
  OPENAI_API_KEY=<your-openai-api-key>
  REPLICATE_API_TOKEN=<replicate-api-key>
  ```
  > You can get your Replicate API key from here: https://replicate.com/

- put your images in `ETSYAutomation/resources/img/` directory

  > By defaut img1 is being used in the code. If needed you have to change the image file name in line `17` of `ETSYAutomation/image_processing.py` file.

 - run the `main.py` file: `python main.py`  
