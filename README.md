# Interior-Shuffle


Welcome to the AI-Enhanced Interior Design Suite, where cutting-edge artificial intelligence meets modern interior design. Our platform leverages advanced machine learning to analyze your room's layout and offers intelligent suggestions for reshuffling existing furniture or incorporating new pieces seamlessly into your space.

## Features

- **Automated Furniture Detection**: Upload a photo of your room and let our AI detect and catalogue your furniture.
- **Intelligent Reshuffling**: Explore AI-recommended furniture arrangements that optimize your space.
- **Virtual Furniture Addition**: Visualize new furniture items in your room from a curated catalogue.
- **High-Resolution Output**: Receive high-quality images of your redesigned room layouts.
- **User-Friendly Interface**: Simple and intuitive design for a hassle-free experience.

## Quick Start

1. **Set Up Your Environment**:
   Make sure you have Python 3.8+ installed and the necessary libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **API Keys**:
   Obtain and configure your API keys for OpenAI and any other used services as environment variables or in a `.env` file.

3. **Running the Application**:
   Start the web server by executing:
   ```bash
   python app.py
   ```

4. **Uploading an Image**:
   Go to the hosted web page and follow the prompts to upload an image of your room.

5. **Customizing Your Space**:
   Choose whether you want to reshuffle your furniture or add new items.

## Usage

- **Endpoint for Room Analysis**:
  POST `/analyze-room` with form-data containing the 'room_image'.
  
- **Endpoint for Furniture Reshuffling**:
  GET `/reshuffle` returns a visualization of your room with reshuffled furniture.

- **Endpoint for Adding New Furniture**:
  GET `/add-furniture` prompts you to select from a range of furniture before returning a visualization.

## Development

- **Expanding Furniture Catalogue**:
  Integrate with additional APIs or datasets to enhance the selection of available furniture.

- **Improving AI Models**:
  Continuously train the AI on a diverse dataset for more accurate detection and placement suggestions.

- **Frontend Customizations**:
  Modify `static/index.html` to tweak the UI as per your branding needs.

## Support

For any queries or technical support, please open an issue in this repository or contact our development team at support@aiinteriordesign.com.

## Contributing

We welcome contributions! Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

A huge thank you to the OpenAI team for providing the powerful DALL·E API that made this project possible.

---

Thank you for choosing AI-Enhanced Interior Design Suite for your creative interior design needs. Happy designing!
