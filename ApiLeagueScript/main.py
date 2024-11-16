# main.py
from fastapi import FastAPI, Response
import pyautogui
from PIL import ImageGrab
import io
from starlette.middleware.base import BaseHTTPMiddleware
import time
import mss

from fastapi.responses import StreamingResponse

from shop_manager import ShopManager

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


@app.get("/cmove")
def move_cursor(x_pos: int = 11, y_pos: int = 11):
    """
    Move the cursor to the specified (x_pos, y_pos) coordinates.
    """
    pyautogui.moveTo(x_pos, y_pos)
    return {"message": f"Cursor moved to ({x_pos}, {y_pos})"}

@app.get("/open/shop")
def openShop():
    shop_manager = ShopManager()
    shop_manager.is_openable()
    pyautogui.moveTo(100, 100)
    pyautogui.click()
@app.get("/open/shop")
def read_current_game_data():
    gameManager = GameManager()


@app.get("/screenshot")
def get_screenshot():
    """
    Capture the current screen and return it as raw byte data.
    """
    # Capture the screen using mss
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])  # You can specify the monitor or region here

    # Convert the screenshot to a PNG byte array
    img_byte_arr = io.BytesIO()
    # 'RGB' format and size from the screenshot
    img_byte_arr.write(screenshot.rgb)
    img_byte_arr.seek(0)

    # Return the image data in raw byte form as a Response
    return Response(content=img_byte_arr.read(), media_type="image/png")
