# Mandelbulb Visualizer

This project is a Mandelbulb visualizer built using Python's Tkinter library. It generates a 2D projection of the 3D Mandelbulb fractal using ray marching techniques to create a visual representation of the fractal structure.

## Customization

You can customize the following parameters directly in the script:

- **`cams`**: Camera position as a tuple `(x, y, z)` (default: `(-3, 0, 0)`).
- **`light`**: Light source position as a tuple `(x, y, z)` (default: `(-5, 5, -10)`).
- **`ang`**: Field of view angle in radians (default: `math.radians(30)`).
- **`close`**: Near clipping plane distance for the ray marching algorithm (default: `0.001`).
- **`far`**: Far clipping plane distance for the ray marching algorithm (default: `10`).
- **`width`, `height`**: Dimensions of the canvas window (default: `800, 800`).

### Modifying the Fractal

You can redefine the object class to implement a new signed distance function (SDF) for different fractal shapes. By default, the `Mandelbulb` class uses the power and maximum iteration parameters:

- **`pow`**: Exponent used in the fractal equation (default: `8`).
- **`mxit`**: Maximum number of iterations for calculating the fractal (default: `100`).

To create different fractal shapes, you can **`simply rewrite the SDF finction`**

## Dependencies

Ensure you have the following Python libraries installed:

- `tkinter` (usually included with Python)
- `math`

## Usage

1. Run the visualization script using Python:

    ```bash
    python mandelbulb_visualizer.py
    ```

2. A window will open displaying the Mandelbulb fractal. You can modify the `pow` and `mxit` parameters in the `Mandelbulb` class to change the fractal's complexity and structure.

3. Customize the camera and light settings directly in the script to explore the fractal from different perspectives.
