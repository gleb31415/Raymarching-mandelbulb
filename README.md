Mandelbulb Visualizer
This project is a simple Mandelbulb visualizer built using Python's tkinter library. It generates a 2D projection of the 3D Mandelbulb fractal using ray marching techniques and renders it on a canvas. The visualization simulates basic lighting and shading effects to give a sense of depth and form to the fractal structure.

Features
Ray Marching: The visualization employs ray marching to calculate the distance to the fractal surface, allowing the rendering of complex 3D shapes like the Mandelbulb.
Lighting and Shading: Implements basic lighting calculations using the dot product between the light vector and surface normal to determine the intensity of the color at each point.
Interactive Parameters: Easily adjustable parameters such as camera position, light source, and field of view to customize the visualization.
Code Overview
Main Components
Mandelbulb Object: The Mandelbulb class is imported from the objects module and is responsible for defining the signed distance function (SDF) of the fractal. The SDF is used in the ray marching process to determine the distance from a given point to the Mandelbulb surface.

Rendering Loop: The nested loop over the canvas width and height iterates through each pixel to calculate its color based on the distance to the fractal. For each pixel, the get_col() function is called to determine the appropriate RGB values.

Lighting Calculation: The get_light_intensity() function calculates the intensity of light hitting a point on the fractal surface. It uses the surface normal and the direction of the light source to compute this value, creating a shaded effect.

Key Functions
get_to_norm(vec): Normalizes a 3D vector to a unit vector.
scal(p, q): Computes the dot product of two vectors p and q.
normal(point, eps): Calculates the surface normal at a given point using central differences.
toreal(point, r, al, be): Transforms a point in spherical coordinates to Cartesian coordinates.
get_light_intensity(point): Returns the intensity of the light at a given point based on the surface normal and light vector.
get_col(point, al, be): Main function to determine the color of a pixel based on its distance to the fractal surface.
Requirements
Python 3.x
tkinter library (usually comes pre-installed with Python)
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/gleb31415/Fourie-complex-transform.git
Navigate to the project directory:

bash
Copy code
cd Fourie-complex-transform
Run the script:

bash
Copy code
python3 main.py
The visualization will open in a new window, rendering the Mandelbulb fractal.

Customization
You can customize the following parameters directly in the script:

cams: Camera position, defined as a tuple (x, y, z).
light: Light source position, defined as a tuple (x, y, z).
ang: Field of view angle in radians.
close and far: Near and far clipping planes for the ray marching algorithm.
Feel free to experiment with these values to see how the visualization changes!

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this code as you like.

Acknowledgements
Special thanks to the creators of the tkinter library for providing a simple and effective way to create graphical user interfaces in Python.
