import asyncio
import aiohttp
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import random
from io import BytesIO

# Create a directory to save the generated images
if not os.path.exists("./quotes"):
    os.makedirs("./quotes")

UNSPLASH_ACCESS_KEY = "EhbLrq_1p58vId4QpxK4tKxZv5qEsEE_B8ma4Fcq6eY"  
# Replace with your Unsplash API access key

async def get_quotes():
    url = "https://api.quotable.io/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                quote = await response.json()
                content = quote['content']
                author = quote['author']
                return content, author
            else:
                return "Failed to fetch a quote", None

async def fetch_random_image():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.unsplash.com/photos/random", params={"client_id": UNSPLASH_ACCESS_KEY, "query": "street photography"}) as response:
                if response.status == 200:
                    image_data = await response.json()
                    image_url = image_data['urls']['regular']
                    async with session.get(image_url) as image_response:
                        if image_response.status == 200:
                            return await image_response.read()
        return None
    except aiohttp.ClientError as e:
        print(f"Error fetching random image: {e}")
        return None


async def generate_image(content, author, image_data):
    try:
        # Create a blank image with the same size as the background
        background_image = Image.open(BytesIO(image_data)).convert("RGB")
        image = Image.new("RGB", background_image.size)
        
        # Darken the background image
        enhancer = ImageEnhance.Brightness(background_image)
        darkened_image = enhancer.enhance(0.5)  # Adjust the enhancement factor as desired
        
        image.paste(darkened_image, (0, 0))

        # Create a draw object
        draw = ImageDraw.Draw(image)

        # Set the font properties
        font_path = "./Montserrat/static/Montserrat-ExtraBold.ttf"
        max_font_size = int(image.height * 2)  # Half the image height
        quote_width = int(image.width * 0.955)  # Maximum width for the quote text

        # Calculate the maximum font size that fits within the quote width
        font_size = max_font_size
        font = ImageFont.truetype(font_path, font_size)
        while font.getsize(content)[0] > quote_width:
            font_size -= 1
            font = ImageFont.truetype(font_path, font_size)

        # Calculate the position to center the quote text
        quote_position = ((image.width - font.getsize(content)[0]) // 2, (image.height - font_size) // 2)

        # Draw the quote text on the image
        draw.text(quote_position, content, font=font, fill=(255, 255, 255))

        # Calculate the position for the author text
        author_position = (quote_position[0], quote_position[1] + font_size + 10)

        # Crop the image to 16:9 aspect ratio and center the text
        target_ratio = 16 / 9
        image_ratio = image.width / image.height
        if image_ratio > target_ratio:
            target_width = int(image.height * target_ratio)
            left = (image.width - target_width) // 2
            right = left + target_width
            image = image.crop((left, 0, right, image.height))
            quote_position = (quote_position[0] - left, quote_position[1])
            author_position = (author_position[0] - left, author_position[1])
        else:
            target_height = int(image.width / target_ratio)
            top = (image.height - target_height) // 2
            bottom = top + target_height
            image = image.crop((0, top, image.width, bottom))
            quote_position = (quote_position[0], quote_position[1] - top)
            author_position = (author_position[0], author_position[1] - top)

        # Create a new draw object for the cropped image
        draw = ImageDraw.Draw(image)

        # Draw the quote text on the cropped image
        draw.text(quote_position, content, font=font, fill=(255, 255, 255))

        # Draw the author text on the cropped image
        draw.text(author_position, author, font=ImageFont.truetype(font_path, font_size//2), fill=(255, 255, 255))

        # Save the image with a unique filename in the quotes directory
        filename = f"./quotes/quote_{content[:10]}.jpg"
        image.save(filename)
        print(f"Image saved: {filename}")

    except ValueError as e:
        print(f"Error generating image: {e}")

async def main():
    content, author = await get_quotes()
    image_data = await fetch_random_image()
    if image_data:
        await generate_image(content, author, image_data)
    else:
        print("Failed to fetch a random image")

if __name__ == "__main__":
    asyncio.run(main())
