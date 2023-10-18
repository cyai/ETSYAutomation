import os
from dotenv import load_dotenv

load_dotenv()

import replicate

class ImageProcess:

    def __init__(self) -> None:
        pass
    
    def image_process(self):
        output = replicate.run(
            "daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
            input={
                "image": open("ETSYAutomation/resources/img/img1.jpg", "rb"),
                "prompt": "This is a picture of a jwellery. You need to create a etsy listing for this. Mention the details of the product including the name, size, materials, color and the use cases. Give a detailed and a long description.",
            },
        )

        return output



