package com.lol.ml.lolmloverlay;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;
import java.awt.*;
import javax.swing.*;
import java.awt.image.BufferedImage;
import java.awt.event.*;
import java.awt.Toolkit;
import javax.swing.Timer;
import org.opencv.core.Mat;
import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Rect;
import org.opencv.videoio.VideoCapture;
import java.io.IOException;
import org.opencv.core.Core;
public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        //FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        //Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        //stage.setTitle("Hello!");
        //stage.setScene(scene);
        //stage.show();
    }

    public static void main(String[] args) {
        //launch();
        JFrame frame = new JFrame("League Overlay");
        frame.setUndecorated(true);
        frame.setBackground(new Color(0, 0, 0, 0));  // Transparent background
        frame.setAlwaysOnTop(true);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH); // Fullscreen
        frame.setVisible(true);

        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        frame.setSize(screenSize.width, screenSize.height);

        // Remove window decorations
        frame.getRootPane().putClientProperty("apple.awt.draggableWindowBackground", false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // You can add any custom UI components, such as text fields or labels
        // For now, let's just display some basic text
        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add(new JTextField("Overlay Active"), BorderLayout.NORTH);

        // Timer to periodically capture the game screen
        Timer timer = new Timer(1000 / 30, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Capture game screen (or League window)
                BufferedImage screenCapture = captureScreen();

                // Process the captured screen with ML for object detection
                detectObjects(screenCapture);

                // You could also update UI or give recommendations based on ML output
            }
        });
        timer.start();

    }
    private static BufferedImage captureScreen() {
        try {
            Robot robot = new Robot();
            Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
            Rectangle screenRect = new Rectangle(screenSize);
            return robot.createScreenCapture(screenRect);
        } catch (AWTException e) {
            e.printStackTrace();
        }
        return null;
    }

    // Detect objects like champions, minions using OpenCV and ML models
    private static void detectObjects(BufferedImage image) {
        // Convert the BufferedImage to OpenCV Mat for processing
        Mat matImage = bufferedImageToMat(image);

        // Pre-process the image (e.g., convert to grayscale)
        Mat grayImage = new Mat();
        Imgproc.cvtColor(matImage, grayImage, Imgproc.COLOR_BGR2GRAY);

        // Here you would load your pre-trained ML model (e.g., YOLO, TensorFlow, etc.)
        // For now, just a placeholder logic
        // Detect any objects and update the overlay
    }
    private static void detectObjects(SavedModelBundle model, BufferedImage image) {
        // Convert the BufferedImage to Tensor
        Tensor<Float> tensorImage = imageToTensor(image);

        // Use the model to make a prediction
        try (Tensor<?> result = model.session().runner().feed("input_tensor_name", tensorImage).fetch("output_tensor_name").run().get(0)) {
            // Parse the result and detect objects
            // You would need to decode the result (boxes, classes, and scores)
            float[] boxes = result.copyTo(new float[10][4]); // Adjust the size according to the output shape
            System.out.println("Detected boxes: " + Arrays.toString(boxes));

            // You can then use the boxes to draw the bounding boxes around objects in your GUI
        }
    }

    // Convert the image to a tensor
    private static Tensor<Float> imageToTensor(BufferedImage image) {
        // Convert the image to a byte array or float array and create a Tensor
        // This conversion depends on the model's input format (e.g., normalized pixels, RGB channels, etc.)
        int width = image.getWidth();
        int height = image.getHeight();
        float[] imageData = new float[width * height * 3];  // Assuming RGB channels
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int pixel = image.getRGB(x, y);
                imageData[(y * width + x) * 3] = ((pixel >> 16) & 0xFF) / 255.0f;  // Red
                imageData[(y * width + x) * 3 + 1] = ((pixel >> 8) & 0xFF) / 255.0f;  // Green
                imageData[(y * width + x) * 3 + 2] = (pixel & 0xFF) / 255.0f;  // Blue
            }
        }
        return Tensor.create(new long[]{1, height, width, 3}, FloatBuffer.wrap(imageData));
    }

    // Convert BufferedImage to OpenCV Mat
    private static Mat bufferedImageToMat(BufferedImage image) {
        // Convert BufferedImage to Mat (OpenCV format)
        int width = image.getWidth();
        int height = image.getHeight();
        Mat mat = new Mat(height, width, CvType.CV_8UC3);
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                Color pixel = new Color(image.getRGB(x, y));
                mat.put(y, x, new byte[]{(byte) pixel.getBlue(), (byte) pixel.getGreen(), (byte) pixel.getRed()});
            }
        }
        return mat;
    }
}