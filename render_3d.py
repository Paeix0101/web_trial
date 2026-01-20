import pyrender
import trimesh
import numpy as np
from PIL import Image  # For saving the image

# Create a simple 3D sphere mesh
sphere = trimesh.creation.icosphere(subdivisions=3, radius=1.0, color=[1.0, 0.0, 0.0, 1.0])  # Red sphere

# Convert to pyrender mesh
mesh = pyrender.Mesh.from_trimesh(sphere)

# Set up the scene
scene = pyrender.Scene(ambient_light=[0.5, 0.5, 0.5])
scene.add(mesh)

# Add a camera (perspective view)
camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0, aspectRatio=1.0)
camera_pose = np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 2.0],  # Position camera 2 units away
    [0.0, 0.0, 0.0, 1.0]
])
scene.add(camera, pose=camera_pose)

# Add a light
light = pyrender.DirectionalLight(color=[1.0, 1.0, 1.0], intensity=3.0)
scene.add(light, pose=camera_pose)  # Light from camera direction

# Offscreen render to get the image
renderer = pyrender.OffscreenRenderer(viewport_width=800, viewport_height=600)
color, depth = renderer.render(scene)

# Save the rendered image using Pillow
image = Image.fromarray(color)
image.save('3d_sphere_render.png')
print("Image saved as '3d_sphere_render.png'")