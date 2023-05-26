# Image Quote Generator

This is a Python script that generates image quotes by combining random quotes obtained from the Quotable API with random images fetched from the Unsplash API. The generated image quotes are saved in a directory named "quotes" as JPEG files.

![Image Quote Generator](quotes/quote_Wisdom_is.jpg)

## Prerequisites

- Python 3.7 or above
- aiohttp library (install using `pip install aiohttp`)
- PIL library (install using `pip install Pillow`)

## Getting Started

1. Clone the repository or download the code files to your local machine.

2. Install the required dependencies using the following command:


3. Open the Python script `main.py` in your preferred editor.

4. Replace the value of the `UNSPLASH_ACCESS_KEY` variable with your own Unsplash API access key. You can obtain an access key by signing up for an account on the Unsplash Developer portal.

5. Save the changes and close the file.

6. Open a terminal or command prompt and navigate to the directory where the script is located.

7. Run the script using the following command:


8. The script will fetch a random quote from the Quotable API and a random image from the Unsplash API. It will then generate an image quote by overlaying the quote text on the image and save it in the "quotes" directory.

9. Check the "quotes" directory to find the generated image quote.

## Configuration

You can customize the behavior of the script by modifying the following variables in the `main.py` file:

- `UNSPLASH_ACCESS_KEY`: Your Unsplash API access key.
- `font_path`: The path to the TrueType font file to be used for the quote text.
- `max_font_size`: The maximum font size for the quote text.
- `quote_width`: The maximum width for the quote text.
- `target_ratio`: The target aspect ratio for the cropped image (default is 16:9).
- `darken_factor`: The factor used to darken the background image (default is 0.5).

Feel free to adjust these variables to suit your preferences.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Quotable API](https://github.com/lukePeavey/quotable)
- [Unsplash API](https://unsplash.com/developers)
- [Pillow Library](https://python-pillow.org/)
- [aiohttp Library](https://docs.aiohttp.org/)

