# main.py
from fastapi import FastAPI
import pyautogui
from PIL import ImageGrab
import io
from starlette.middleware.base import BaseHTTPMiddleware
import time

from fastapi.responses import StreamingResponse

app = FastAPI()


class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()  # Record start time

        response = await call_next(request)  # Process the request

        # Calculate duration
        duration = time.time() - start_time
        print(f"Request to {request.url} took {duration:.4f} seconds")

        return response

# Add the custom middleware to the app
app.add_middleware(TimingMiddleware)
@app.get("/move_cursor")
def move_cursor(x_pos: int, y_pos: int):
    """
    Move the cursor to the specified (x_pos, y_pos) coordinates.
    """
    pyautogui.moveTo(x_pos, y_pos)
    return {"message": f"Cursor moved to ({x_pos}, {y_pos})"}



@app.get("/screenshot")
def get_screenshot():
    """
    Capture the current screen and return it as an image.
    """
    # Capture the screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot to a byte stream
    img_byte_arr = io.BytesIO()
    screenshot.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Return the image as a response
    return StreamingResponse(img_byte_arr, media_type="image/png")